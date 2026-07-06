"""
Image Agent: Enhances research reports with relevant images.

The ImageAgent analyzes the report structure and source materials,
identifying positions where images from cited academic sources
would genuinely enhance understanding. Images are ONLY added when
they come from or are directly referenced in the source materials.
"""
import logging
from app.agents.base import BaseAgent
from app.tools.image_search import ImageSearchTool

logger = logging.getLogger(__name__)

IMAGE_SYSTEM = """You are a strict academic image editor. Your role is to evaluate whether ANY images, diagrams, charts, or figures from the source materials would genuinely enhance the research report.

CRITICAL RULES — follow them exactly:

1. ONLY suggest an image when BOTH of these are true:
   (a) The search results / source materials explicitly contain or reference a specific image, figure, chart, diagram, or illustration.
   (b) That image would genuinely help the reader understand the corresponding section of the report.

2. If the source materials do NOT contain any images or figures, return ZERO placements. An empty list is the CORRECT answer when no suitable images exist. Never invent images.

3. Each placement MUST cite which source URL or source title contains the image. Without a source reference, do NOT suggest the placement.

4. Do NOT suggest decorative images. Every image must have clear academic value — it should explain a concept, show data, illustrate a methodology, or present a framework that is discussed in the report text.

5. Search queries must be derived from the ACTUAL source material, not invented. Use the exact terminology found in the sources.

6. Allow 0-4 placements. Zero is perfectly fine and often correct. Do NOT feel obligated to suggest images.

7. If the report is in Chinese, write captions and queries in Chinese.

Output format: Return a JSON object with a "placements" array. Each placement has:
- section_title: exact section header from the report
- position_after: a short unique excerpt from the report text to locate insertion point
- caption: descriptive academic caption (cite which source the image is from)
- search_query: specific keyword query derived from the source material
- visual_type: "photo"|"diagram"|"chart"|"infographic"|"map"|"illustration"
- importance: "high"|"medium"|"low"
- source_reference: the URL or title of the source that contains this image"""


