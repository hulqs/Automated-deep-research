# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Deep Research Agent System** — AI-driven academic research agent system. Users input a research topic, and the system automatically decomposes it, searches multiple sources (Wikipedia, arXiv, DuckDuckGo), iteratively summarizes, and generates a structured Markdown academic report.

## Commands

### Backend
```bash
cd backend

# Setup
python -m venv venv && source venv/Scripts/activate  # Git Bash (Windows)
pip install -r requirements.txt

# Run dev server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# API docs at http://localhost:8000/docs
```

### Frontend
```bash
cd frontend
npm install
npm run build    # Compile TypeScript (tsc)
npm run serve    # Static server on port 3000
npm run dev      # Build + serve (one step)
npm run watch    # tsc --watch for dev iteration
```

### Environment
- Copy `.env.example` patterns from `backend/.env` (create from `backend/app/config.py` defaults)
- Required: `OPENAI_API_KEY` (OpenAI-compatible API key — DeepSeek, OpenAI, etc.)
- Run `backend/research.db` is auto-created on first startup

## Architecture

### Layered Architecture (Backend)

```
FastAPI app (main.py)
  → API Routes (api/*.py) — JWT auth via Depends(get_current_user)
    → Services (services/*.py) — business logic
      → Agents (agents/*.py) — AI agent pipeline
        → Tools (tools/*.py) — search layer
```

### AI Agent Pipeline (6 phases, sequenced by `ResearchOrchestrator`)

| Phase | Agent | Purpose |
|-------|-------|---------|
| 1 | `DecompositionAgent` | Decompose topic into sub-questions and search queries |
| 2 | `SearchAgent` | Multi-round search (up to 3 rounds) across Wikipedia/arXiv/Web |
| 3 | `SummarizationAgent` | Round-by-round + final comprehensive summary with knowledge nodes |
| 4 | `TodoPlannerAgent` | Generate self-evaluated research TODO plan (retry if <7/10 score) |
| 5 | `ReportAgent` | Generate structured Markdown academic report |
| 6 | `ImageAgent` | Analyze source images, fetch CC-licensed images from Wikimedia Commons |

- All agents extend `BaseAgent` which provides `call_llm()` (text, 4000 tokens) and `call_llm_json()` (JSON mode, 8192 tokens, with auto-repair via `json-repair` library)
- Configuration fallback chain: **DB user_settings → .env → hardcoded defaults**
- Task cancellation: checkpoints at each phase query DB status

### Search Tools (`backend/app/tools/`)

- `SearchAggregator.search(query, sources)` — unified entry: parallel/sequential searches, URL dedup, relevance sorting
- Sources: Wikipedia API (multi-language), arXiv API (Atom XML), DuckDuckGo HTML scrape, Wikimedia Commons API
- `langchain_tools.py` wraps tools with `@tool` decorator for future LangChain agent use

### Data Models (`backend/app/models/`)

- **User** — UUID PK, username, email, bcrypt password, role (admin/researcher/user)
- **ResearchTask** — UUID PK, FK→user, topic, status (7 states enum), progress (0-1), queries/results/gaps (JSON), final_report (Markdown TEXT), metadata_json
- **Article + KnowledgeNode** — user-scoped articles and knowledge graph nodes
- **UserSettings** — per-user LLM API config (API key, base URL, model)
- **TodoItem + IntermediateReport** — child entities of ResearchTask

### Auth (`backend/app/core/security.py`)

- JWT with HS256, 24h expiry; `get_current_user` FastAPI dependency via `HTTPBearer`
- bcrypt password hashing

### Frontend (`frontend/`)

- **Zero-framework TypeScript SPA** — vanilla TypeScript compiled to `app.js`
- Client-side routing via `showPage()` + `innerHTML`
- Custom Markdown renderer (`parseMarkdown()`)
- **Design System**: CSS custom properties (tokens for colors, shadows, radii, transitions) with 5 themes (Dark Blue, Light, Emerald, Sunset, Purple)
- **i18n**: Built-in Chinese/English with 200+ translation keys, runtime switching via `t()` function and `data-i18n` attributes
- State persisted in `localStorage` (token, user, theme, lang, currentPage)

### Database

- SQLite via `aiosqlite` (async), SQLAlchemy 2.0 ORM
- Auto-creates tables on startup (`Base.metadata.create_all`)
- `check_same_thread=False` for async multi-thread access

## Key Design Patterns

- **Dependency Injection**: FastAPI `Depends()` for db sessions and auth user
- **Configuration**: `pydantic-settings` with `lru_cache` singleton; `.env` loaded both into `os.environ` (for openai SDK) and pydantic model
- **JSON Robustness**: 3-layer LLM JSON parsing: standard → `json-repair` → RuntimeError
- **Retry**: `tenacity` decorator on `call_llm_json()` (max 2 attempts, exponential backoff 2-10s)
- **Orchestrator**: Runs research in background (not a background task — called from service layer directly)
