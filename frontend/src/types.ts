// ====== Type Definitions ======

interface User {
  id: string;
  username: string;
  email: string;
  full_name: string;
}

interface LoginResponse {
  access_token: string;
  user: User;
}

interface ResearchTask {
  id: string;
  title: string;
  topic: string;
  description: string;
  status: TaskStatus;
  progress: number;
  queries: SearchQuery[];
  search_results: SearchResult[];
  knowledge_gaps: KnowledgeGap[];
  summary: string;
  final_report: string;
  report_path: string;
  created_at: string;
  updated_at: string;
  completed_at: string | null;
  todo_items: TodoItem[];
  intermediate_reports: IntermediateReport[];
}

type TaskStatus =
  | "pending"
  | "decomposing"
  | "searching"
  | "summarizing"
  | "generating"
  | "completed"
  | "failed";

interface SearchQuery {
  query: string;
  source: string;
  lang: string;
}

interface SearchResult {
  title: string;
  url: string;
  snippet: string;
  source: string;
  relevance_score: number;
}

interface KnowledgeGap {
  topic: string;
  reason: string;
  suggested_queries: string[];
}

interface TodoItem {
  id: string;
  content: string;
  is_completed: boolean;
  priority: "low" | "medium" | "high";
  order_index: number;
}

interface IntermediateReport {
  id: string;
  round_number: number;
  content: string;
  gaps_identified: KnowledgeGap[];
  created_at: string;
}

interface Article {
  id: string;
  title: string;
  content: string;
  abstract: string;
  keywords: string[];
  status: string;
  source_url: string;
  source_type: string;
  word_count: number;
  created_at: string;
  updated_at: string;
}

interface KnowledgeNode {
  id: string;
  title: string;
  content: string;
  node_type: string;
  source: string;
  confidence: number;
  created_at: string;
}

interface TaskListResponse {
  tasks: ResearchTask[];
  total: number;
}

interface CreateTaskPayload {
  title: string;
  topic: string;
  description?: string;
}

interface CreateArticlePayload {
  title: string;
  content?: string;
  abstract?: string;
  keywords?: string[];
}

interface NaturalInputPayload {
  text: string;
}

interface NaturalInputResult {
  action: "research" | "article";
  payload: CreateTaskPayload | CreateArticlePayload;
  explanation: string;
}

type PageName = "dashboard" | "tasks" | "articles" | "knowledge" | "settings";

interface UserSettingsData {
  id: string;
  user_id: string;
  openai_api_key: string;
  openai_base_url: string;
  openai_model: string;
  created_at: string;
  updated_at: string;
}
