---
name: Search Agent Skill
description: 多轮跨源学术搜索智能体。在 Wikipedia、ArXiv 和互联网上执行搜索查询，评估信息完整性，识别知识空白，并动态决定是否需要更多轮次搜索。
---

# Search Agent（多源搜索智能体）

**Agent 2** — 信息收集引擎。支持最多 3 轮搜索，每轮后由 LLM 评估信息充分性，自动识别知识空白并生成补充查询建议。

## 能力

- **多源并行搜索**：通过 `SearchAggregator` 同时在 Wikipedia、ArXiv、Web 上搜索
- **URL 去重**：自动过滤重复 URL
- **相关性排序**：按 `relevance_score` 降序排列结果
- **完整性评估**：LLM 评估已收集信息是否充分回答研究主题
- **知识空白识别**：自动发现未覆盖的子话题，生成建议补充查询
- **轮次控制**：最多 3 轮，信息充分或达到上限时自动停止

## 搜索来源

| 来源 | 工具类 | 说明 |
|------|--------|------|
| `wikipedia` | `WikipediaSearchTool` | Wikipedia API，支持多语言（默认 `zh`） |
| `arxiv` | `ArxivSearchTool` | arXiv Atom XML API，最多 20 条结果 |
| `web` | `WebSearchTool` | DuckDuckGo HTML 抓取，通用网页搜索 |

## 核心方法

### `search_round(queries, round_num) → dict`

执行一轮搜索，遍历所有查询并聚合结果。

```python
round_data = await agent.search_round(all_queries, round_num=1)
# 返回: {"round": 1, "results": [...], "result_count": N}
```

### `evaluate_completeness(topic, results, queries_used) → dict`

评估信息完整性，识别知识空白。

```json
{
    "is_sufficient": true,
    "knowledge_gaps": [
        {
            "topic": "空白主题",
            "reason": "缺失原因",
            "suggested_queries": ["建议补充查询"]
        }
    ],
    "confidence": 0.85
}
```

## 编排器中的使用

```python
# Phase 2: 分轮次搜索（最多 3 轮）
for round_num in range(1, MAX_ROUNDS + 1):
    round_data = await searcher.search_round(all_queries, round_num)
    all_results.extend(round_data["results"])

    eval_result = await searcher.evaluate_completeness(topic, all_results, all_queries)
    gaps = eval_result.get("knowledge_gaps", [])

    if eval_result.get("is_sufficient") or round_num >= MAX_ROUNDS:
        break
```

## 技术实现

- 继承 `BaseAgent`
- `SearchAggregator.search()` 并行搜索 + URL 去重 + 相关性排序
- 完整性评估通过 `ChatPromptTemplate` + `call_llm_json()` 实现
- 结果限制：`search_results` 最多保留 50 条，`knowledge_gaps` 最多 20 条

## 相关技能

- [[decomposition-agent]] — 提供搜索查询
- [[summarization-agent]] — 对搜索结果进行总结
- [[deep-research]] — 编排器中的第二阶段
