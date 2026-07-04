import httpx
from typing import List, Dict, Any
from app.config import setting

class WikipediaSearchTool:
    """Wikipedia API search tool with multilingual support."""

    BASE_URL = "https://{lang}.wikipedia.org/w/api.php"

    @staticmethod
    async def search(query: str, lang: str = None, limit: int = 10) -> List[Dict[str, Any]]:
        lang = lang or setting.WIKIPEDIA_LANG
        url = WikipediaSearchTool.BASE_URL.format(lang=lang)
        params = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": query,
            "srlimit": limit,
            "srprop": "snippet|titlesnippet",
        }
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.get(url, params=params)
            data = resp.json()
            results = []
            for item in data.get("query", {}).get("search", []):
                results.append({
                    "title": item.get("title", ""),
                    "snippet": WikipediaSearchTool._clean_html(item.get("snippet", "")),
                    "url": f"https://{lang}.wikipedia.org/wiki/{item.get('title', '').replace(' ', '_')}",
                    "source": "wikipedia",
                    "relevance_score": 0.8,
                    "page_id": item.get("pageid"),
                })
            return results

    @staticmethod
    async def get_page_content(title: str, lang: str = None) -> Dict[str, Any]:
        lang = lang or setting.WIKIPEDIA_LANG
        url = WikipediaSearchTool.BASE_URL.format(lang=lang)
        params = {
            "action": "query",
            "format": "json",
            "titles": title,
            "prop": "extracts",
            "exintro": True,
            "explaintext": True,
        }
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.get(url, params=params)
            data = resp.json()
            pages = data.get("query", {}).get("pages", {})
            for pid, page in pages.items():
                return {
                    "title": page.get("title", ""),
                    "content": page.get("extract", ""),
                    "page_id": pid,
                }
            return {}

    @staticmethod
    def _clean_html(text: str) -> str:
        import re
        return re.sub(r'<[^>]+>', '', text)
