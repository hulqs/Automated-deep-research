from app.tools.wikipedia_search import WikipediaSearchTool
from app.tools.arxiv_search import ArxivSearchTool
from app.tools.web_search import WebSearchTool
from app.tools.langchain_tools import SEARCH_TOOLS, search_wikipedia, search_arxiv, search_web

class SearchAggregator:
    """Unified search across Wikipedia, ArXiv, and web."""

    TOOLS = {
        "wikipedia": WikipediaSearchTool,
        "arxiv": ArxivSearchTool,
        "web": WebSearchTool,
    }

    @staticmethod
    async def search(query: str, sources: list[str] = None) -> list[dict]:
        if sources is None:
            sources = ["wikipedia", "arxiv", "web"]
        results = []
        for src in sources:
            tool = SearchAggregator.TOOLS.get(src)
            if tool is None:
                continue
            try:
                res = await tool.search(query)
                results.extend(res)
            except Exception:
                pass
        seen = set()
        deduped = []
        for r in results:
            if r.get("url") not in seen:
                seen.add(r.get("url"))
                deduped.append(r)
        return sorted(deduped, key=lambda x: x.get("relevance_score", 0), reverse=True)
