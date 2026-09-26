---
name: Deep Research Agent Skill
description: 一个完整的学术研究流水线，采用多智能体（Multi-Agent）协同编排。系统能够自动分解研究主题，跨 Wikipedia、ArXiv 和互联网进行信息检索，综合分析研究结果，并最终生成结构化的 Markdown 学术报告及 TODO 研究计划。
---

# Deep Research Orchestrator（深度研究编排器）

编排器（`ResearchOrchestrator`）是整个系统的核心调度器，按顺序驱动 6 个 AI Agent 协同完成学术研究任务。

## Agent 流水线（6 阶段）

| 阶段 | Agent | 职责 |
|------|-------|------|
| 1 | **DecompositionAgent** | 将研究主题拆解为子问题和搜索查询 |
| 2 | **SearchAgent** | 多轮搜索（最多 3 轮），覆盖 Wikipedia / arXiv / Web |
| 3 | **SummarizationAgent** | 逐轮总结 + 最终综合摘要，构建知识节点 |
| 4 | **TodoPlannerAgent** | 生成带自评（≥7/10）的研究 TODO 计划 |
| 5 | **ReportAgent** | 生成结构化 Markdown 学术报告 |
| 6 | **ImageAgent** | 分析源材料中的图片，从 Wikimedia Commons 获取 CC 许可图片并嵌入报告 |

所有 Agent 均继承 `BaseAgent`，通过 `call_llm()`（文本，4000 tokens）和 `call_llm_json()`（JSON 模式，8192 tokens，含 `json-repair` 自动修复）调用 LLM。

## 执行流程

1. **问题分解** → 提取关键词、子问题、搜索查询
2. **分轮搜索** → 每轮搜索后评估完整性，识别知识空白
3. **逐轮总结** → 每轮生成摘要 + 保存中间报告（`IntermediateReport`）
4. **最终摘要** → 综合所有轮次生成最终学术摘要
5. **TODO 规划** → 生成分阶段研究计划，自评不达标则重试（最多 2 次）
6. **报告生成** → 含摘要、引言、文献综述、核心分析、研究发现、结论、参考文献
7. **图像增强** → 仅在源材料包含图片时才嵌入（宁缺毋滥）

## 配置回退链

**DB user_settings → .env → 硬编码默认值**

## API 接口

| 方法 | 路径 | 说明 |
|------|------|------|
| `POST` | `/api/research/` | 创建研究任务 |
| `POST` | `/api/research/{id}/run` | 启动完整研究流程 |
| `GET` | `/api/research/{id}` | 查看研究任务及生成的报告 |
| `GET` | `/api/research/` | 列出用户的所有研究任务 |
| `GET`  | `/api/articles/` | 管理文章资源 |
| `POST` | `/api/auth/register` | 用户注册 |
| `POST` | `/api/auth/login` | 用户登录 |

## 环境配置

```bash
# 必填：LLM API Key（兼容 OpenAI / DeepSeek 等）
OPENAI_API_KEY=your-api-key

# 可选：自定义 API 地址和模型
OPENAI_BASE_URL=https://api.deepseek.com
OPENAI_MODEL=deepseek-v4-flash

# 可选：搜索配置
WIKIPEDIA_LANG=zh
ARXIV_MAX_RESULTS=20
```

## 子技能

本技能由以下子 Agent 技能组成，可独立调用：

- [[decomposition-agent]] — 问题分解
- [[search-agent]] — 多源搜索
- [[summarization-agent]] — 内容总结
- [[report-agent]] — 报告生成
- [[todo-planner-agent]] — TODO 计划
- [[image-agent]] — 图像增强