class ImageAgent(BaseAgent):
    """Identifies optimal image placements and retrieves relevant images for reports."""

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str | None = None,
    ):
        super().__init__(api_key=api_key, base_url=base_url, model=model)

    async def identify_image_placements(
        self,
        topic: str,
        report_content: str,
        key_concepts: list[str] = None,
        search_results: list[dict] = None,
    ) -> list[dict]:
        """
        Analyze the report and source materials to identify where images should be placed.

        ONLY suggests images when the source materials actually contain or reference images.

        Returns a list of image placement dicts with:
        - section_title: the section header to place the image after
        - caption: descriptive caption for the image
        - search_query: specific query to find the image
        - visual_type: type of visual (photo, diagram, chart, etc.)
        - importance: "high" | "medium" | "low"
        - source_reference: URL or title of the source containing this image
        """
        # Truncate report for LLM context
        report_excerpt = report_content[:4000]

        # Build source materials context — this is critical for the LLM
        # to determine if any sources actually contain images
        sources_text = ""
        if search_results:
            source_lines = []
            seen = set()
            for r in search_results[:30]:
                url = r.get("url", "")
                title = r.get("title", "")
                if url and url not in seen:
                    seen.add(url)
                    snippet = r.get("snippet", "") or r.get("content", "") or ""
                    # Include first 200 chars of content so LLM can see if it mentions figures/images
                    snippet_short = snippet[:200] if snippet else ""
                    source_lines.append(
                        f"- [{title}]({url})\n  source: {r.get('source', 'web')}\n  snippet: {snippet_short}"
                    )
            sources_text = "\n".join(source_lines)

        key_concepts_text = ""
        if key_concepts:
            key_concepts_text = "Key concepts: " + ", ".join(key_concepts[:10])

        user_prompt = f"""Topic: {topic}
{key_concepts_text}

=== SOURCE MATERIALS (check if any contain images/figures/charts) ===
{sources_text[:3000] if sources_text else "No source materials provided. Return empty placements."}

=== REPORT CONTENT ===
{report_excerpt}
===

Analyze the source materials above and the report content. ONLY suggest image placements when the source materials explicitly contain or reference images, figures, charts, or diagrams.

Return ONLY valid JSON (no markdown, no extra text):

{{
    "placements": [
        {{
            "section_title": "exact section header from the report where image should appear",
            "position_after": "the text content after which to insert the image (short excerpt)",
            "caption": "descriptive academic caption for the image (cite which source it comes from)",
            "search_query": "specific keyword query derived from the SOURCE MATERIAL, not invented",
            "visual_type": "photo|diagram|chart|infographic|map|illustration",
            "importance": "high|medium|low",
            "source_reference": "URL or title of the source that contains/references this image"
        }}
    ]
}}

CRITICAL REMINDERS:
- If NO source materials contain images or figures, return {{"placements": []}}
- Only suggest an image when a SPECIFIC source references it
- section_title MUST match an actual section header in the report
- Do NOT invent images — empty placements array is the CORRECT answer when no real images exist
- 宁缺毋滥 — better no image than an irrelevant one"""

        result = await self.call_llm_json(IMAGE_SYSTEM, user_prompt, temperature=0.2)
        placements = result.get("placements", [])

        # Filter out placements without source references
        valid_placements = [p for p in placements if p.get("source_reference")]

        if len(valid_placements) < len(placements):
            logger.info(
                f"ImageAgent filtered out {len(placements) - len(valid_placements)} "
                f"placements without source references"
            )

        logger.info(f"ImageAgent identified {len(valid_placements)} valid image placements (from {len(placements)} total)")
        return valid_placements

    async def fetch_images_for_placements(
        self,
        placements: list[dict],
    ) -> list[dict]:
        """
        Fetch actual images for each placement from Wikimedia Commons.
        ONLY returns placements that successfully found a real image.
        If no image is found for a placement, it is skipped — no placeholders.
        """
        enriched = []
        for i, placement in enumerate(placements):
            search_query = placement.get("search_query", "")
            if not search_query:
                logger.info(f"Skipping placement #{i}: no search query")
                continue

            # Try to find images from Wikimedia Commons
            images = await ImageSearchTool.search(
                query=search_query,
                limit=3,
                thumb_width=800,
            )

            if images:
                best = images[0]
                placement["image_url"] = best.get("url", "")
                placement["image_source"] = best.get("source", "wikimedia")
                placement["image_license"] = best.get("license", "Unknown")
                placement["image_attribution"] = best.get("attribution", "")
                placement["image_title"] = best.get("title", "")
                placement["image_width"] = best.get("width", 800)
                placement["image_height"] = best.get("height", 400)
                # Add alternative images
                placement["alternatives"] = [
                    {"url": alt.get("url", ""), "title": alt.get("title", "")}
                    for alt in images[1:3]
                ]
                enriched.append(placement)
                logger.info(
                    f"ImageAgent found image for placement #{i}: "
                    f"query='{search_query[:60]}', title='{best.get('title', '')[:60]}'"
                )
            else:
                # NO placeholder fallback — skip this placement entirely
                logger.info(
                    f"ImageAgent skipping placement #{i}: "
                    f"no images found for query='{search_query[:60]}'. "
                    f"Placement skipped (no placeholder)."
                )

        logger.info(
            f"ImageAgent fetched images for {len(enriched)}/{len(placements)} placements "
            f"({len(placements) - len(enriched)} skipped — no images found)"
        )
        return enriched

    async def embed_images_in_report(
        self,
        report_content: str,
        placements: list[dict],
    ) -> str:
        """
        Insert images into the report Markdown at the identified positions.

        Uses section headers and position_after excerpts to locate insertion points
        and embeds images with proper Markdown formatting.
        """
        if not placements:
            return report_content

        lines = report_content.split("\n")
        result_lines = []
        placed_indices = set()  # track which placements have been used

        for i, line in enumerate(lines):
            result_lines.append(line)

            # Check if any placement should be inserted after this line
            for p_idx, placement in enumerate(placements):
                if p_idx in placed_indices:
                    continue

                section_title = placement.get("section_title", "")
                position_after = placement.get("position_after", "")

                # Match by section header -- insert image after the section header line
                # We look for the target section and insert after the section's first paragraph
                if section_title and _is_section_header(line, section_title):
                    # Mark as pending -- we'll insert after next substantial paragraph
                    placed_indices.add(p_idx)
                    # Insert image markdown right after the section header
                    result_lines.append("")
                    result_lines.append(_format_image_markdown(placement))
                    result_lines.append("")
                    continue

                # Match by content excerpt -- insert after matching line
                if position_after and _line_contains_excerpt(line, position_after):
                    placed_indices.add(p_idx)
                    result_lines.append("")
                    result_lines.append(_format_image_markdown(placement))
                    result_lines.append("")

        # If any placements weren't matched by section/content, append them
        # near relevant sections at the end of each major section
        for p_idx, placement in enumerate(placements):
            if p_idx not in placed_indices:
                # Find the closest section header and insert there
                section_title = placement.get("section_title", "")
                best_pos = _find_best_insertion_point(lines, section_title)
                if best_pos is not None and best_pos < len(result_lines):
                    result_lines.insert(best_pos, "")
                    result_lines.insert(best_pos + 1, _format_image_markdown(placement))
                    result_lines.insert(best_pos + 2, "")

        return "\n".join(result_lines)


