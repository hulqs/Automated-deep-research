import httpx, xml.etree.ElementTree as ET
from typing import List, Dict, Any
from app.config import setting

class ArxivSearchTool:
    BASE_URL = "http://export.arxiv.org/api/query"

    @staticmethod
    async def search(query: str, max_results: int = None, start: int = 0) -> List[Dict[str, Any]]:
        max_results = max_results or setting.ARXIV_MAX_RESULTS
        params = {"search_query": f"all:{query}", "max_results": max_results, "start": start, "sortBy": "relevance"}
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.get(ArxivSearchTool.BASE_URL, params=params)
            return ArxivSearchTool._parse_response(resp.text)

    @staticmethod
    def _parse_response(xml_text: str) -> List[Dict[str, Any]]:
        ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
        root = ET.fromstring(xml_text)
        results = []
        for entry in root.findall("atom:entry", ns):
            title = entry.find("atom:title", ns)
            summary = entry.find("atom:summary", ns)
            lid = entry.find("atom:id", ns)
            pub = entry.find("atom:published", ns)
            authors = [a.find("atom:name", ns).text for a in entry.findall("atom:author", ns) if a.find("atom:name", ns) is not None]
            results.append({
                "title": title.text.strip() if title is not None and title.text else "",
                "snippet": (summary.text or "")[:500] if summary is not None else "",
                "url": lid.text.strip() if lid is not None and lid.text else "",
                "source": "arxiv", "relevance_score": 0.7,
                "authors": authors,
                "published": pub.text if pub is not None else "",
            })
        return results
