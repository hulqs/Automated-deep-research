/// <reference path="types.ts" />

// ====== i18n Translation Dictionary ======
type Lang = "zh" | "en";
const I18N: Record<Lang, Record<string, string>> = {
  zh: {
    // App
    "app.title": "Deep Research",
    "app.subtitle": "AI 驱动的学术研究代理系统",
    "app.dashboard": "仪表盘",
    "app.researchTasks": "研究任务",
    "app.articles": "文章",
    "app.knowledgeGraph": "知识图谱",
    "app.signOut": "退出登录",
    "app.user": "用户",

    // Auth
    "auth.signIn": "登录",
    "auth.createAccount": "创建账号",
    "auth.username": "用户名",
    "auth.password": "密码",
    "auth.email": "邮箱",
    "auth.fullName": "姓名",
    "auth.usernamePlaceholder": "输入用户名",
    "auth.passwordPlaceholder": "输入密码",
    "auth.emailPlaceholder": "your@email.com",
    "auth.fullNamePlaceholder": "你的姓名",
    "auth.passwordMin": "至少6个字符",
    "auth.noAccount": "没有账号？",
    "auth.hasAccount": "已有账号？",
    "auth.createOne": "创建一个",
    "auth.joinDesc": "加入 Deep Research 开始探索",
    "auth.fillAllFields": "请填写所有字段",
    "auth.fillRequired": "请填写必填字段",
    "auth.loginFailed": "登录失败",
    "auth.registerFailed": "注册失败",
    "auth.connectionError": "连接错误: {msg}",

    // Dashboard
    "dashboard.title": "仪表盘",
    "dashboard.welcome": "欢迎回来，{name}",
    "dashboard.totalTasks": "总任务数",
    "dashboard.completed": "已完成",
    "dashboard.running": "进行中",
    "dashboard.quickStart": "快速开始",
    "dashboard.quickStartDesc": "描述你想研究或写作的主题，系统会自动判断是创建研究任务还是文章。",
    "dashboard.quickInputPlaceholder": "例如：量子计算在人工智能中的应用现状、写一篇关于气候变化对农业影响的文章...",
    "dashboard.start": "开始",
    "dashboard.recentTasks": "最近任务",
    "dashboard.newResearch": "+ 新建研究",
    "dashboard.noTasks": "暂无任务",
    "dashboard.noTasksDesc": "开始你的第一个研究",
    "dashboard.analyzing": "分析中...",

    // Tasks
    "tasks.title": "研究任务",
    "tasks.count": "{count} 个任务",
    "tasks.quickCreate": "快速创建",
    "tasks.quickInputPlaceholder": "描述你想研究或写作的主题...",
    "tasks.newTask": "+ 新建研究",
    "tasks.newTaskTitle": "新建研究任务",
    "tasks.titleLabel": "标题",
    "tasks.titlePlaceholder": "例如：量子计算综述",
    "tasks.topicLabel": "研究主题",
    "tasks.topicPlaceholder": "描述你想研究的主题...",
    "tasks.notesLabel": "备注",
    "tasks.notesPlaceholder": "可选...",
    "tasks.cancel": "取消",
    "tasks.startResearch": "开始研究",
    "tasks.creating": "创建中...",
    "tasks.researchStarted": "研究已启动！它在后台运行。刷新以查看进度。",
    "tasks.back": "返回",
    "tasks.researchPlan": "研究计划",
    "tasks.topic": "主题:",
    "tasks.summary": "摘要",
    "tasks.researchInProgress": "研究进行中...",
    "tasks.researchFailed": "研究失败",
    "tasks.researchFailedDesc": "研究过程中发生了错误，请重试或检查你的 API 配置。",
    "tasks.cancelResearch": "终止研究",
    "tasks.confirmCancel": "确定终止这个研究任务？",
    "tasks.retry": "重新研究",
    "tasks.delete": "删除",
    "tasks.confirmDelete": "确定删除这个研究任务？",
    "tasks.titleRequired": "请填写标题和主题",
    "tasks.researchStartedWithTitle": "研究已启动: \"{title}\"",
    "tasks.start": "开始",

    // Articles
    "articles.title": "文章",
    "articles.count": "{count} 篇文章",
    "articles.quickCreate": "快速创建",
    "articles.quickInputPlaceholder": "描述你想写的文章主题...",
    "articles.newArticle": "+ 新建文章",
    "articles.noArticles": "暂无文章",
    "articles.noArticlesDesc": "创建你的第一篇文章",
    "articles.noAbstract": "无摘要",
    "articles.source": "来源",
    "articles.confirmDelete": "确定删除这篇文章？",
    "articles.newArticleTitle": "新建文章",
    "articles.contentLabel": "内容",
    "articles.abstractLabel": "摘要",
    "articles.keywordsLabel": "关键词（逗号分隔）",
    "articles.save": "保存",
    "articles.saving": "保存中...",
    "articles.titleRequired": "标题为必填项",
    "articles.articleCreatedWithTitle": "文章已创建: \"{title}\"",
    "articles.create": "创建",

    // Knowledge
    "knowledge.title": "知识图谱",
    "knowledge.nodeCount": "{count} 个节点",
    "knowledge.noNodes": "暂无知识节点",
    "knowledge.noNodesDesc": "研究过程中会生成知识节点",
    "knowledge.confidence": "置信度: {pct}%",

    // General
    "general.error": "错误",
    "general.loading": "加载中...",
    "general.unauthorized": "未授权",
  },
  en: {
    // App
    "app.title": "Deep Research",
    "app.subtitle": "AI-powered academic research agent system",
    "app.dashboard": "Dashboard",
    "app.researchTasks": "Research Tasks",
    "app.articles": "Articles",
    "app.knowledgeGraph": "Knowledge Graph",
    "app.signOut": "Sign Out",
    "app.user": "User",

    // Auth
    "auth.signIn": "Sign In",
    "auth.createAccount": "Create Account",
    "auth.username": "Username",
    "auth.password": "Password",
    "auth.email": "Email",
    "auth.fullName": "Full Name",
    "auth.usernamePlaceholder": "Enter username",
    "auth.passwordPlaceholder": "Enter password",
    "auth.emailPlaceholder": "your@email.com",
    "auth.fullNamePlaceholder": "Your full name",
    "auth.passwordMin": "Minimum 6 characters",
    "auth.noAccount": "No account?",
    "auth.hasAccount": "Already have an account?",
    "auth.createOne": "Create one",
    "auth.joinDesc": "Join Deep Research to start exploring",
    "auth.fillAllFields": "Please fill in all fields",
    "auth.fillRequired": "Please fill in required fields",
    "auth.loginFailed": "Login failed",
    "auth.registerFailed": "Registration failed",
    "auth.connectionError": "Connection error: {msg}",

    // Dashboard
    "dashboard.title": "Dashboard",
    "dashboard.welcome": "Welcome back, {name}",
    "dashboard.totalTasks": "Total Tasks",
    "dashboard.completed": "Completed",
    "dashboard.running": "In Progress",
    "dashboard.quickStart": "Quick Start",
    "dashboard.quickStartDesc": "Describe your research or writing topic. The system will automatically determine whether to create a research task or an article.",
    "dashboard.quickInputPlaceholder": "e.g., Applications of quantum computing in AI, write an article about climate change impact on agriculture...",
    "dashboard.start": "Start",
    "dashboard.recentTasks": "Recent Tasks",
    "dashboard.newResearch": "+ New Research",
    "dashboard.noTasks": "No tasks yet",
    "dashboard.noTasksDesc": "Start your first research",
    "dashboard.analyzing": "Analyzing...",

    // Tasks
    "tasks.title": "Research Tasks",
    "tasks.count": "{count} tasks",
    "tasks.quickCreate": "Quick Create",
    "tasks.quickInputPlaceholder": "Describe your research or writing topic...",
    "tasks.newTask": "+ New Research",
    "tasks.newTaskTitle": "New Research Task",
    "tasks.titleLabel": "Title",
    "tasks.titlePlaceholder": "e.g., Quantum Computing Review",
    "tasks.topicLabel": "Research Topic",
    "tasks.topicPlaceholder": "Describe your research topic...",
    "tasks.notesLabel": "Notes",
    "tasks.notesPlaceholder": "Optional...",
    "tasks.cancel": "Cancel",
    "tasks.startResearch": "Start Research",
    "tasks.creating": "Creating...",
    "tasks.researchStarted": "Research started! It runs in the background. Refresh to see progress.",
    "tasks.back": "Back",
    "tasks.researchPlan": "Research Plan",
    "tasks.topic": "Topic:",
    "tasks.summary": "Summary",
    "tasks.researchInProgress": "Research in progress...",
    "tasks.researchFailed": "Research Failed",
    "tasks.researchFailedDesc": "An error occurred during research. Please retry or check your API configuration.",
    "tasks.cancelResearch": "Cancel Research",
    "tasks.confirmCancel": "Are you sure you want to cancel this research?",
    "tasks.retry": "Retry Research",
    "tasks.delete": "Delete",
    "tasks.confirmDelete": "Are you sure you want to delete this research task?",
    "tasks.titleRequired": "Please fill in title and topic",
    "tasks.researchStartedWithTitle": "Research started: \"{title}\"",
    "tasks.start": "Start",

    // Articles
    "articles.title": "Articles",
    "articles.count": "{count} articles",
    "articles.quickCreate": "Quick Create",
    "articles.quickInputPlaceholder": "Describe your article topic...",
    "articles.newArticle": "+ New Article",
    "articles.noArticles": "No articles yet",
    "articles.noArticlesDesc": "Create your first article",
    "articles.noAbstract": "No abstract",
    "articles.source": "Source",
    "articles.confirmDelete": "Are you sure you want to delete this article?",
    "articles.newArticleTitle": "New Article",
    "articles.contentLabel": "Content",
    "articles.abstractLabel": "Abstract",
    "articles.keywordsLabel": "Keywords (comma separated)",
    "articles.save": "Save",
    "articles.saving": "Saving...",
    "articles.titleRequired": "Title is required",
    "articles.articleCreatedWithTitle": "Article created: \"{title}\"",
    "articles.create": "Create",

    // Knowledge
    "knowledge.title": "Knowledge Graph",
    "knowledge.nodeCount": "{count} nodes",
    "knowledge.noNodes": "No knowledge nodes yet",
    "knowledge.noNodesDesc": "Knowledge nodes will be generated during research",
    "knowledge.confidence": "Confidence: {pct}%",

    // General
    "general.error": "Error",
    "general.loading": "Loading...",
    "general.unauthorized": "Unauthorized",
  },
};

