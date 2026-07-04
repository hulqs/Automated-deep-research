# Deep Research Agent System

> AI 驱动的学术研究代理系统 —— 输入一个研究主题，自动完成主题分解、多源搜索、内容总结和报告生成。

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688.svg)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3+-green.svg)](https://www.langchain.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red.svg)](https://www.sqlalchemy.org/)

---

## 📖 项目介绍

**Deep Research Agent System** 是一个基于多智能体协作的深度研究系统。用户只需输入一个研究主题，系统便会自动调度多个 AI Agent 协同工作：将主题拆解为可搜索的子问题，从 Wikipedia、arXiv 及互联网等多个数据源搜集信息，经过多轮迭代搜索与总结，最终生成一份结构完整的学术研究报告。

项目采用 **FastAPI** 构建后端 API，**TypeScript** 编写前端单页应用，数据库使用 **SQLite**（异步驱动），AI 能力基于 **LangChain** 框架接入 OpenAI 兼容接口（支持 OpenAI、DeepSeek 等）。

**主要应用场景：**

- 学术文献综述的快速生成
- 技术调研与知识梳理
- 跨领域研究主题的探索
- 结构化写作辅助

---

## 🎨 项目效果

### 仪表盘

仪表盘提供研究任务概览统计（总任务数、已完成、进行中），支持自然语言快速输入——直接描述你想研究或写作的主题，系统会自动判断是创建研究任务还是文章。

### 研究流程

1. **主题分解** —— 将宽泛的研究主题拆分为 3-7 个聚焦的子问题和具体搜索查询
2. **多轮搜索** —— 从 Wikipedia、arXiv、Web 多源搜集信息，最多 3 轮迭代，每轮评估知识完整性
3. **内容总结** —— 每轮搜索结果即时总结，提取关键发现和知识节点
4. **报告生成** —— 生成包含摘要、引言、文献综述、核心分析、研究发现、结论和参考文献的完整学术报告
5. **待办规划** —— 自动生成分阶段的研究待办计划

### 知识图谱

研究过程中提取的知识节点（概念、事实、参考文献、知识空白）自动汇聚为知识图谱，支持按置信度筛选。

---

## ✨ 项目特点

- **🤖 多 Agent 协作**：5 个专职 AI Agent（主题分解、搜索、总结、报告生成、待办规划）流水线协作，各司其职
- **🔍 多源搜索**：内置 Wikipedia、arXiv 和通用网页搜索（DuckDuckGo），结果自动聚合去重
- **🔄 多轮迭代**：最多 3 轮搜索-评估-总结循环，自动识别知识空白并补充搜索
- **📝 自然语言交互**：前端支持自然语言输入，AI 自动判断意图——直接说"写一篇关于XX的文章"或"研究一下XX"即可
- **🔐 多用户系统**：JWT 认证，支持管理员、研究者、普通用户三种角色
- **⚙️ 个性化配置**：每个用户可独立配置自己的 API Key、Base URL 和模型，支持 DeepSeek 等兼容服务
- **📊 结构化输出**：研究报告包含摘要、引言、文献综述、分析、发现、结论和参考文献的完整学术结构
- **🗂️ 知识管理**：研究过程中自动提取知识节点，构建个人知识库

---

## 🏗️ 项目架构

```
┌─────────────────────────────────────────────────┐
│                   Frontend (TS)                   │
│         仪表盘 │ 研究任务 │ 文章 │ 知识图谱        │
└─────────────────────┬───────────────────────────┘
                      │ REST API (JWT Auth)
┌─────────────────────▼───────────────────────────┐
│                 FastAPI Backend                   │
│  ┌──────────┬──────────┬──────────┬──────────┐  │
│  │  /auth   │ /users   │/research │/articles │  │
│  │ 注册/登录 │ 用户管理  │ 研究任务  │ 文章管理  │  │
│  ├──────────┼──────────┼──────────┼──────────┤  │
│  │  /ai     │/settings │          │          │  │
│  │ 自然语言  │ API配置   │          │          │  │
│  └──────────┴──────────┴──────────┴──────────┘  │
│                      │                           │
│  ┌───────────────────▼────────────────────────┐  │
│  │         Research Orchestrator              │  │
│  │   ┌─────────────┐  ┌───────────────────┐   │  │
│  │   │ Decomposer  │  │   SearchAgent     │   │  │
│  │   │ (主题分解)   │  │ (多源搜索+评估)    │   │  │
│  │   └─────────────┘  └───────────────────┘   │  │
│  │   ┌─────────────┐  ┌───────────────────┐   │  │
│  │   │ Summarizer  │  │   ReportAgent     │   │  │
│  │   │ (内容总结)   │  │ (报告生成)         │   │  │
│  │   └─────────────┘  └───────────────────┘   │  │
│  │   ┌─────────────┐                          │  │
│  │   │TodoPlanner  │                          │  │
│  │   │ (待办规划)   │                          │  │
│  │   └─────────────┘                          │  │
│  └────────────────────────────────────────────┘  │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│                 Data Layer                       │
│  ┌──────────┬──────────┬────────────────────┐   │
│  │ SQLite   │ Wikipedia│  arXiv API         │   │
│  │(async)   │   API    │  Web Search        │   │
│  └──────────┴──────────┴────────────────────┘   │
└─────────────────────────────────────────────────┘
```

### 目录结构

```
lanshan-project/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI 应用入口
│   │   ├── config.py            # 配置管理（Pydantic Settings）
│   │   ├── database.py          # 数据库引擎与会话
│   │   ├── api/                 # API 路由层
│   │   │   ├── auth.py          # 认证接口
│   │   │   ├── users.py         # 用户管理接口
│   │   │   ├── research.py      # 研究任务接口
│   │   │   ├── articles.py      # 文章与知识节点接口
│   │   │   ├── ai.py            # AI 自然语言解析接口
│   │   │   └── settings.py      # 用户设置接口
│   │   ├── models/              # 数据库模型
│   │   │   ├── user.py          # 用户与角色
│   │   │   ├── research_task.py # 研究任务
│   │   │   ├── article.py       # 文章、知识节点、待办、中间报告
│   │   │   └── user_settings.py # 用户 API 配置
│   │   ├── schemas/             # Pydantic 请求/响应模型
│   │   ├── services/            # 业务逻辑层
│   │   ├── agents/              # AI Agent 层
│   │   │   ├── base.py              # Agent 基类（LangChain + JSON 修复）
│   │   │   ├── decomposition_agent.py # 主题分解 Agent
│   │   │   ├── search_agent.py       # 搜索协调 Agent
│   │   │   ├── summarization_agent.py # 内容总结 Agent
│   │   │   ├── report_agent.py       # 报告生成 Agent
│   │   │   ├── todo_planner_agent.py # 待办规划 Agent
│   │   │   └── orchestrator.py       # 研究流程编排器
│   │   ├── tools/               # 搜索工具
│   │   │   ├── web_search.py        # 通用网页搜索（DuckDuckGo）
│   │   │   ├── wikipedia_search.py  # Wikipedia API
│   │   │   └── arxiv_search.py      # arXiv API
│   │   └── core/                # 安全模块（JWT、密码哈希）
│   └── requirements.txt
└── frontend/
    └── src/
        ├── app.ts               # 单页应用主逻辑
        └── types.ts             # TypeScript 类型定义
```

### 研究流水线

```
用户输入主题
    │
    ▼
[Phase 1] DecompositionAgent ← 将主题拆解为子问题 + 搜索查询
    │
    ▼
┌── [Phase 2] 多轮搜索循环（最多 3 轮）──┐
│                                          │
│  SearchAgent.search_round()              │
│    ├─ Wikipedia API                      │
│    ├─ arXiv API                          │
│    └─ DuckDuckGo Web Search              │
│         │                                │
│         ▼                                │
│  SearchAgent.evaluate_completeness()     │
│    ├─ 信息是否充足？                      │
│    ├─ 识别知识空白                        │
│    └─ 建议补充搜索方向                    │
│         │                                │
│         ▼                                │
│  SummarizationAgent.summarize_round()    │
│    └─ 生成本轮总结 + 知识节点             │
│         │                                │
│         └── 信息不足 → 继续下一轮 ──────┘│
│                                          │
└──────────── 信息充足 / 达到上限 ──────────┘
    │
    ▼
[Phase 3] SummarizationAgent.final_summary() → 综合所有轮次的最终摘要
    │
    ▼
[Phase 4] TodoPlannerAgent → 生成分阶段研究待办计划
    │
    ▼
[Phase 5] ReportAgent → 生成完整 Markdown 学术报告
```

### 五大 AI Agent

| Agent | 职责 |
|-------|------|
| **Decomposition Agent** | 将研究主题拆解为聚焦的子问题和可执行的搜索查询 |
| **Search Agent** | 跨 Wikipedia、arXiv、Web 多轮搜索，评估信息完整性 |
| **Summarization Agent** | 综合搜索结果，构建知识节点，识别知识空白 |
| **Report Agent** | 生成带引用的结构化 Markdown 学术报告 |
| **TODO Planner Agent** | 创建分阶段的学术研究待办计划 |

---

## 🔧 集成方式

### 环境要求

- **Python** >= 3.11
- **Node.js** >= 18（前端开发可选）
- **OpenAI 兼容 API Key**（支持 OpenAI、DeepSeek 等）

### 后端安装

```bash
# 1. 克隆项目
git clone <your-repo-url>
cd lanshan-project/backend

# 2. 创建虚拟环境
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 配置环境变量
cat > .env << EOF
APP_NAME=Deep Research Agent System
DEBUG=true
DATABASE_URL=sqlite+aiosqlite:///./research.db
JWT_SECRET_KEY=your-secret-key-change-me
OPENAI_API_KEY=your-api-key
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-4o
EOF

# 5. 启动后端服务
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

启动后访问 http://localhost:8000/docs 查看 Swagger API 文档。

### 前端运行

```bash
# 1. 进入前端目录
cd frontend

# 2. 安装依赖（如需要）
npm install

# 3. 编译 TypeScript
npx tsc

# 4. 直接用浏览器打开 index.html，
#    或使用任意静态文件服务器：
npx serve .
```

> **注意：** 前端默认连接 `http://localhost:8000/api`，如需修改后端地址，编辑 `frontend/src/app.ts` 中的 `API` 常量。

---

## 📘 使用方法

### 1. 注册与登录

打开前端页面，创建账号并登录。系统支持三种角色：

| 角色 | 权限 |
|------|------|
| **管理员 (admin)** | 全部权限 |
| **研究者 (researcher)** | 创建研究任务、管理文章 |
| **普通用户 (user)** | 基础使用 |

### 2. 配置 API（可选）

进入 **Settings** 页面，配置你的 API Key、Base URL 和模型名称。如果不配置，系统将使用服务器默认设置。

> 💡 推荐使用 DeepSeek API：Base URL 填 `https://api.deepseek.com`，Model 填 `deepseek-chat`。

### 3. 快速开始（自然语言）

在仪表盘的输入框中直接描述你想做什么：

- **创建研究任务：** `量子计算在人工智能中的应用现状`
- **写文章：** `写一篇关于气候变化对农业影响的综述文章`

系统会自动判断意图并执行相应操作。

### 4. 创建研究任务

点击 **"+ 新建研究"**，填写：
- **标题**：如 "量子计算综述"
- **研究主题**：详细描述你想研究的内容
- **备注**：可选补充说明

创建后任务在后台异步执行，你可以在任务列表页查看进度。研究流程包括：

1. **主题分解** → 2. **多轮搜索** → 3. **内容总结** → 4. **生成报告** → 5. **待办规划**

完成后点击任务即可查看完整的学术研究报告（Markdown 格式），包含摘要、引言、文献综述、分析、发现、结论和参考文献。

### 5. 管理文章

在 **Articles** 页面可以手动创建、编辑和删除文章，支持 Markdown 内容、摘要、关键词标签。

### 6. 查看知识图谱

在 **Knowledge Graph** 页面查看研究过程中提取的知识节点，包括概念、事实、参考文献等，按置信度排序。

### API 接口概览

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/auth/register` | 用户注册 |
| POST | `/api/auth/login` | 用户登录 |
| GET | `/api/users/me` | 获取当前用户信息 |
| PUT | `/api/users/me` | 更新当前用户信息 |
| POST | `/api/research/` | 创建研究任务 |
| GET | `/api/research/` | 获取任务列表 |
| GET | `/api/research/{id}` | 获取任务详情 |
| POST | `/api/research/{id}/run` | 启动研究任务 |
| DELETE | `/api/research/{id}` | 删除研究任务 |
| PUT | `/api/research/{id}/todos/{todo_id}` | 更新待办状态 |
| POST | `/api/articles/` | 创建文章 |
| GET | `/api/articles/` | 获取文章列表 |
| GET | `/api/articles/{id}` | 获取文章详情 |
| PUT | `/api/articles/{id}` | 更新文章 |
| DELETE | `/api/articles/{id}` | 删除文章 |
| POST | `/api/articles/knowledge-nodes` | 创建知识节点 |
| GET | `/api/articles/knowledge-nodes` | 获取知识节点列表 |
| POST | `/api/ai/parse-input` | 自然语言意图解析 |
| GET | `/api/settings` | 获取用户 API 设置 |
| PUT | `/api/settings` | 更新用户 API 设置 |
| GET | `/api/health` | 健康检查 |
