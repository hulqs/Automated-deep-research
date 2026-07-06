"""
Image search tool -- retrieves relevant CC-licensed images from Wikimedia Commons
and other free image sources for research reports.
"""
import hashlib
import urllib.parse
from typing import Optional


class ImageSearchTool:
    """Search for free-to-use images from Wikimedia Commons and other sources."""

    BASE_URL = "https://commons.wikimedia.org/w/api.php"

    @staticmethod
    async def search(
        query: str,
        limit: int = 5,
        thumb_width: int = 600,
    ) -> list[dict]:
        """
        Search Wikimedia Commons for images matching the query.
        Returns a list of image metadata dicts.
        """
        import aiohttp

        results = []

        # Search Wikimedia Commons for files
        params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": f"{query} filetype:bitmap",
            "srnamespace": "6",  # File namespace
            "srlimit": min(limit * 2, 20),
            "srprop": "snippet|titlesnippet",
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    ImageSearchTool.BASE_URL, params=params, timeout=aiohttp.ClientTimeout(total=15)
                ) as resp:
                    if resp.status != 200:
                        return results
                    data = await resp.json()
        except Exception:
            return results

        page_titles = []
        for item in data.get("query", {}).get("search", []):
            title = item.get("title", "")
            if title.startswith("File:"):
                page_titles.append(title)

        if not page_titles:
            return results

        # Get image info (URLs, dimensions, license)
        image_params = {
            "action": "query",
            "format": "json",
            "prop": "imageinfo",
            "titles": "|".join(page_titles[:limit]),
            "iiprop": "url|size|extmetadata|mime",
            "iiurlwidth": thumb_width,
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    ImageSearchTool.BASE_URL, params=image_params, timeout=aiohttp.ClientTimeout(total=15)
                ) as resp:
                    if resp.status != 200:
                        return results
                    img_data = await resp.json()
        except Exception:
            return results

        for page_id, page_info in img_data.get("query", {}).get("pages", {}).items():
            imageinfo = page_info.get("imageinfo", [])
            if not imageinfo:
                continue
            info = imageinfo[0]
            ext_meta = info.get("extmetadata", {})

            # Extract license info
            license_name = ext_meta.get("LicenseShortName", {}).get("value", "Unknown")
            license_url = ext_meta.get("LicenseUrl", {}).get("value", "")
            attribution = ext_meta.get("Artist", {}).get("value", "")

            results.append({
                "title": page_info.get("title", "").replace("File:", ""),
                "url": info.get("thumburl") or info.get("url", ""),
                "original_url": info.get("url", ""),
                "width": info.get("thumbwidth") or info.get("width", 0),
                "height": info.get("thumbheight") or info.get("height", 0),
                "source": "wikimedia",
                "license": license_name,
                "license_url": license_url,
                "attribution": attribution,
                "description": ext_meta.get("ImageDescription", {}).get("value", ""),
            })

        return results

    @staticmethod
    def generate_placeholder_url(
        topic: str,
        width: int = 800,
        height: int = 400,
        index: int = 0,
    ) -> str:
        """
        DEPRECATED: This method is no longer used in the main pipeline.
        Images are now only embedded when real images are found from
        source materials or Wikimedia Commons. No placeholder fallback.

        Kept for backward compatibility with any external callers.
        """
        # Use a stable seed based on topic for consistent placeholders
        seed = int(hashlib.md5(topic.encode()).hexdigest()[:8], 16) % 1000
        return f"https://picsum.photos/seed/{seed + index}/{width}/{height}"