// ====== i18n Helper ======
let currentLang: Lang = (localStorage.getItem("lang") as Lang) || "zh";

function t(key: string, params?: Record<string, string | number>): string {
  const dict = I18N[currentLang];
  let text = dict[key];
  if (text === undefined) return key;
  if (params) {
    for (const [k, v] of Object.entries(params)) {
      text = text.replace(`{${k}}`, String(v));
    }
  }
  return text;
}

function setLanguage(lang: Lang): void {
  currentLang = lang;
  localStorage.setItem("lang", lang);
  // Update document lang attribute
  document.documentElement.lang = lang === "zh" ? "zh-CN" : "en-US";
  // Update lang-toggle active states
  document.querySelectorAll<HTMLElement>(".lang-toggle").forEach((btn) => {
    const btnLang = btn.getAttribute("data-lang");
    btn.classList.toggle("active", btnLang === lang);
  });
  // Update all data-i18n elements
  applyI18nToDOM();
  // Re-render current page
  if (currentPage) showPage(currentPage);
  // Update sidebar user info
  updateSidebarUser();
}

function applyI18nToDOM(): void {
  // Update text content for elements with data-i18n
  document.querySelectorAll<HTMLElement>("[data-i18n]").forEach((el) => {
    const key = el.getAttribute("data-i18n");
    if (key) {
      el.textContent = t(key);
    }
  });
  // Update placeholders for inputs with data-i18n-placeholder
  document.querySelectorAll<HTMLElement>("[data-i18n-placeholder]").forEach((el) => {
    const key = el.getAttribute("data-i18n-placeholder");
    if (key && (el instanceof HTMLInputElement || el instanceof HTMLTextAreaElement)) {
      el.placeholder = t(key);
    }
  });
  // Update document title
  document.title = t("app.title");
}

// ====== Theme System ======
type ThemeName = "dark" | "light" | "emerald" | "sunset" | "purple";
let currentTheme: ThemeName = (localStorage.getItem("theme") as ThemeName) || "dark";

function setTheme(theme: ThemeName): void {
  currentTheme = theme;
  localStorage.setItem("theme", theme);
  document.documentElement.setAttribute("data-theme", theme);
  // Update theme switcher active state
  document.querySelectorAll<HTMLElement>(".theme-dot").forEach((dot) => {
    const dotTheme = dot.getAttribute("data-theme-val");
    dot.classList.toggle("active", dotTheme === theme);
    dot.setAttribute("aria-pressed", String(dotTheme === theme));
  });
}