def _is_section_header(line: str, section_title: str) -> bool:
    """Check if a line is a Markdown section header matching the title."""
    stripped_line = line.strip().lstrip("#").strip()
    stripped_title = section_title.strip().lstrip("#").strip()
    # Allow partial match
    return bool(stripped_line and stripped_title and
                (stripped_line == stripped_title or
                 stripped_title in stripped_line or
                 stripped_line in stripped_title))


def _line_contains_excerpt(line: str, excerpt: str) -> bool:
    """Check if a line contains the given text excerpt."""
    if not excerpt or len(excerpt) < 10:
        return False
    # Clean both for comparison
    clean_line = line.strip().lower()
    clean_excerpt = excerpt.strip().lower()
    return clean_excerpt[:30] in clean_line


def _find_best_insertion_point(lines: list[str], section_title: str) -> int | None:
    """Find the best position to insert an image near a given section."""
    for i, line in enumerate(lines):
        if _is_section_header(line, section_title):
            # Insert after section header + 1 line
            return min(i + 2, len(lines))
    # Fallback: append near the end, before references
    for i, line in enumerate(lines):
        if line.strip().startswith("##") and ("参考" in line or "reference" in line.lower()):
            return i
    return len(lines)


def _format_image_markdown(placement: dict) -> str:
    """Format an image placement as Markdown with caption and attribution."""
    image_url = placement.get("image_url", "")
    caption = placement.get("caption", "")
    visual_type = placement.get("visual_type", "")
    attribution = placement.get("image_attribution", "")
    source = placement.get("image_source", "")
    license_info = placement.get("image_license", "")

    alt_text = caption[:100] if caption else "Research illustration"

    # Build the figure markdown
    lines = [
        f"![{alt_text}]({image_url})",
        "",
    ]

    if caption:
        type_label = f"*[{visual_type.capitalize()}]* " if visual_type else ""
        lines.append(f"*{type_label}{caption}*")

    # Add attribution line for CC-licensed images
    if attribution or license_info:
        attr_parts = []
        if attribution:
            attr_parts.append(f"图片来源: {attribution}")
        if license_info and license_info != "Unknown":
            attr_parts.append(f"许可: {license_info}")
        if source:
            attr_parts.append(f"来源: {source.capitalize()}")
        lines.append(f"  {' | '.join(attr_parts)}")

    return "\n".join(lines)
