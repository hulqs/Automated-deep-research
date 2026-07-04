"""
LangChain tool wrappers for search capabilities.
"""
from langchain_core.tools import tool
from typing import List, Optional
from app.tools.wikipedia_search import WikipediaSearchTool
from app.tools.arxiv_search import ArxivSearchTool
from app.tools.web_search import WebSearchTool


@tool
async def search_wikipedia(query: str, lang: str = "zh", limit: int = 10) -> str:
    """Search Wikipedia for information on a topic. Returns article titles and snippets.
    
    Args:
        query: The search query
        lang: Language code (zh for Chinese, en for English)
        limit: Maximum number of results
    """
    results = await WikipediaSearchTool.search(query, lang=lang, limit=limit)
    if not results:
        return "No Wikipedia results found."
    return "\n\n".join(
        f"[{r['title']}]({r['url']})\n{r['snippet'][:300]}"
        for r in results[:limit]
    )


@tool
async def search_arxiv(query: str, max_results: int = 10) -> str:
    """Search arXiv for academic papers on a topic. Returns paper titles, authors, and abstracts.
    
    Args:
        query: The search query
        max_results: Maximum number of results
    """
    results = await ArxivSearchTool.search(query, max_results=max_results)
    if not results:
        return "No arXiv results found."
    return "\n\n".join(
        f"[{r['title']}]({r['url']})\nAuthors: {', '.join(r.get('authors', []))}\n{r['snippet'][:300]}"
        for r in results[:max_results]
    )


@tool
async def search_web(query: str) -> str:
    """Search the web using DuckDuckGo for general information. Returns page titles, URLs, and snippets.
    
    Args:
        query: The search query
    """
    results = await WebSearchTool.search(query)
    if not results:
        return "No web results found."
    return "\n\n".join(
        f"[{r['title']}]({r['url']})\n{r['snippet'][:300]}"
        for r in results[:10]
    )


# Collect all search tools
SEARCH_TOOLS = [search_wikipedia, search_arxiv, search_web]
