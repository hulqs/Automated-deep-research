---
name: Summarization Agent Skill
description: 学术内容总结智能体。逐轮综合检索结果，提取关键发现和论点，识别矛盾，构建结构化知识节点（Knowledge Nodes），并生成最终的综合学术摘要。
---

# Summarization Agent（内容总结智能体）

**Agent 3** — 知识提炼引擎。分两个层次工作：逐轮摘要 + 最终综合摘要，同时构建结构化的知识节点（Knowledge Nodes）。

## 能力

- **逐轮摘要**：对每轮搜索结果进行即时总结，生成 Markdown 格式摘要
- **关键发现提取**：从材料中提取核心事实、论点和发现
- **矛盾识别**：识别不同来源之间的信息冲突
- **知识节点构建**：将信息组织为 `concept` / `fact` / `reference` 三类节点
- **残留问题跟踪**：标记每轮后仍待解答的问题
- **最终综合摘要**：合并所有轮次摘要，生成包含概述、核心发现、不同观点、知识空白、参考文献的综合学术摘要
- **来源引用**：始终注明信息来源
- **语言感知**：输入为中文则输出中文摘要

## 核心方法

### `summarize_round(topic, results, round_num) → dict`

对单轮搜索结果进行摘要。

```json
{
    "round_summary": "Markdown 格式的摘要文本",
    "key_findings": ["发现1", "发现2"],
    "knowledge_nodes": [
        {
            "title": "节点标题",
            "content": "节点内容",
            "node_type": "concept|fact|reference",
            "confidence": 0.85
        }
    ],
    "remaining_questions": ["待解答问题"]
}
```

- 输入截断：最多处理 30 条结果，每条 snippet 最多 800 字符，总输入 ≤ 12000 字符
- JSON 模式输出，含严格 JSON 规则提示

### `final_summary(topic, all_rounds) → str`

综合所有轮次的摘要，生成最终学术摘要。

输出 Markdown 格式，包含章节：
- `## 概述`
- `## 核心发现`
- `## 不同观点`
- `## 知识空白`
- `## 参考文献`

- 输入截断：每轮摘要最多 2000 字符，总输入 ≤ 8000 字符
- 使用 `call_llm()`（文本模式，非 JSON）

## 技术实现

- 继承 `BaseAgent`
- 日志记录输入长度便于调试
- 增强的 JSON 规则提示确保输出格式正确
- 知识节点带 `confidence` 置信度评分

## 相关技能

- [[search-agent]] — 提供待总结的搜索结果
- [[report-agent]] — 使用总结生成最终报告
- [[deep-research]] — 编排器中的第三阶段
