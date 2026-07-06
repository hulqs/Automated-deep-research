# Deep Research Agent Skill

## Description
Complete academic research pipeline with multi-agent orchestration. Decomposes research topics, searches across Wikipedia/ArXiv/Web, synthesizes findings, and generates structured Markdown reports with TODO planning.

## Capabilities
- **Problem Decomposition Agent**: Breaks complex topics into searchable sub-queries
- **Multi-Source Search Agent**: Searches Wikipedia, ArXiv, and web with multi-round refinement
- **Summarization Agent**: Synthesizes findings, identifies knowledge gaps, builds knowledge nodes
- **Report Generation Agent**: Produces structured academic Markdown reports with citations
- **TODO Planner Agent**: Generates phased research plans with priorities

## Usage
1. Create a research task via the Dashboard or API
2. The orchestrator runs all agents in sequence: decompose -> search -> summarize -> plan -> report
3. View the generated report, knowledge nodes, and TODO plan

## API Endpoints
- POST /api/research/ - Create research task
- POST /api/research/{id}/run - Start research pipeline
- GET /api/research/{id} - View task with report
- GET /api/articles/ - Manage articles
- POST /api/auth/register - Register user
- POST /api/auth/login - Login

## Environment
Set OPENAI_API_KEY to enable LLM-powered agents.
Optional: OPENAI_BASE_URL for custom endpoints.
