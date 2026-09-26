---
name: Report Agent Skill
description: 学术报告生成智能体。基于研究摘要、搜索结果、知识节点和 TODO 计划，生成带有完整引用信息的结构化 Markdown 学术研究报告。
---

# Report Agent（报告生成智能体）

**Agent 5** — 最终输出生成器。将所有研究成果整合为结构严谨、引用完善的学术 Markdown 报告。

## 能力

- **结构化报告**：按学术规范生成完整报告架构
- **内联引用**：在正文中引用所有信息来源
- **学术语调**：保持严谨的学术写作风格
- **Markdown 排版**：使用标题、列表、引用块、表格等丰富格式
- **TODO 集成**：在报告中嵌入研究待办计划
- **语言感知**：中文主题使用中文撰写报告
- **可控温度**：使用 `temperature=0.4` 平衡创意与准确性

## 报告结构

生成的报告包含以下章节：

| 章节 | 标题 | 说明 |
|------|------|------|
| 摘要 | `## 摘要 (Abstract)` | 研究概要和核心结论 |
| 引言 | `## 1. 引言 (Introduction)` | 研究背景与问题陈述 |
| 文献综述 | `## 2. 研究现状 (Literature Review)` | 现有研究成果梳理 |
| 核心分析 | `## 3. 核心分析 (Analysis)` | 深度分析与论证 |
| 研究发现 | `## 4. 研究发现 (Findings)` | 关键发现与洞见 |
| 研究规划 | `## 5. 研究规划与待办 (Research Plan)` | 后续研究方向 |
| 结论 | `## 6. 结论 (Conclusion)` | 总结与展望 |
| 参考文献 | `## 参考文献 (References)` | 完整引用列表 |

## 输入参数

| 参数 | 类型 | 说明 |
|------|------|------|
| `topic` | `str` | 研究主题 |
| `summary` | `str` | 综合摘要（截断至 3000 字符） |
| `search_results` | `list[dict]` | 搜索结果（最多 30 条，URL 去重） |
| `knowledge_nodes` | `list[dict]` | 知识节点（最多 20 条） |
| `todo_plan` | `list[dict]` | TODO 计划项（最多 15 条） |

## 使用示例

```python
from app.agents.report_agent import ReportAgent

agent = ReportAgent(api_key="...", base_url="...", model="...")
report = await agent.generate_report(
    topic="量子计算在药物发现中的应用",
    summary=final_summary,
    search_results=all_results,
    knowledge_nodes=knowledge_nodes,
    todo_plan=todo_list
)
# report 是完整的 Markdown 字符串，可直接保存为 .md 文件
```

## 技术实现

- 继承 `BaseAgent`
- 使用 `call_llm()` 文本模式（非 JSON）
- 来源去重：URL 级别去重，避免重复引用
- 知识节点格式化：标题 + 类型 + 置信度 + 内容摘要
- TODO 集成：以 Markdown checkbox 格式嵌入

## 相关技能

- [[summarization-agent]] — 提供研究摘要
- [[todo-planner-agent]] — 提供 TODO 计划
- [[image-agent]] — 在报告生成后进行图像增强
- [[deep-research]] — 编排器中的第五阶段
