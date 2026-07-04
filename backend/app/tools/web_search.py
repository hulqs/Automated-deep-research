import httpx
from typing import List, Dict, Any
from bs4 import BeautifulSoup

class WebSearchTool:
    """General web search and scraping tool."""

    @staticmethod
    async def scrape_page(url: str) -> Dict[str, Any]:
        async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
            try:
                resp = await client.get(url, headers={"User-Agent": "Mozilla/5.0 (compatible; ResearchBot/1.0)"})
                soup = BeautifulSoup(resp.text, "lxml")
                title = soup.title.string if soup.title else ""
                for tag in soup(["script", "style", "nav", "footer", "header"]):
                    tag.decompose()
                text = soup.get_text(separator="\n", strip=True)
                return {"title": title, "content": text[:5000], "url": url, "source": "web"}
            except Exception as e:
                return {"title": "", "content": "", "url": url, "source": "web", "error": str(e)}

    @staticmethod
    async def search(query: str) -> List[Dict[str, Any]]:
        # Use DuckDuckGo HTML search as a fallback
        url = "https://html.duckduckgo.com/html/"
        async with httpx.AsyncClient(timeout=30.0) as client:
            try:
                resp = await client.post(url, data={"q": query}, headers={"User-Agent": "Mozilla/5.0"})
                soup = BeautifulSoup(resp.text, "lxml")
                results = []
                for r in soup.select(".result")[:10]:
                    a_tag = r.select_one(".result__a")
                    snippet_tag = r.select_one(".result__snippet")
                    if a_tag:
                        results.append({
                            "title": a_tag.get_text(strip=True),
                            "url": a_tag.get("href", ""),
                            "snippet": snippet_tag.get_text(strip=True) if snippet_tag else "",
                            "source": "web", "relevance_score": 0.5,
                        })
                return results
            except Exception:
                return []
