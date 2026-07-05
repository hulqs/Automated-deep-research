# Deep Research Agent System

> AI 驱动的学术研究代理系统 —— 输入一个研究主题，自动完成主题分解、多源搜索、内容总结和报告生成。

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/) [![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688.svg)](https://fastapi.tiangolo.com/) [![LangChain](https://img.shields.io/badge/LangChain-0.3+-green.svg)](https://www.langchain.com/) [![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red.svg)](https://www.sqlalchemy.org/) [![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-3178C6.svg)](https://www.typescriptlang.org/) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## 目录

-   [项目亮点](#-%E9%A1%B9%E7%9B%AE%E4%BA%AE%E7%82%B9)
-   [项目介绍](#-%E9%A1%B9%E7%9B%AE%E4%BB%8B%E7%BB%8D)
-   [技术栈](#-%E6%8A%80%E6%9C%AF%E6%A0%88)
-   [系统架构](#-%E7%B3%BB%E7%BB%9F%E6%9E%B6%E6%9E%84)
-   [核心设计](#-%E6%A0%B8%E5%BF%83%E8%AE%BE%E8%AE%A1)
-   [数据库设计](#-%E6%95%B0%E6%8D%AE%E5%BA%93%E8%AE%BE%E8%AE%A1)
-   [研究流水线详解](#-%E7%A0%94%E7%A9%B6%E6%B5%81%E6%B0%B4%E7%BA%BF%E8%AF%A6%E8%A7%A3)
-   [AI Agent 体系](#-ai-agent-%E4%BD%93%E7%B3%BB)
-   [前端设计](#-%E5%89%8D%E7%AB%AF%E8%AE%BE%E8%AE%A1)
-   [快速开始](#-%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B)
-   [配置指南](#-%E9%85%8D%E7%BD%AE%E6%8C%87%E5%8D%97)
-   [API 文档](#-api-%E6%96%87%E6%A1%A3)
-   [使用场景](#-%E4%BD%BF%E7%94%A8%E5%9C%BA%E6%99%AF)
-   [项目结构](#-%E9%A1%B9%E7%9B%AE%E7%BB%93%E6%9E%84)
-   [开发路线图](#-%E5%BC%80%E5%8F%91%E8%B7%AF%E7%BA%BF%E5%9B%BE)

---

## ✨ 项目亮点

### 🧠 多智能体流水线协作

系统设计了 **6 个专职 AI Agent**，以流水线模式协作完成深度研究任务。每个 Agent 承担独立职责，通过结构化的数据传递形成完整的知识加工链路。编排器（Orchestrator）负责状态管理与流程控制，支持任务取消和进度追踪。

### 🔍 多源异构搜索聚合

集成 **Wikipedia API**（多语言）、**arXiv API**（学术论文）和 **DuckDuckGo**（通用网页）三大搜索源。`SearchAggregator` 统一调度，自动完成结果去重、相关性排序和源标记，单次研究任务可检索数十条高质量信息源。

### 🔄 自适应多轮迭代研究

不同于传统单轮搜索，系统采用**最多 3 轮**的迭代研究策略。每轮搜索后由 AI 评估信息完整性，自动识别知识空白并生成补充搜索查询，确保研究深度。达到信息充足阈值或轮次上限后自动终止。

### 💬 自然语言意图理解

前端支持自然语言输入，后端 `/api/ai/parse-input` 接口通过 AI 分析用户意图，自动判断是"研究某个主题"还是"撰写一篇文章"，并提取标题、主题、关键词等结构化字段，实现零学习成本的使用体验。

### 🎨 五主题设计系统

前端基于 CSS 自定义属性（Design Tokens）构建了完整的设计系统，支持 **Dark Blue**、**Light**、**Emerald**、**Sunset**、**Purple** 五种主题一键切换。所有颜色、阴影、渐变均通过 CSS 变量驱动，实现了视觉风格的完全可替换。

### 🌐 国际化双语言支持

前端内置完整的中英文 i18n 方案（200+ 翻译键），通过 `data-i18n` 属性和 `t()` 辅助函数实现运行时语言切换，无需重新加载页面。

### ⚙️ 用户级 API 配置

每个用户可独立配置 API Key、Base URL 和模型名称。配置采用三级回退链：**用户数据库配置 → 全局 .env 配置 → 硬编码默认值**。支持 OpenAI、DeepSeek 等所有兼容 OpenAI 接口的服务商，且提供连接测试功能。

### 🖼️ 报告图像智能增强

`ImageAgent` 分析源材料中是否包含图表、图像引用，仅在源材料确实包含可视化内容时才通过 Wikimedia Commons API 检索合规的 CC 许可图片嵌入报告。严格遵循"宁缺毋滥"原则——无真实图片则不加，绝不使用占位图。

### 📋 待办计划自评估机制

`TodoPlannerAgent` 不仅生成研究待办计划，还内置了**生成-评估-修正**循环：评估器从主题相关性、需求覆盖度、结构完整性、逻辑连贯性四个维度打分，不达标则带入反馈重新生成（最多重试 2 次）。

### 🛡️ 鲁棒的 JSON 处理

LLM 输出的结构化数据经过**三层容错处理**：标准 JSON 解析 → `json-repair` 自动修复 → 失败时抛出明确异常。配合增强的系统提示词（明确 JSON 格式约束），大幅降低了因 LLM 输出格式异常导致的流程中断。

---

## 📖 项目介绍

**Deep Research Agent System** 是一个基于多智能体协作的深度研究系统。用户只需输入一个研究主题，系统便会自动调度多个 AI Agent 协同工作：将主题拆解为可搜索的子问题，从 Wikipedia、arXiv 及互联网等多个数据源搜集信息，经过多轮迭代搜索与总结，最终生成一份包含摘要、引言、文献综述、核心分析、研究发现、研究规划和结论的完整学术研究报告（Markdown 格式）。

项目采用 **FastAPI** 构建后端 REST API，纯 **TypeScript** 编写前端单页应用（零框架依赖），数据库使用 **SQLite**（异步驱动 `aiosqlite`），AI 能力基于 **LangChain** 框架接入 OpenAI 兼容接口（支持 OpenAI、DeepSeek 及任何兼容服务商）。

**主要应用场景：**

-   📚 学术文献综述的快速生成
-   🔬 技术调研与知识梳理
-   🌍 跨领域研究主题的探索
-   ✍️ 结构化写作辅助
-   🎓 学生的研究入门与文献检索

---

## 🔧 技术栈

### 后端

类别

技术

版本

用途

**Web 框架**

FastAPI

0.115.0

高性能异步 REST API

**ASGI 服务器**

Uvicorn

0.30.0

生产级 ASGI 服务

**ORM**

SQLAlchemy

2.0.35

异步数据库 ORM

**数据库驱动**

aiosqlite

0.20.0

SQLite 异步驱动

**数据校验**

Pydantic

2.9.0

请求/响应模型验证

**配置管理**

pydantic-settings

2.5.0

环境变量与 .env 配置

**AI 框架**

LangChain

0.3+

LLM 调用、Prompt 模板、输出解析

**LLM 适配**

langchain-openai

0.2.0

OpenAI 兼容接口适配

**OpenAI SDK**

openai

1.51.0

底层 API 通信

**认证**

python-jose

3.3.0

JWT 令牌生成与验证

**密码哈希**

passlib[bcrypt]

1.7.4

bcrypt 密码加密

**HTTP 客户端**

httpx

0.27.0

异步 HTTP 请求

**HTTP 客户端**

aiohttp

3.10.5

异步 HTTP 会话管理

**网页解析**

BeautifulSoup4

4.12.3

HTML 内容提取

**XML 解析**

lxml

5.3.0

高性能 HTML/XML 解析

**JSON 修复**

json-repair

0.25.0

自动修复 LLM 输出的畸形 JSON

**重试机制**

tenacity

9.0.0

指数退避重试策略

**环境变量**

python-dotenv

-

.env 文件加载

**CORS**

-

-

FastAPI 内置 CORSMiddleware

### 前端

类别

技术

版本

用途

**语言**

TypeScript

5.0+

类型安全的前端逻辑

**构建**

TypeScript Compiler

5.0+

TS → JS 编译

**开发服务器**

serve

14.2.0

静态文件服务

**样式方案**

CSS 自定义属性

-

设计系统与五主题切换

**字体**

Plus Jakarta Sans

-

Google Fonts 现代无衬线体

**国际化**

自研 i18n

-

纯 TypeScript 运行时翻译

### 外部服务

服务

用途

协议

**OpenAI / DeepSeek API**

LLM 推理（文本 + JSON 模式）

REST (OpenAI 兼容)

**Wikipedia API**

多语言百科搜索

REST (MediaWiki)

**arXiv API**

学术论文检索

REST (Atom XML)

**DuckDuckGo HTML**

通用网页搜索

HTML 解析

**Wikimedia Commons API**

CC 许可图片检索

REST (MediaWiki)

---

## 🏗️ 系统架构

### 总体架构

```
┌──────────────────────────────────────────────────────────┐
│                    Frontend (TypeScript)                   │
│                                                           │
│  仪表盘 │ 研究任务 │ 文章管理 │ 知识图谱                    │
│  五主题 · 中英文 · 自然语言输入 · 响应式设计                │
└──────────────────────┬───────────────────────────────────┘
                       │ REST API (JWT Bearer Token)
┌──────────────────────▼───────────────────────────────────┐
│                  FastAPI Backend                           │
│                                                           │
│  ┌──────────┬──────────┬───────────┬──────────────────┐  │
│  │ /auth    │ /users   │ /research │ /articles        │  │
│  │ 注册/登录 │ 用户管理  │ 研究任务   │ 文章+知识节点     │  │
│  ├──────────┼──────────┼───────────┼──────────────────┤  │
│  │ /ai      │ /settings│ /health   │                  │  │
│  │ 自然语言  │ API配置   │ 健康检查   │                  │  │
│  └──────────┴──────────┴───────────┴──────────────────┘  │
│                       │                                   │
│  ┌────────────────────▼───────────────────────────────┐  │
│  │          Research Orchestrator (编排器)             │  │
│  │                                                     │  │
│  │  Phase 1 ──▶ DecompositionAgent    (主题分解)       │  │
│  │  Phase 2 ──▶ SearchAgent          (多轮搜索+评估)   │  │
│  │             SummarizationAgent    (逐轮总结)        │  │
│  │  Phase 3 ──▶ SummarizationAgent   (最终综合)       │  │
│  │  Phase 4 ──▶ TodoPlannerAgent     (待办规划)       │  │
│  │  Phase 5 ──▶ ReportAgent          (报告生成)       │  │
│  │  Phase 6 ──▶ ImageAgent           (图像增强)       │  │
│  └────────────────────────────────────────────────────┘  │
│                       │                                   │
│  ┌────────────────────▼───────────────────────────────┐  │
│  │                Tools Layer (工具层)                  │  │
│  │  SearchAggregator ──┬── WikipediaSearchTool         │  │
│  │                     ├── ArxivSearchTool             │  │
│  │                     ├── WebSearchTool (DuckDuckGo)  │  │
│  │                     └── ImageSearchTool (Wikimedia) │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────┬───────────────────────────────────┘
                       │
┌──────────────────────▼───────────────────────────────────┐
│                   Data Layer (数据层)                      │
│  ┌─────────────┬──────────────┬──────────────────────┐   │
│  │ SQLite      │ Wikipedia    │ arXiv API            │   │
│  │ (aiosqlite) │ API          │ DuckDuckGo           │   │
│  └─────────────┴──────────────┴──────────────────────┘   │
└──────────────────────────────────────────────────────────┘
```

### 架构设计原则

原则

说明

**分层解耦**

API 层 → Service 层 → Agent/Orchestrator 层 → Tools 层，每层职责清晰

**依赖注入**

FastAPI `Depends()` 实现数据库会话、用户认证的依赖注入

**配置外置**

三级配置回退链（DB → .env → 默认值），环境无关

**异步优先**

全链路 `async/await`，数据库、HTTP、LLM 调用均为异步

**优雅降级**

ImageAgent 失败不影响报告主体，搜索源不可用时自动跳过

**状态可观测**

任务状态枚举（7 种状态）、进度百分比（0.0-1.0）、中间报告持久化

---

## 📐 核心设计

### BaseAgent：鲁棒的 LLM 调用基类

所有 Agent 继承自 `BaseAgent`，封装了：

-   **双模式 LLM 实例**：`self.llm`（文本模式，max_tokens=4000）和 `self.llm_json`（JSON 模式，max_tokens=8192，`response_format={"type": "json_object"}`）
-   **`call_llm()`**：通用文本调用，支持自定义 temperature
-   **`call_llm_json()`**：结构化 JSON 调用，包含三层容错：
    1.  标准 `json.loads()` 解析
    2.  `json-repair` 自动修复引号、逗号、括号等常见错误
    3.  失败则抛出包含原始内容的 `RuntimeError`
-   **增强系统提示词**：自动拼接 JSON 格式约束指令，减少 LLM 输出格式错误
-   **指数退避重试**：通过 `@retry` 装饰器实现（最多 2 次，指数等待 2-10 秒）

```python
# BaseAgent 核心结构
class BaseAgent:
    def __init__(self, api_key=None, base_url=None, model=None):
        # 回退链：参数 → 全局 setting → 硬编码默认
        self.llm = ChatOpenAI(...)       # 文本模式
        self.llm_json = ChatOpenAI(...)  # JSON 模式

    async def call_llm(system, user, temperature=0.3) -> str: ...
    
    @retry(stop=2, wait=exponential(2, 10))
    async def call_llm_json(system, user, temperature=0.2) -> dict:
        # 标准解析 → json-repair → 异常
```

### SearchAggregator：统一搜索聚合

```python
class SearchAggregator:
    TOOLS = {"wikipedia": WikipediaSearchTool, "arxiv": ArxivSearchTool, "web": WebSearchTool}

    @staticmethod
    async def search(query, sources=None) -> list[dict]:
        # 1. 并行/串行调用各搜索源
        # 2. URL 去重（保留首次出现）
        # 3. 按 relevance_score 降序排列
```

### 配置回退链

```
用户 Settings 页面配置 (DB: user_settings)
        ↓ 若为空
全局 .env 文件 (OPENAI_API_KEY, OPENAI_BASE_URL, OPENAI_MODEL)
        ↓ 若为空
硬编码默认值 (base_url="https://api.deepseek.com", model="deepseek-v4-flash")
```

### 任务取消机制

研究任务在后台异步执行，支持用户手动取消：

1.  前端调用 `POST /api/research/{id}/cancel`，将状态设为 `FAILED`
2.  `ResearchOrchestrator._is_cancelled()` 在每个阶段检查点查询数据库状态
3.  检测到取消后立即终止流水线，保留已生成的中间报告

---

## 🗃️ 数据库设计

### ER 图（核心实体）

```
users (用户)
  ├── 1:N ── research_tasks (研究任务)
  │             ├── 1:N ── todo_items (待办事项)
  │             └── 1:N ── intermediate_reports (中间报告)
  ├── 1:N ── articles (文章)
  ├── 1:N ── knowledge_nodes (知识节点)
  └── 1:1 ── user_settings (用户 API 配置)
```

### 数据模型详解

#### User（用户表）

字段

类型

说明

id

UUID (PK)

用户主键

username

VARCHAR(50), UNIQUE

用户名

email

VARCHAR(120), UNIQUE

邮箱

hashed_password

VARCHAR(255)

bcrypt 哈希密码

full_name

VARCHAR(100)

姓名

role

ENUM(admin, researcher, user)

角色

is_active

BOOLEAN

是否激活

avatar_url

VARCHAR(500)

头像 URL

#### ResearchTask（研究任务表）

字段

类型

说明

id

UUID (PK)

任务主键

user_id

FK → users

所属用户

title

VARCHAR(300)

任务标题

topic

TEXT

研究主题

description

TEXT

补充说明

status

ENUM(7 种状态)

当前阶段

progress

FLOAT (0.0-1.0)

完成进度

queries

JSON

分解后的搜索查询

search_results

JSON

收集的搜索结果（最多 50 条）

knowledge_gaps

JSON

识别的知识空白（最多 20 条）

summary

TEXT

阶段性综合摘要

final_report

TEXT

最终 Markdown 报告

report_path

VARCHAR(500)

报告文件路径

metadata_json

JSON

元数据（错误信息、模型参数等）

created_at

DATETIME

创建时间

updated_at

DATETIME

更新时间

completed_at

DATETIME

完成时间

**任务状态枚举（TaskStatus）：**

```
待处理 → 主题分解 → 搜索中 → 内容总结 → 报告生成 → 完成
                                                  ↘ 失败 (可取消)
```

#### Article（文章表）

字段

类型

说明

id

UUID (PK)

文章主键

user_id

FK → users

所属用户

title

VARCHAR(300)

文章标题

content

TEXT

Markdown 正文

abstract

TEXT

摘要

keywords

JSON

关键词数组

status

ENUM(draft, published, archived)

发布状态

source_url

VARCHAR(500)

来源 URL

source_type

VARCHAR(50)

来源类型

#### KnowledgeNode（知识节点表）

字段

类型

说明

id

UUID (PK)

节点主键

user_id

FK → users

所属用户

task_id

FK → research_tasks (nullable)

来源任务

title

VARCHAR(300)

节点标题

content

TEXT

节点内容

node_type

VARCHAR(50)

类型 (concept / fact / reference / gap)

confidence

VARCHAR(10)

置信度 (0.0-1.0)

#### UserSettings（用户 API 配置表）

字段

类型

说明

id

UUID (PK)

主键

user_id

FK → users, UNIQUE

所属用户

openai_api_key

TEXT

用户自定义 API Key

openai_base_url

VARCHAR(500)

自定义 Base URL

openai_model

VARCHAR(100)

自定义模型名

---

## 🔬 研究流水线详解

```
用户输入主题
    │
    ▼
┌── Phase 1: 主题分解 (5%) ─────────────────────────────┐
│  DecompositionAgent.decompose()                        │
│  · 输入: topic + description                           │
│  · 输出: sub_questions[], queries[], key_concepts[]    │
│  · LLM: JSON 模式, temperature=0.2                     │
└────────────────────────────────────────────────────────┘
    │
    ▼
┌── Phase 2: 多轮搜索循环 (5%-45%) ─────────────────────┐
│                                                        │
│  For round in 1..3:                                    │
│    ┌─ SearchAgent.search_round() ──────────────────┐  │
│    │  · 遍历所有 queries                             │  │
│    │  · SearchAggregator.search()                   │  │
│    │    ├─ WikipediaSearchTool (多语言 API)          │  │
│    │    ├─ ArxivSearchTool (Atom XML 解析)           │  │
│    │    └─ WebSearchTool (DuckDuckGo HTML)            │  │
│    │  · URL 去重 + 相关性排序                         │  │
│    └────────────────────────────────────────────────┘  │
│    ┌─ SearchAgent.evaluate_completeness() ─────────┐  │
│    │  · 评估信息充分性 (is_sufficient)               │  │
│    │  · 识别知识空白 (knowledge_gaps)                │  │
│    │  · 置信度评分 (confidence 0-1)                  │  │
│    └────────────────────────────────────────────────┘  │
│    ┌─ SummarizationAgent.summarize_round() ────────┐  │
│    │  · 综合本论搜索结果 (最多 30 条)                │  │
│    │  · 输出: round_summary, key_findings,           │  │
│    │          knowledge_nodes, remaining_questions   │  │
│    │  · 保存 IntermediateReport                     │  │
│    └────────────────────────────────────────────────┘  │
│    if is_sufficient or round >= 3: break               │
│                                                        │
└────────────────────────────────────────────────────────┘
    │
    ▼
┌── Phase 3: 最终综合 (75%) ────────────────────────────┐
│  SummarizationAgent.final_summary()                    │
│  · 合并所有轮次的 round_summary    │
│  · 输出 Markdown 格式综合报告                           │
│  · 结构: 概述 / 核心发现 / 不同观点 / 知识空白 / 参考文献  │
└────────────────────────────────────────────────────────┘
    │
    ▼
┌── Phase 4: 待办规划 (75%-85%) ────────────────────────┐
│  TodoPlannerAgent.generate_plan_with_evaluation()      │
│  ┌─ generate_plan() ──────────────────────────────┐   │
│  │  · 生成分阶段研究计划 (phases → todos)           │   │
│  └────────────────────────────────────────────────┘   │
│  ┌─ evaluate_plan() ─────────────────────────────┐   │
│  │  · 四维评估: 主题相关性/需求覆盖/结构完整/逻辑连贯  │   │
│  │  · 评分 1-10，≥7 分视为合格                     │   │
│  └────────────────────────────────────────────────┘   │
│  ┌─ if not matching: regenerate(feedback) ───────┐   │
│  │  · 最多重试 2 次                                 │   │
│  └────────────────────────────────────────────────┘   │
│  · 持久化 TodoItems (关联 task_id)                    │
└────────────────────────────────────────────────────────┘
    │
    ▼
┌── Phase 5: 报告生成 (85%-92%) ────────────────────────┐
│  ReportAgent.generate_report()                         │
│  · 输入: topic + summary + search_results +             │
│           knowledge_nodes + todo_plan                  │
│  · 输出完整 Markdown 学术报告                           │
│  · 结构: 摘要 → 引言 → 文献综述 → 分析 →                │
│           研究发现 → 研究规划 → 结论 → 参考文献          │
│  · temperature=0.4（稍高以获得更流畅的文风）            │
└────────────────────────────────────────────────────────┘
    │
    ▼
┌── Phase 6: 图像增强 (92%) ────────────────────────────┐
│  ImageAgent (非关键路径，失败不影响报告)                 │
│  ┌─ identify_image_placements() ──────────────────┐   │
│  │  · 分析源材料中是否包含图表/图像引用               │   │
│  │  · 仅在源材料有图片时才建议插入位置                 │   │
│  │  · 输出: placements[] (0-4 个)                   │   │
│  └────────────────────────────────────────────────┘   │
│  ┌─ fetch_images_for_placements() ────────────────┐   │
│  │  · Wikimedia Commons API 检索 CC 许可图片        │   │
│  │  · 未找到则跳过（不使用占位图）                    │   │
│  └────────────────────────────────────────────────┘   │
│  ┌─ embed_images_in_report() ─────────────────────┐   │
│  │  · 按 section_title 定位插入点                   │   │
│  │  · 生成 Markdown 图片语法 + 学术图注              │   │
│  └────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
    │
    ▼
  完成 (100%)
```

---

## 🤖 AI Agent 体系

### Agent 矩阵

#

Agent

职责

输入

输出

LLM 模式

Temperature

1

**DecompositionAgent**

主题分解为子问题与搜索查询

研究主题 + 描述

JSON: sub_questions → queries[] + key_concepts[]

JSON

0.2

2

**SearchAgent**

跨源搜索 + 信息充分性评估

查询列表 + 已有结果

搜索结果 + 知识空白评估

JSON (评估)

0.2

3

**SummarizationAgent**

搜索结果综合与知识节点提取

本论结果 + 所有轮次

逐轮摘要 + 最终综合报告

JSON + Text

0.2 / 0.3

4

**TodoPlannerAgent**

生成 + 自评估研究待办计划

主题 + 摘要 + 知识空白

分阶段 TODO 计划

JSON

0.2

5

**ReportAgent**

结构化 Markdown 学术报告

主题 + 摘要 + 来源 + 节点

Markdown 报告

Text

0.4

6

**ImageAgent**

源材料图片分析 + CC 图片检索嵌入

报告 + 源材料

图片位置 + Markdown 嵌入

JSON

0.2

### Prompts 设计

每个 Agent 的 System Prompt 包含：

1.  **角色定义**：明确 Agent 的专家身份（如 "expert research planner"）
2.  **任务指令**：具体要完成的操作步骤
3.  **语言跟随**：要求输出语言与输入语言一致（中文输入 → 中文输出）
4.  **格式约束**：JSON 模式下的格式要求（无 markdown 包裹、引号转义、禁止尾随逗号）
5.  **输出结构**：期望的 JSON schema 或 Markdown 结构

### LangChain 集成方式

-   **Prompt 模板**：使用 `ChatPromptTemplate.from_messages()` 构建结构化提示词
-   **ChatOpenAI**：作为 LLM 后端，支持 temperature、max_tokens、timeout 参数
-   **JSON 模式**：通过 `model_kwargs={"response_format": {"type": "json_object"}}` 启用原生 JSON 输出
-   **工具定义**：`langchain_tools.py` 中定义了 `@tool` 装饰的标准搜索工具（可供未来 Agent 工具调用扩展）

---

## 🎨 前端设计

### 设计系统 (Design Tokens)

前端完全通过 CSS 自定义属性驱动，实现了零 JS 开销的主题切换：

```
核心 Token 分组:
├── 颜色 (bg, surface, border, text, accent, success, warn, danger)
├── 圆角 (sm: 6px, base: 10px, lg: 14px, xl: 18px)
├── 阴影 (sm, base, lg, glow)
├── 过渡 (fast: 150ms, base: 250ms, smooth: 350ms)
└── 渐变 (subtle, hero)
```

### 五种主题

主题

主色调

风格

Dark Blue (默认)

`#5b7cf8` 蓝色

科技感深色

Light

`#4f6ef7` 蓝色

清爽亮色

Emerald

`#10b981` 翠绿

护眼自然

Sunset

`#f59e0b` 琥珀

温暖活力

Purple

`#a78bfa` 紫色

优雅神秘

### 前端技术特点

-   **零框架依赖**：纯 TypeScript + CSS 构建，无 React/Vue 依赖
-   **SPA 路由**：基于 `showPage()` + `innerHTML` 的客户端路由
-   **Markdown 渲染**：自研 `parseMarkdown()` 函数，支持标题、列表、表格、代码块、引用、图片、链接等完整语法
-   **状态持久化**：`localStorage` 存储 token、user、theme、lang、currentPage
-   **响应式设计**：900px 断点，移动端侧边栏转为顶部导航
-   **骨架屏**：CSS 动画骨架屏（`.skeleton`），减少加载感知延迟
-   **Toast 通知**：支持 success/error/info 三种类型，自动消失 + 滑入动画
-   **模态对话框**：高斯模糊背景遮罩，缩放动画入场

### i18n 架构

```typescript
const I18N = {
    zh: { "app.title": "Deep Research", "auth.signIn": "登录", ... },
    en: { "app.title": "Deep Research", "auth.signIn": "Sign In", ... },
}

// 运行时翻译
function t(key: string, params?: Record<string, string>): string

// 语言切换
function setLanguage(lang: "zh" | "en"): void
    → 更新 document.documentElement.lang
    → applyI18nToDOM(): 遍历 [data-i18n] 和 [data-i18n-placeholder]
    → 重新渲染当前页面
```

### 前端状态管理

```
global state:
  token: string          ← localStorage("token")
  user: User | null      ← localStorage("user")
  currentPage: string    ← localStorage("currentPage")
  currentLang: "zh"|"en" ← localStorage("lang")
  currentTheme: string   ← localStorage("theme")

flow:
  DOMContentLoaded → auth check → showApp() or authPage
  showPage(page) → render*Page(container)
  api(path, opts) → fetch with Authorization header → 401 → doLogout()
```

---

## 🚀 快速开始

### 环境要求

-   **Python** ≥ 3.11
-   **Node.js** ≥ 18（前端开发可选）
-   **OpenAI 兼容 API Key**（支持 OpenAI、DeepSeek 及任何兼容服务商）

### 1. 克隆项目

```bash
git clone <your-repo-url>
cd lanshan-project
```

### 2. 后端安装

#### Windows

```powershell
cd backend
python -m venv venv

# CMD:
venvScriptsactivate
# PowerShell:
.venvScriptsActivate.ps1
# Git Bash:
source venv/Scripts/activate

pip install -r requirements.txt

# 创建 .env 文件：
@"
APP_NAME=Deep Research Agent System
DEBUG=true
DATABASE_URL=sqlite+aiosqlite:///./research.db
JWT_SECRET_KEY=change-me-to-a-random-string
OPENAI_API_KEY=sk-your-api-key
OPENAI_BASE_URL=https://api.deepseek.com
OPENAI_MODEL=deepseek-chat
"@ | Out-File -FilePath .env -Encoding utf8

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Linux / macOS

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cat > .env << EOF
APP_NAME=Deep Research Agent System
DEBUG=true
DATABASE_URL=sqlite+aiosqlite:///./research.db
JWT_SECRET_KEY=change-me-to-a-random-string
OPENAI_API_KEY=sk-your-api-key
OPENAI_BASE_URL=https://api.deepseek.com
OPENAI_MODEL=deepseek-chat
EOF

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

启动后访问 [http://localhost:8000/docs](http://localhost:8000/docs) 查看 Swagger API 文档。

### 3. 前端运行

```bash
cd frontend
npm install
npm run dev    # 编译 TypeScript + 启动开发服务器 (端口 3000)
```

或直接用浏览器打开 `frontend/index.html`（需先编译 TypeScript：`npm run build`）。

> **注意：** 前端默认连接 `http://localhost:8000/api`。如需修改，编辑 `frontend/app.js` 中的 `API` 常量。

### 4. 开始使用

1.  打开浏览器访问 `http://localhost:3000`
2.  注册账号并登录
3.  （可选）进入 Settings 页面配置自己的 API Key
4.  在仪表盘输入研究主题，例如：「量子计算在人工智能中的应用现状」
5.  系统自动分析意图并启动研究任务
6.  在任务列表页查看进度，完成后点击查看完整报告

---

## ⚙️ 配置指南

### 环境变量参考

变量

默认值

说明

`APP_NAME`

Deep Research Agent System

应用名称

`APP_VERSION`

1.0.0

版本号

`DEBUG`

true

调试模式（开启 SQL 日志）

`DATABASE_URL`

sqlite+aiosqlite:///./research.db

数据库连接 URL

`JWT_SECRET_KEY`

(需修改)

JWT 签名密钥（生产环境务必修改）

`JWT_ALGORITHM`

HS256

JWT 签名算法

`JWT_EXPIRE_MINUTES`

1440 (24h)

Token 有效期

`OPENAI_API_KEY`

(必填)

LLM API 密钥

`OPENAI_BASE_URL`

[https://api.deepseek.com](https://api.deepseek.com)

API 基础 URL

`OPENAI_MODEL`

deepseek-v4-flash

模型名称

`WIKIPEDIA_LANG`

zh

Wikipedia 搜索语言

`ARXIV_MAX_RESULTS`

20

arXiv 最大返回结果数

`CORS_ORIGINS`

["*"]

允许的跨域来源

`UPLOAD_DIR`

./uploads

上传文件目录

`REPORT_DIR`

./reports

报告存储目录

### 支持的大模型服务商

服务商

Base URL

推荐模型

DeepSeek

`https://api.deepseek.com`

`deepseek-chat` / `deepseek-v4-flash`

OpenAI

`https://api.openai.com/v1`

`gpt-4o` / `gpt-4o-mini`

硅基流动

`https://api.siliconflow.cn/v1`

`deepseek-ai/DeepSeek-V3`

阿里百炼

`https://dashscope.aliyuncs.com/compatible-mode/v1`

`qwen-plus`

其他兼容服务

自定义

按服务商文档填写

---

## 📡 API 文档

### 认证接口

方法

路径

认证

说明

POST

`/api/auth/register`

❌

用户注册

POST

`/api/auth/login`

❌

用户登录（返回 JWT）

### 用户接口

方法

路径

认证

说明

GET

`/api/users/me`

✅

获取当前用户信息

PUT

`/api/users/me`

✅

更新当前用户信息

### 研究任务接口

方法

路径

认证

说明

POST

`/api/research/`

✅

创建研究任务

GET

`/api/research/`

✅

获取任务列表（支持 `skip`, `limit`）

GET

`/api/research/{id}`

✅

获取任务详情（含中间报告、待办事项）

POST

`/api/research/{id}/run`

✅

启动研究（后台异步执行）

POST

`/api/research/{id}/cancel`

✅

取消正在运行的研究

DELETE

`/api/research/{id}`

✅

删除研究任务

PUT

`/api/research/{id}/todos/{todo_id}`

✅

更新待办完成状态

### 文章接口

方法

路径

认证

说明

POST

`/api/articles/`

✅

创建文章

GET

`/api/articles/`

✅

获取文章列表

GET

`/api/articles/{id}`

✅

获取文章详情

PUT

`/api/articles/{id}`

✅

更新文章

DELETE

`/api/articles/{id}`

✅

删除文章

GET

`/api/articles/knowledge-nodes`

✅

获取知识节点列表

POST

`/api/articles/knowledge-nodes`

✅

创建知识节点

### AI 接口

方法

路径

认证

说明

POST

`/api/ai/parse-input`

✅

自然语言意图解析

**请求示例：**

```json
{
  "text": "量子计算在人工智能中的应用现状"
}
```

**响应示例：**

```json
{
  "action": "research",
  "payload": {
    "title": "量子计算在人工智能中的应用现状",
    "topic": "调研量子计算技术在人工智能领域的当前应用情况，包括量子机器学习、量子神经网络等方向的最新进展",
    "description": ""
  },
  "explanation": "正在创建关于量子计算与AI交叉领域的研究任务"
}
```

### 设置接口

方法

路径

认证

说明

GET

`/api/settings`

✅

获取用户 API 配置

PUT

`/api/settings`

✅

更新用户 API 配置

POST

`/api/settings/test`

✅

测试 API 连接

### 健康检查

方法

路径

认证

说明

GET

`/api/health`

❌

服务健康检查

---

## 🎯 使用场景

### 场景一：快速文献综述

**输入：** "帮我调研 Transformer 架构在计算机视觉领域的最新进展"

**系统行为：**

1.  分解为 5-7 个子问题（如 "Vision Transformer 架构演进"、"ViT vs CNN 性能对比"、"自监督 ViT 预训练方法"）
2.  从 arXiv 拉取相关论文，Wikipedia 补充背景知识，Web 搜索最新博客和新闻
3.  3 轮迭代后生成包含 30+ 引用来源的结构化综述

### 场景二：技术调研报告

**输入：** "研究一下 Rust 语言在嵌入式系统开发中的应用和优势"

**系统行为：**

1.  拆解为 "Rust 嵌入式生态现状"、"与 C/C++ 的内存安全对比"、"RTOS 支持情况" 等子方向
2.  多渠道搜索并自动生成学术格式的调研报告
3.  附带研究待办（如 "深入调研 Embassy 框架"、"阅读 Rust Embedded Book"）

### 场景三：跨领域探索

**输入：** "探索区块链技术在医疗数据隐私保护中的潜力"

**系统行为：**

1.  自动识别跨领域特性，从 "区块链基础" 和 "医疗数据隐私" 两个维度拆解
2.  知识空白识别后补充 "HIPAA 合规" 和 "零知识证明" 等方向
3.  生成包含两种技术融合路径分析的综合报告

---

## 📁 项目结构

```
lanshan-project/
├── backend/
│   ├── .env                        # 环境变量配置（不入版本控制）
│   ├── requirements.txt            # Python 依赖清单
│   ├── __init__.py
│   └── app/
│       ├── __init__.py
│       ├── main.py                 # FastAPI 应用入口 + 生命周期管理
│       ├── config.py               # Pydantic Settings 配置管理
│       ├── database.py             # SQLAlchemy 异步引擎 + 会话工厂
│       │
│       ├── api/                    # 🔌 API 路由层
│       │   ├── __init__.py
│       │   ├── auth.py             # POST /auth/register, /auth/login
│       │   ├── users.py            # GET/PUT /users/me
│       │   ├── research.py         # CRUD + run + cancel 研究任务
│       │   ├── articles.py         # CRUD 文章 + 知识节点
│       │   ├── ai.py               # POST /ai/parse-input 自然语言解析
│       │   └── settings.py         # GET/PUT/POST /settings + 连接测试
│       │
│       ├── models/                 # 🗃️ 数据库模型 (SQLAlchemy ORM)
│       │   ├── __init__.py
│       │   ├── user.py             # 用户 + 角色枚举
│       │   ├── research_task.py    # 研究任务 + 状态枚举
│       │   ├── article.py          # 文章 + 知识节点 + 待办 + 中间报告
│       │   └── user_settings.py    # 用户 API 配置
│       │
│       ├── schemas/                # 📋 Pydantic 请求/响应模型
│       │   ├── __init__.py
│       │   ├── user.py             # UserCreate, UserResponse, ...
│       │   ├── research.py         # ResearchTaskCreate, ResearchTaskResponse, ...
│       │   ├── article.py          # ArticleCreate, ArticleResponse, ...
│       │   └── settings.py         # UserSettingsUpdate, UserSettingsResponse, ...
│       │
│       ├── services/               # 🧠 业务逻辑层
│       │   ├── __init__.py
│       │   ├── auth_service.py     # 注册/登录逻辑
│       │   ├── research_service.py # 研究任务 CRUD + 执行
│       │   ├── article_service.py  # 文章 CRUD
│       │   ├── settings_service.py # 用户配置 CRUD + 连接测试
│       │   └── ai_service.py       # 自然语言意图解析
│       │
│       ├── agents/                 # 🤖 AI Agent 层
│       │   ├── __init__.py
│       │   ├── base.py             # BaseAgent（LLM 调用 + JSON 修复 + 重试）
│       │   ├── decomposition_agent.py  # Agent 1: 主题分解
│       │   ├── search_agent.py         # Agent 2: 多轮搜索 + 完整性评估
│       │   ├── summarization_agent.py  # Agent 3: 内容总结 + 知识节点提取
│       │   ├── report_agent.py         # Agent 4: Markdown 报告生成
│       │   ├── todo_planner_agent.py   # Agent 5: 待办规划 + 自评估
│       │   ├── image_agent.py          # Agent 6: 图像增强（源材料分析 + CC 图片检索）
│       │   └── orchestrator.py         # 研究流程编排器（6 阶段流水线）
│       │
│       ├── tools/                  # 🔍 搜索工具层
│       │   ├── __init__.py         # SearchAggregator 统一搜索聚合
│       │   ├── wikipedia_search.py # Wikipedia API（多语言）
│       │   ├── arxiv_search.py     # arXiv API（Atom XML）
│       │   ├── web_search.py       # DuckDuckGo HTML 搜索 + 网页抓取
│       │   ├── image_search.py     # Wikimedia Commons CC 图片搜索
│       │   └── langchain_tools.py  # LangChain @tool 封装
│       │
│       └── core/                   # 🔐 安全模块
│           ├── __init__.py
│           └── security.py         # JWT 生成/验证 + bcrypt 密码哈希 + 认证依赖
│
├── frontend/
│   ├── package.json                # Node.js 依赖（仅 TypeScript + serve）
│   ├── tsconfig.json               # TypeScript 编译配置
│   ├── index.html                  # 单页应用入口 + 完整 CSS 设计系统
│   ├── app.js                      # 编译后的 JavaScript（SPA 主逻辑）
│   ├── app.js.map                  # Source Map
│   └── node_modules/               # 开发依赖
│
├── .claude/                        # Claude Code 配置
├── .gitignore
└── README.md                       # 本文档
```

---

## 🗺️ 开发路线图

### 已完成 ✅

-    多 Agent 流水线协作（6 Agent）
-    多源搜索聚合（Wikipedia + arXiv + DuckDuckGo）
-    多轮迭代研究（自适应终止）
-    JWT 多用户认证 + 角色管理
-    用户级 API 配置（三级回退链）
-    结构化 Markdown 报告生成
-    自然语言意图解析
-    知识节点提取与图谱展示
-    报告图像智能增强（CC 许可图片）
-    待办计划自评估与修正
-    五主题设计系统
-    中英文国际化
-    鲁棒 JSON 处理（三层容错）
-    任务取消机制
-    Swagger API 自动文档
-    响应式前端布局

### 规划中 🔮

-    **流式输出 (SSE)**：研究进度实时推送，替代前端轮询
-    **LangGraph 状态图**：将线性流水线升级为状态图驱动的 Agent 工作流
-    **Agent 工具调用**：让 SearchAgent 自主决策调用哪个搜索源
-    **PDF 报告导出**：Markdown → PDF 转换（LaTeX 模板）
-    **引用管理**：BibTeX 格式引用导出
-    **协作研究**：多人协同编辑研究任务
-    **研究历史对比**：不同时间点研究结果的 diff 视图
-    **自定义 Agent 模板**：用户可配置 Agent 的 System Prompt
-    **搜索结果缓存**：减少重复 API 调用，加速重复研究
-    **Docker 一键部署**：`docker-compose up` 即可启动
-    **PostgreSQL 支持**：生产环境数据库切换
-    **前端框架迁移**：考虑 React/Vue 重写以支持更复杂的交互

---

## 📄 许可证

MIT License

---

> Built with ❤️ using FastAPI, LangChain, and TypeScript