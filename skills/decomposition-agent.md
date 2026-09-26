---
name: Decomposition Agent Skill
description: 将复杂的研究主题自动拆解为多个可检索的子问题（Sub-Questions）和具体搜索查询（Search Queries），提取关键概念和术语，并建议搜索来源。
---

# Decomposition Agent（问题分解智能体）

**Agent 1** — 研究流水线的入口阶段。使用 LangChain `ChatPromptTemplate`，将用户输入的宽泛研究主题转化为结构化的、可执行的检索计划。

## 能力

- **子问题拆解**：将主题拆分为 3-7 个聚焦的子问题
- **搜索查询生成**：为每个子问题生成 1-3 条具体搜索查询
- **来源建议**：为每条查询指定搜索来源（`wikipedia` / `arxiv` / `web`）
- **语言感知**：输入为中文则输出中文子问题和查询；英文输入则输出英文
- **关键概念提取**：识别核心概念和术语
- **深度建议**：给出研究深度评估（`basic` / `moderate` / `deep`）

## 输入

| 参数 | 类型 | 说明 |
|------|------|------|
| `topic` | `str` | 研究主题（必填） |
| `description` | `str` | 研究描述/目标（可选，默认 `"N/A"`） |

## 输出（JSON）

```json
{
    "sub_questions": [
        {
            "question": "子问题文本",
            "keywords": ["关键词1", "关键词2"],
            "queries": [
                {
                    "query": "搜索查询字符串",
                    "source": "wikipedia|arxiv|web",
                    "lang": "zh|en"
                }
            ]
        }
    ],
    "key_concepts": ["概念1", "概念2"],
    "suggested_depth": "basic|moderate|deep",
    "domain": "学科领域"
}
```

## 使用示例

```python
from app.agents.decomposition_agent import DecompositionAgent

agent = DecompositionAgent(api_key="...", base_url="...", model="...")
result = await agent.decompose(
    topic="量子计算在药物发现中的应用",
    description="探索量子计算如何加速药物分子模拟和筛选"
)
# result["sub_questions"] → 子问题列表
# result["key_concepts"] → ["量子计算", "药物发现", "分子模拟", "量子化学"]
```

## 技术实现

- 继承 `BaseAgent`
- 使用 `ChatPromptTemplate.format_messages()` 构建提示词
- 通过 `call_llm_json()` 返回结构化 JSON（含 `json-repair` 自动修复）
- 模型：默认 `deepseek-v4-flash`，支持通过构造函数覆盖

## 相关技能

- [[search-agent]] — 使用本 Agent 输出的查询进行搜索
- [[deep-research]] — 编排器中的第一阶段