function initTheme(): void {
  setTheme(currentTheme);
}

// ====== Application State ======
const API = "http://localhost:8000/api";
let token: string = localStorage.getItem("token") || "";
let user: User | null = null;
let currentPage: PageName = "dashboard";

// Restore user from localStorage
try {
  const stored = localStorage.getItem("user");
  if (stored) user = JSON.parse(stored) as User;
} catch { /* ignore */ }

// ====== Auth ======

function showRegister(): void {
  document.getElementById("loginCard")!.classList.add("hidden");
  document.getElementById("registerCard")!.classList.remove("hidden");
}

function showLogin(): void {
  document.getElementById("registerCard")!.classList.add("hidden");
  document.getElementById("loginCard")!.classList.remove("hidden");
}

function showErr(id: string, msg: string): void {
  const el = document.getElementById(id)!;
  el.textContent = msg;
  el.style.display = "block";
}

async function doLogin(): Promise<void> {
  document.getElementById("loginError")!.style.display = "none";
  const username = (document.getElementById("loginUser") as HTMLInputElement).value.trim();
  const password = (document.getElementById("loginPass") as HTMLInputElement).value;
  if (!username || !password) return showErr("loginError", t("auth.fillAllFields"));

  try {
    const r = await fetch(`${API}/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }),
    });
    const d: LoginResponse & { detail?: string } = await r.json();
    if (!r.ok) return showErr("loginError", d.detail || t("auth.loginFailed"));

    token = d.access_token;
    user = d.user;
    localStorage.setItem("token", token);
    localStorage.setItem("user", JSON.stringify(user));
    showApp();
  } catch (e) {
    showErr("loginError", t("auth.connectionError", { msg: (e as Error).message }));
  }
}

async function doRegister(): Promise<void> {
  document.getElementById("regError")!.style.display = "none";
  const username = (document.getElementById("regUser") as HTMLInputElement).value.trim();
  const email = (document.getElementById("regEmail") as HTMLInputElement).value.trim();
  const full_name = (document.getElementById("regName") as HTMLInputElement).value.trim();
  const password = (document.getElementById("regPass") as HTMLInputElement).value;
  if (!username || !email || !password)
    return showErr("regError", t("auth.fillRequired"));

  try {
    const r = await fetch(`${API}/auth/register`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, email, full_name, password }),
    });
    const d: LoginResponse & { detail?: string } = await r.json();
    if (!r.ok) return showErr("regError", d.detail || t("auth.registerFailed"));

    token = d.access_token;
    user = d.user;
    localStorage.setItem("token", token);
    localStorage.setItem("user", JSON.stringify(user));
    showApp();
  } catch (e) {
    showErr("regError", t("auth.connectionError", { msg: (e as Error).message }));
  }
}

// ====== App Shell ======

function updateSidebarUser(): void {
  const avatar = document.getElementById("sidebarAvatar")!;
  const nameEl = document.getElementById("sidebarName")!;
  avatar.textContent = (user!.full_name || user!.username)[0].toUpperCase();
  nameEl.textContent = user!.full_name || user!.username;
}

function showApp(): void {
  document.getElementById("authPage")!.classList.add("hidden");
  document.getElementById("appLayout")!.classList.remove("hidden");
  updateSidebarUser();

  // Apply language setting
  document.documentElement.lang = currentLang === "zh" ? "zh-CN" : "en-US";
  applyI18nToDOM();

  const saved = localStorage.getItem("currentPage") as PageName | null;
  const validPages: PageName[] = ["dashboard", "tasks", "articles", "knowledge"];
  showPage(saved && validPages.includes(saved) ? saved : "dashboard");
}

function doLogout(): void {
  token = "";
  user = null;
  localStorage.removeItem("token");
  localStorage.removeItem("user");
  localStorage.removeItem("currentPage");
  document.getElementById("authPage")!.classList.remove("hidden");
  document.getElementById("appLayout")!.classList.add("hidden");
}

function showPage(page: PageName): void {
  currentPage = page;
  localStorage.setItem("currentPage", page);

  document.querySelectorAll<HTMLElement>(".nav-item").forEach((n) => n.classList.remove("active"));
  const activeNav = document.querySelector<HTMLElement>(`.nav-item[data-page="${page}"]`);
  if (activeNav) activeNav.classList.add("active");

  const mc = document.getElementById("mainContent")!;
  switch (page) {
    case "dashboard": renderDashboard(mc); break;
    case "tasks": renderTasks(mc); break;
    case "articles": renderArticles(mc); break;
    case "knowledge": renderKnowledge(mc); break;
  }
}

// ====== API Helper ======

async function api<T = unknown>(
  path: string,
  opts: RequestInit = {}
): Promise<{ json(): Promise<T>; ok: boolean; status: number }> {
  const h: Record<string, string> = {
    "Content-Type": "application/json",
    Authorization: `Bearer ${token}`,
    ...(opts.headers as Record<string, string> || {}),
  };
  const r = await fetch(`${API}${path}`, { ...opts, headers: h });
  if (r.status === 401) {
    doLogout();
    throw new Error(t("general.unauthorized"));
  }
  return r;
}

// ====== Dashboard ======

async function renderDashboard(mc: HTMLElement): Promise<void> {
  mc.innerHTML = `<div class="loading"><div class="spinner"></div></div>`;
  try {
    const [tasksR, articlesR] = await Promise.all([
      api<TaskListResponse>("/research/?limit=100"),
      api<Article[]>("/articles/?limit=100"),
    ]);
    const tasksData = await tasksR.json();
    const articles = await articlesR.json();
    const taskList: ResearchTask[] = tasksData.tasks || (tasksData as unknown as ResearchTask[]) || [];

    const total = taskList.length;
    const completed = taskList.filter((t) => t.status === "completed").length;
    const running = taskList.filter((t) => t.status !== "completed" && t.status !== "failed").length;

    mc.innerHTML =
      `<div class="page-header"><h1>${t("dashboard.title")}</h1><p>${t("dashboard.welcome", { name: esc(user!.full_name || user!.username) })}</p></div>` +
      `<div class="stats-grid">` +
        `<div class="stat-card"><div class="stat-value" style="color:var(--accent)">${total}</div><div class="stat-label">${t("dashboard.totalTasks")}</div></div>` +
        `<div class="stat-card"><div class="stat-value" style="color:var(--success)">${completed}</div><div class="stat-label">${t("dashboard.completed")}</div></div>` +
        `<div class="stat-card"><div class="stat-value" style="color:var(--warn)">${running}</div><div class="stat-label">${t("dashboard.running")}</div></div>` +
      `</div>` +
      // Natural input area
      `<div class="card" style="margin-bottom:24px">` +
        `<div class="card-title" style="margin-bottom:12px">${t("dashboard.quickStart")}</div>` +
        `<p style="color:var(--text2);font-size:13px;margin-bottom:12px">${t("dashboard.quickStartDesc")}</p>` +
        `<div style="display:flex;gap:10px">` +
          `<input id="quickInput" class="search-input" style="max-width:100%;flex:1" placeholder="${t("dashboard.quickInputPlaceholder")}">` +
          `<button class="btn btn-primary" id="quickSubmitBtn" onclick="handleQuickInput()">${t("dashboard.start")}</button>` +
        `</div>` +
      `</div>` +
      `<div class="toolbar">` +
        `<h3 style="font-size:16px">${t("dashboard.recentTasks")}</h3>` +
        `<button class="btn btn-primary btn-sm" style="margin-left:auto" onclick="showNewTaskModal()">${t("dashboard.newResearch")}</button>` +
      `</div>` +
      `<div id="recentTasks">${renderTaskList(taskList.slice(0, 5))}</div>`;
  } catch (e) {
    mc.innerHTML = `<div class="empty-state"><h3>${t("general.error")}</h3><p>${(e as Error).message}</p></div>`;
  }
}

// ====== Natural Chinese Input ======

async function handleQuickInputGeneric(
  inputId: string,
  btnId: string,
  btnRestoreText: string,
  showAlerts: boolean = false,
): Promise<void> {
  const input = document.getElementById(inputId) as HTMLInputElement;
  const btn = document.getElementById(btnId) as HTMLButtonElement;
  const text = input.value.trim();
  if (!text) return;

  btn.textContent = t("dashboard.analyzing");
  btn.disabled = true;
  try {
    const r = await api<NaturalInputResult>("/ai/parse-input", {
      method: "POST",
      body: JSON.stringify({ text } as NaturalInputPayload),
    });
    const result = await r.json();

    if (result.action === "research") {
      const payload = result.payload as CreateTaskPayload;
      const taskR = await api<ResearchTask>("/research/", {
        method: "POST",
        body: JSON.stringify(payload),
      });
      const task = await taskR.json();
      await api(`/research/${task.id}/run`, { method: "POST" });
      showPage("tasks");
      input.value = "";
      if (showAlerts) {
        setTimeout(() => alert(`${t("tasks.researchStartedWithTitle", { title: task.title })}\n${result.explanation}`), 300);
      }
    } else {
      const payload = result.payload as CreateArticlePayload;
      await api<Article>("/articles/", {
        method: "POST",
        body: JSON.stringify(payload),
      });
      showPage("articles");
      input.value = "";
      if (showAlerts) {
        setTimeout(() => alert(`${t("articles.articleCreatedWithTitle", { title: payload.title })}\n${result.explanation}`), 300);
      }
    }
  } catch (e) {
    alert(t("general.error") + ": " + (e as Error).message);
  } finally {
    btn.textContent = btnRestoreText;
    btn.disabled = false;
  }
}

function handleQuickInput(): void {
  handleQuickInputGeneric("quickInput", "quickSubmitBtn", t("dashboard.start"), true);
}

function handleQuickInputFromTasks(): void {
  handleQuickInputGeneric("tasksQuickInput", "tasksQuickBtn", t("tasks.start"));
}

function handleQuickInputFromArticles(): void {
  handleQuickInputGeneric("articlesQuickInput", "articlesQuickBtn", t("articles.create"));
}

// Handle Enter key in quick input
document.addEventListener("keydown", (e: KeyboardEvent) => {
  if (e.key === "Enter" && document.activeElement?.id === "quickInput") {
    handleQuickInput();
  }
});

// ====== Task Rendering ======

function renderTaskList(tasks: ResearchTask[]): string {
  if (!tasks || tasks.length === 0)
    return `<div class="empty-state"><h3>${t("dashboard.noTasks")}</h3><p>${t("dashboard.noTasksDesc")}</p><button class="btn btn-primary" onclick="showNewTaskModal()">${t("dashboard.newResearch")}</button></div>`;

  const statusClass: Record<string, string> = {
    pending: "status-pending",
    decomposing: "status-running",
    searching: "status-running",
    summarizing: "status-running",
    generating: "status-running",
    completed: "status-completed",
    failed: "status-failed",
  };

  return tasks
    .map((t) => {
      const sc = statusClass[t.status] || "status-pending";
      const progressHtml =
        t.status !== "completed" && t.status !== "failed"
          ? `<div class="progress-bar"><div class="progress-fill" style="width:${(t.progress || 0) * 100}%"></div></div>`
          : "";
      return (
        `<div class="task-item" onclick="viewTask('${t.id}')">` +
        `<div class="task-left">` +
          `<div class="task-title">${esc(t.title)}</div>` +
          `<div class="task-meta"><span>${esc(t.topic).substring(0, 60)}</span><span>${new Date(t.created_at).toLocaleDateString()}</span></div>` +
        `</div>` +
        `<div class="task-right"><span class="status-badge ${sc}">${t.status}</span>${progressHtml}</div>` +
        `</div>`
      );
    })
    .join("");
}

async function renderTasks(mc: HTMLElement): Promise<void> {
  mc.innerHTML = `<div class="loading"><div class="spinner"></div></div>`;
  try {
    const r = await api<TaskListResponse>("/research/?limit=100");
    const d = await r.json();
    const tasks: ResearchTask[] = d.tasks || (d as unknown as ResearchTask[]) || [];

    mc.innerHTML =
      `<div class="page-header"><h1>${t("tasks.title")}</h1><p>${t("tasks.count", { count: tasks.length })}</p></div>` +
      `<div class="card" style="margin-bottom:20px">` +
        `<div class="card-title" style="margin-bottom:10px">${t("tasks.quickCreate")}</div>` +
        `<div style="display:flex;gap:10px">` +
          `<input id="tasksQuickInput" class="search-input" style="max-width:100%;flex:1" placeholder="${t("tasks.quickInputPlaceholder")}">` +
          `<button class="btn btn-primary btn-sm" id="tasksQuickBtn" onclick="handleQuickInputFromTasks()">${t("tasks.start")}</button>` +
        `</div>` +
      `</div>` +
      `<div class="toolbar"><button class="btn btn-primary" onclick="showNewTaskModal()">${t("tasks.newTask")}</button></div>` +
      `<div id="taskList">${renderTaskList(tasks)}</div>`;
  } catch (e) {
    mc.innerHTML = `<div class="empty-state"><h3>${t("general.error")}</h3><p>${(e as Error).message}</p></div>`;
  }
}

// ====== Task Modal & Actions ======

function showNewTaskModal(): void {
  const overlay = document.createElement("div");
  overlay.className = "modal-overlay";
  overlay.innerHTML =
    `<div class="modal"><h3>${t("tasks.newTaskTitle")}</h3>` +
    `<div class="form-group"><label>${t("tasks.titleLabel")}</label><input id="ntTitle" placeholder="${t("tasks.titlePlaceholder")}"></div>` +
    `<div class="form-group"><label>${t("tasks.topicLabel")}</label><textarea id="ntTopic" rows="4" placeholder="${t("tasks.topicPlaceholder")}"></textarea></div>` +
    `<div class="form-group"><label>${t("tasks.notesLabel")}</label><textarea id="ntDesc" rows="2" placeholder="${t("tasks.notesPlaceholder")}"></textarea></div>` +
    `<div class="modal-actions"><button class="btn btn-secondary" id="cancelModalBtn">${t("tasks.cancel")}</button><button class="btn btn-primary" id="createTaskBtn">${t("tasks.startResearch")}</button></div></div>`;
  document.body.appendChild(overlay);

  overlay.querySelector("#cancelModalBtn")!.addEventListener("click", () => overlay.remove());
  overlay.querySelector("#createTaskBtn")!.addEventListener("click", () => createTask(overlay));
  overlay.addEventListener("click", (e) => { if (e.target === overlay) overlay.remove(); });
}

async function createTask(overlay: HTMLElement): Promise<void> {
  const title = (overlay.querySelector("#ntTitle") as HTMLInputElement).value.trim();
  const topic = (overlay.querySelector("#ntTopic") as HTMLTextAreaElement).value.trim();
  const description = (overlay.querySelector("#ntDesc") as HTMLTextAreaElement).value.trim();
  if (!title || !topic) return alert(t("tasks.titleRequired"));

  const btn = overlay.querySelector("#createTaskBtn") as HTMLButtonElement;
  btn.textContent = t("tasks.creating");
  btn.disabled = true;
  try {
    const r = await api<ResearchTask>("/research/", {
      method: "POST",
      body: JSON.stringify({ title, topic, description } as CreateTaskPayload),
    });
    const task = await r.json();
    overlay.remove();
    await api(`/research/${task.id}/run`, { method: "POST" });
    showPage("tasks");
    setTimeout(() => alert(t("tasks.researchStarted")), 300);
  } catch (e) {
    alert(t("general.error") + ": " + (e as Error).message);
    btn.textContent = t("tasks.startResearch");
    btn.disabled = false;
  }
}

async function viewTask(taskId: string): Promise<void> {
  const mc = document.getElementById("mainContent")!;
  mc.innerHTML = `<div class="loading"><div class="spinner"></div></div>`;
  try {
    const r = await api<ResearchTask>(`/research/${taskId}`);
    const tsk = await r.json();

    if (tsk.final_report) {
      const reportHtml = parseMarkdown(tsk.final_report);
      mc.innerHTML =
        `<div style="margin-bottom:16px"><button class="btn btn-secondary btn-sm" onclick="showPage('tasks')">${t("tasks.back")}</button></div>` +
        `<div class="report-content">${reportHtml}</div>`;
    } else {
      let todoHtml = "";
      if (tsk.todo_items && tsk.todo_items.length > 0) {
        todoHtml =
          `<h4 style="margin:16px 0 8px">${t("tasks.researchPlan")}</h4><ul class="todo-list">` +
          tsk.todo_items
            .map(
              (ti) =>
                `<li class="todo-item">` +
                `<div class="todo-check${ti.is_completed ? " checked" : ""}"></div>` +
                `<span class="todo-text${ti.is_completed ? " done" : ""}">${esc(ti.content)}</span>` +
                `<span class="todo-priority priority-${ti.priority}">${ti.priority}</span>` +
                `</li>`
            )
            .join("") +
          `</ul>`;
      }

      const statusLabel =
        tsk.status === "completed"
          ? "status-completed"
          : tsk.status === "failed"
            ? "status-failed"
            : "status-running";

      // Determine the body content based on status
      let bodyContent = "";
      if (tsk.status === "failed") {
        const errorMsg = (tsk as any).metadata_json?.error || t("tasks.researchFailed");
        bodyContent =
          `<div class="empty-state" style="padding:32px 16px">` +
            `<span class="empty-icon">⚠</span>` +
            `<h3 style="color:var(--danger)">${t("tasks.researchFailed")}</h3>` +
            `<p style="color:var(--text-secondary);margin-bottom:8px">${t("tasks.researchFailedDesc")}</p>` +
            (errorMsg ? `<p style="font-size:0.8rem;color:var(--text-tertiary);margin-bottom:16px">${esc(errorMsg)}</p>` : "") +
            `<button class="btn btn-primary btn-sm" onclick="retryResearch('${tsk.id}')">${t("tasks.retry")}</button>` +
          `</div>`;
      } else if (tsk.summary) {
        bodyContent =
          `<h4 style="margin-bottom:8px">${t("tasks.summary")}</h4>` +
          `<div class="card" style="background:var(--surface2);white-space:pre-wrap;max-height:400px;overflow-y:auto;font-size:14px">${esc(tsk.summary)}</div>`;
      } else {
        bodyContent = `<div class="empty-state"><p>${t("tasks.researchInProgress")}</p></div>`;
      }

      mc.innerHTML =
        `<div style="margin-bottom:16px"><button class="btn btn-secondary btn-sm" onclick="showPage('tasks')">${t("tasks.back")}</button></div>` +
        `<div class="card">` +
          `<div class="card-header">` +
            `<span class="card-title">${esc(tsk.title)}</span>` +
            `<span class="status-badge ${statusLabel}">${tsk.status}</span>` +
          `</div>` +
          `<p style="color:var(--text2);margin-bottom:12px"><strong>${t("tasks.topic")}</strong> ${esc(tsk.topic)}</p>` +
          bodyContent +
          todoHtml +
          `<div style="display:flex;gap:8px;margin-top:16px">` +
            (tsk.status !== "completed" && tsk.status !== "failed"
              ? `<button class="btn btn-danger btn-sm" onclick="cancelResearch('${tsk.id}')">${t("tasks.cancelResearch")}</button>`
              : "") +
            `<button class="btn btn-danger btn-sm" onclick="deleteTask('${tsk.id}')">${t("tasks.delete")}</button>` +
          `</div>` +
        `</div>`;
    }
  } catch (e) {
    mc.innerHTML = `<div class="empty-state"><h3>${t("general.error")}</h3><p>${(e as Error).message}</p></div>`;
  }
}

async function deleteTask(id: string): Promise<void> {
  if (!confirm(t("tasks.confirmDelete"))) return;
  await api(`/research/${id}`, { method: "DELETE" });
  showPage("tasks");
}

async function cancelResearch(id: string): Promise<void> {
  if (!confirm(t("tasks.confirmCancel"))) return;
  try {
    await api(`/research/${id}/cancel`, { method: "POST" });
    // Refresh the task view
    const mc = document.getElementById("mainContent")!;
    if (mc) viewTask(id);
  } catch (e) {
    alert(t("general.error") + ": " + (e as Error).message);
  }
}

async function retryResearch(id: string): Promise<void> {
  try {
    await api(`/research/${id}/run`, { method: "POST" });
    // Refresh the task view
    const mc = document.getElementById("mainContent")!;
    if (mc) viewTask(id);
  } catch (e) {
    alert(t("general.error") + ": " + (e as Error).message);
  }
}

// ====== Articles ======

async function renderArticles(mc: HTMLElement): Promise<void> {
  mc.innerHTML = `<div class="loading"><div class="spinner"></div></div>`;
  try {
    const r = await api<Article[]>("/articles/?limit=100");
    const articles = await r.json();

    mc.innerHTML =
      `<div class="page-header"><h1>${t("articles.title")}</h1><p>${t("articles.count", { count: articles.length })}</p></div>` +
      `<div class="card" style="margin-bottom:20px">` +
        `<div class="card-title" style="margin-bottom:10px">${t("articles.quickCreate")}</div>` +
        `<div style="display:flex;gap:10px">` +
          `<input id="articlesQuickInput" class="search-input" style="max-width:100%;flex:1" placeholder="${t("articles.quickInputPlaceholder")}">` +
          `<button class="btn btn-primary btn-sm" id="articlesQuickBtn" onclick="handleQuickInputFromArticles()">${t("articles.create")}</button>` +
        `</div>` +
      `</div>` +
      `<div class="toolbar"><button class="btn btn-primary" onclick="showNewArticleModal()">${t("articles.newArticle")}</button></div>` +
      `<div class="grid-2">` +
        (articles.length
          ? articles
              .map(
                (a) =>
                  `<div class="article-card" onclick="viewArticle('${a.id}')">` +
                  `<div class="title">${esc(a.title)}</div>` +
                  `<div class="abstract">${esc(a.abstract || t("articles.noAbstract"))}</div>` +
                  `<div class="article-tags">` +
                  (a.keywords || []).map((k) => `<span class="tag">${esc(k)}</span>`).join("") +
                  `<span class="tag" style="background:var(--accent);color:#fff">${a.source_type}</span>` +
                  `</div>` +
                  `<div style="font-size:12px;color:var(--text2);margin-top:8px">${new Date(a.updated_at).toLocaleDateString()}</div>` +
                  `</div>`
              )
              .join("")
          : `<div class="empty-state"><h3>${t("articles.noArticles")}</h3><p>${t("articles.noArticlesDesc")}</p></div>`) +
      `</div>`;
  } catch (e) {
    mc.innerHTML = `<div class="empty-state"><h3>${t("general.error")}</h3><p>${(e as Error).message}</p></div>`;
  }
}

function showNewArticleModal(): void {
  const overlay = document.createElement("div");
  overlay.className = "modal-overlay";
  overlay.innerHTML =
    `<div class="modal"><h3>${t("articles.newArticleTitle")}</h3>` +
    `<div class="form-group"><label>${t("articles.titleLabel")}</label><input id="naTitle"></div>` +
    `<div class="form-group"><label>${t("articles.contentLabel")}</label><textarea id="naContent" rows="8"></textarea></div>` +
    `<div class="form-group"><label>${t("articles.abstractLabel")}</label><textarea id="naAbstract" rows="2"></textarea></div>` +
    `<div class="form-group"><label>${t("articles.keywordsLabel")}</label><input id="naKeywords"></div>` +
    `<div class="modal-actions"><button class="btn btn-secondary" id="cxlArt">${t("tasks.cancel")}</button><button class="btn btn-primary" id="svArt">${t("articles.save")}</button></div></div>`;
  document.body.appendChild(overlay);

  overlay.querySelector("#cxlArt")!.addEventListener("click", () => overlay.remove());
  overlay.querySelector("#svArt")!.addEventListener("click", () => createArticle(overlay));
  overlay.addEventListener("click", (e) => { if (e.target === overlay) overlay.remove(); });
}

async function createArticle(overlay: HTMLElement): Promise<void> {
  const title = (overlay.querySelector("#naTitle") as HTMLInputElement).value.trim();
  const content = (overlay.querySelector("#naContent") as HTMLTextAreaElement).value.trim();
  const abstract = (overlay.querySelector("#naAbstract") as HTMLTextAreaElement).value.trim();
  const keywords = (overlay.querySelector("#naKeywords") as HTMLInputElement).value
    .split(",")
    .map((k) => k.trim())
    .filter(Boolean);
  if (!title) return alert(t("articles.titleRequired"));

  const btn = overlay.querySelector("#svArt") as HTMLButtonElement;
  btn.textContent = t("articles.saving");
  btn.disabled = true;
  try {
    await api<Article>("/articles/", {
      method: "POST",
      body: JSON.stringify({ title, content, abstract, keywords } as CreateArticlePayload),
    });
    overlay.remove();
    showPage("articles");
  } catch (e) {
    alert(t("general.error") + ": " + (e as Error).message);
    btn.textContent = t("articles.save");
    btn.disabled = false;
  }
}

async function viewArticle(id: string): Promise<void> {
  const mc = document.getElementById("mainContent")!;
  mc.innerHTML = `<div class="loading"><div class="spinner"></div></div>`;
  try {
    const r = await api<Article>(`/articles/${id}`);
    const a = await r.json();

    mc.innerHTML =
      `<div style="margin-bottom:16px"><button class="btn btn-secondary btn-sm" onclick="showPage('articles')">${t("tasks.back")}</button></div>` +
      `<div class="report-content">` +
        `<h1>${esc(a.title)}</h1>` +
        `<p style="color:var(--text2)">${esc(a.abstract)}</p>` +
        `<div style="display:flex;gap:6px;margin:12px 0">` +
          (a.keywords || []).map((k) => `<span class="tag">${esc(k)}</span>`).join("") +
        `</div>` +
        `<div style="white-space:pre-wrap;margin-top:24px">${esc(a.content)}</div>` +
        (a.source_url ? `<p style="margin-top:16px"><a href="${a.source_url}" target="_blank">${t("articles.source")}</a></p>` : "") +
        `<button class="btn btn-danger btn-sm" style="margin-top:16px" onclick="deleteArticle('${a.id}')">${t("tasks.delete")}</button>` +
      `</div>`;
  } catch (e) {
    mc.innerHTML = `<div class="empty-state"><h3>${t("general.error")}</h3><p>${(e as Error).message}</p></div>`;
  }
}

async function deleteArticle(id: string): Promise<void> {
  if (!confirm(t("articles.confirmDelete"))) return;
  await api(`/articles/${id}`, { method: "DELETE" });
  showPage("articles");
}

// ====== Knowledge Graph ======

async function renderKnowledge(mc: HTMLElement): Promise<void> {
  mc.innerHTML = `<div class="loading"><div class="spinner"></div></div>`;
  try {
    const r = await api<KnowledgeNode[]>("/articles/knowledge-nodes");
    const nodes = await r.json();

    mc.innerHTML =
      `<div class="page-header"><h1>${t("knowledge.title")}</h1><p>${t("knowledge.nodeCount", { count: nodes.length })}</p></div>` +
      `<div class="grid-2">` +
        (nodes.length
          ? nodes
              .map(
                (n) =>
                  `<div class="card">` +
                  `<div class="card-title">${esc(n.title)}</div>` +
                  `<div style="font-size:13px;color:var(--text2);margin:8px 0">${esc(n.content).substring(0, 300)}</div>` +
                  `<div class="article-tags">` +
                    `<span class="tag">${n.node_type}</span>` +
                    `<span class="tag">${t("knowledge.confidence", { pct: Math.round(n.confidence * 100) })}</span>` +
                  `</div>` +
                  `</div>`
              )
              .join("")
          : `<div class="empty-state"><h3>${t("knowledge.noNodes")}</h3><p>${t("knowledge.noNodesDesc")}</p></div>`) +
      `</div>`;
  } catch (e) {
    mc.innerHTML = `<div class="empty-state"><h3>${t("general.error")}</h3><p>${(e as Error).message}</p></div>`;
  }
}

// ====== Markdown to HTML Parser ======

function parseMarkdown(md: string): string {
  if (!md) return "";

  // Split into lines for block-level processing
  const lines = md.split("\n");
  const html: string[] = [];
  let i = 0;
  let inCodeBlock = false;
  let codeBlockContent = "";
  let codeBlockLang = "";
  let inTable = false;
  let tableRows: string[][] = [];
  let tableAligns: string[] = [];
  let inList: string | null = null; // 'ul' | 'ol'

  function flushList(): void {
    if (inList) {
      html.push(`</${inList}>`);
      inList = null;
    }
  }

  function flushTable(): void {
    if (!inTable || tableRows.length === 0) return;
    let tHtml = "<table>";
    // Header
    if (tableRows.length > 0) {
      tHtml += "<thead><tr>";
      for (let ci = 0; ci < tableRows[0].length; ci++) {
        const align = tableAligns[ci] || "left";
        tHtml += `<th style="text-align:${align}">${parseInline(tableRows[0][ci])}</th>`;
      }
      tHtml += "</tr></thead>";
    }
    // Body
    if (tableRows.length > 1) {
      tHtml += "<tbody>";
      for (let ri = 1; ri < tableRows.length; ri++) {
        tHtml += "<tr>";
        for (let ci = 0; ci < tableRows[ri].length; ci++) {
          const align = tableAligns[ci] || "left";
          tHtml += `<td style="text-align:${align}">${parseInline(tableRows[ri][ci])}</td>`;
        }
        tHtml += "</tr>";
      }
      tHtml += "</tbody>";
    }
    tHtml += "</table>";
    html.push(tHtml);
    tableRows = [];
    tableAligns = [];
    inTable = false;
  }

  function parseTableCellRow(line: string): string[] {
    // | col1 | col2 | col3 |
    const trimmed = line.replace(/^\||\|$/g, "");
    return trimmed.split("|").map((c) => c.trim());
  }

  function isAlignRow(cells: string[]): boolean {
    return cells.every((c) => /^:?-{3,}:?$/.test(c));
  }

  function getAligns(cells: string[]): string[] {
    return cells.map((c) => {
      if (c.startsWith(":") && c.endsWith(":")) return "center";
      if (c.endsWith(":")) return "right";
      return "left";
    });
  }

  while (i < lines.length) {
    const raw = lines[i];

    // Code block toggle
    if (/^```/.test(raw)) {
      flushList();
      flushTable();
      if (!inCodeBlock) {
        inCodeBlock = true;
        codeBlockLang = raw.replace(/^```/, "").trim();
        codeBlockContent = "";
      } else {
        // Close code block
        const langAttr = codeBlockLang ? ` class="language-${escHtml(codeBlockLang)}"` : "";
        html.push(
          `<pre><code${langAttr}>${escHtml(codeBlockContent).replace(/\n$/, "")}</code></pre>`
        );
        inCodeBlock = false;
        codeBlockLang = "";
        codeBlockContent = "";
      }
      i++;
      continue;
    }

    if (inCodeBlock) {
      codeBlockContent += (codeBlockContent ? "\n" : "") + raw;
      i++;
      continue;
    }

    // Table
    const isTableLine = /^\|.*\|$/.test(raw.trim());
    if (isTableLine) {
      flushList();
      const cells = parseTableCellRow(raw.trim());
      if (!inTable) {
        inTable = true;
        tableRows = [cells];
      } else if (inTable && tableRows.length === 1 && isAlignRow(cells)) {
        tableAligns = getAligns(cells);
      } else {
        tableRows.push(cells);
      }
      i++;
      continue;
    } else if (inTable) {
      flushTable();
    }

    // Horizontal rule
    if (/^(-{3,}|\*{3,}|_{3,})\s*$/.test(raw.trim())) {
      flushList();
      html.push("<hr>");
      i++;
      continue;
    }

    // Headings
    const hMatch = raw.match(/^(#{1,4})\s+(.+)$/);
    if (hMatch) {
      flushList();
      const level = hMatch[1].length;
      html.push(`<h${level}>${parseInline(hMatch[2])}</h${level}>`);
      i++;
      continue;
    }

    // Blockquote
    if (/^>\s?/.test(raw)) {
      flushList();
      const qLines: string[] = [];
      while (i < lines.length && /^>\s?/.test(lines[i])) {
        qLines.push(lines[i].replace(/^>\s?/, ""));
        i++;
      }
      html.push(`<blockquote>${parseMarkdown(qLines.join("\n"))}</blockquote>`);
      continue;
    }

    // Unordered list
    const ulMatch = raw.match(/^(\s*)[-*+]\s+(.+)$/);
    if (ulMatch) {
      flushList();
      if (inList !== "ul") {
        if (inList) flushList();
        html.push("<ul>");
        inList = "ul";
      }
      html.push(`<li>${parseInline(ulMatch[2])}</li>`);
      i++;
      continue;
    }

    // Ordered list
    const olMatch = raw.match(/^(\s*)\d+\.\s+(.+)$/);
    if (olMatch) {
      flushList();
      if (inList !== "ol") {
        if (inList) flushList();
        html.push("<ol>");
        inList = "ol";
      }
      html.push(`<li>${parseInline(olMatch[2])}</li>`);
      i++;
      continue;
    }

    // Empty line — break paragraphs and lists
    if (raw.trim() === "") {
      flushList();
      if (html.length > 0 && !/^<\/?(h[1-4]|hr|ul|ol|table|blockquote|pre|div)/.test(html[html.length - 1])) {
        // paragraph break
      }
      i++;
      continue;
    }

    // Paragraph — collect consecutive non-special lines
    flushList();
    const pLines: string[] = [];
    while (
      i < lines.length &&
      lines[i].trim() !== "" &&
      !/^```/.test(lines[i]) &&
      !/^\|.*\|$/.test(lines[i].trim()) &&
      !/^(-{3,}|\*{3,}|_{3,})\s*$/.test(lines[i].trim()) &&
      !/^(#{1,4})\s/.test(lines[i]) &&
      !/^>\s?/.test(lines[i]) &&
      !/^(\s*)[-*+]\s+/.test(lines[i]) &&
      !/^(\s*)\d+\.\s+/.test(lines[i])
    ) {
      pLines.push(lines[i]);
      i++;
    }
    if (pLines.length > 0) {
      html.push(`<p>${parseInline(pLines.join("\n"))}</p>`);
    }
  }

  // Close any open blocks
  if (inCodeBlock) {
    const langAttr = codeBlockLang ? ` class="language-${escHtml(codeBlockLang)}"` : "";
    html.push(`<pre><code${langAttr}>${escHtml(codeBlockContent)}</code></pre>`);
  }
  flushTable();
  flushList();

  return html.join("\n");
}

function parseInline(text: string): string {
  if (!text) return "";
  // Escape HTML first
  let out = escHtml(text);
  // Images (before links)
  out = out.replace(/!\[([^\]]*)\]\(([^)\s]+)(?:\s+"([^"]*)")?\)/g,
    (_m, alt, src, title) => {
      const t = title ? ` title="${escHtml(title)}"` : "";
      return `<img src="${escHtml(src)}" alt="${escHtml(alt)}"${t}>`;
    });
  // Links
  out = out.replace(/\[([^\]]+)\]\(([^)\s]+)(?:\s+"([^"]*)")?\)/g,
    (_m, text, url, title) => {
      const t = title ? ` title="${escHtml(title)}"` : "";
      return `<a href="${escHtml(url)}"${t} target="_blank" rel="noopener">${text}</a>`;
    });
  // Bold + Italic
  out = out.replace(/\*\*\*(.+?)\*\*\*/g, "<strong><em>$1</em></strong>");
  out = out.replace(/___(.+?)___/g, "<strong><em>$1</em></strong>");
  // Bold
  out = out.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");
  out = out.replace(/__(.+?)__/g, "<strong>$1</strong>");
  // Italic
  out = out.replace(/\*(.+?)\*/g, "<em>$1</em>");
  out = out.replace(/_(.+?)_/g, "<em>$1</em>");
  // Inline code
  out = out.replace(/`([^`]+)`/g, "<code>$1</code>");
  // Strikethrough
  out = out.replace(/~~(.+?)~~/g, "<del>$1</del>");
  // Soft line breaks within paragraphs → <br>
  out = out.replace(/\n/g, "<br>");
  return out;
}

function escHtml(s: string): string {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

// ====== Utilities ======

function esc(s: string | null | undefined): string {
  if (!s) return "";
  const d = document.createElement("div");
  d.textContent = s;
  return d.innerHTML;
}

// ====== Init ======

document.addEventListener("DOMContentLoaded", () => {
  // Initialize theme
  initTheme();
  // Set initial language direction
  document.documentElement.lang = currentLang === "zh" ? "zh-CN" : "en-US";
  // Apply i18n to static DOM elements
  applyI18nToDOM();
  // Wire up theme switcher dots
  document.querySelectorAll<HTMLElement>(".theme-dot").forEach((dot) => {
    dot.addEventListener("click", () => {
      const theme = dot.getAttribute("data-theme-val") as ThemeName;
      if (theme) setTheme(theme);
    });
  });
  // Wire up language toggle buttons
  document.querySelectorAll<HTMLElement>(".lang-toggle").forEach((btn) => {
    btn.addEventListener("click", () => {
      const lang = btn.getAttribute("data-lang") as Lang;
      if (lang) setLanguage(lang);
    });
  });
  // Auth check
  if (token && user) {
    showApp();
  }
});

// Expose functions to global scope for onclick handlers
Object.assign(window, {
  showRegister,
  showLogin,
  doLogin,
  doRegister,
  doLogout,
  showPage,
  showNewTaskModal,
  showNewArticleModal,
  handleQuickInput,
  handleQuickInputFromTasks,
  handleQuickInputFromArticles,
  viewTask,
  deleteTask,
  cancelResearch,
  retryResearch,
  viewArticle,
  deleteArticle,
  setLanguage,
  setTheme,
  t,
} as Record<string, unknown>);
