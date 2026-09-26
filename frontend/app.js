"use strict";
/// <reference path="types.ts" />
const I18N = {
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
        "auth.usernameTooShort": "用户名至少需要3个字符",
        "auth.usernameInvalidChars": "用户名只能包含字母、数字、下划线或中文",
        "auth.emailInvalid": "请输入有效的邮箱地址",
        "auth.passwordTooShort": "密码至少需要6个字符",
        "auth.fullNameTooLong": "姓名不能超过100个字符",
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
        "tasks.researchCancelled": "研究已终止",
        "tasks.researchCancelledDesc": "该研究任务已被手动终止。",
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
        "auth.usernameTooShort": "Username must be at least 3 characters",
        "auth.usernameInvalidChars": "Username can only contain letters, numbers, underscores or Chinese characters",
        "auth.emailInvalid": "Please enter a valid email address",
        "auth.passwordTooShort": "Password must be at least 6 characters",
        "auth.fullNameTooLong": "Name cannot exceed 100 characters",
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
        "tasks.researchCancelled": "Research Terminated",
        "tasks.researchCancelledDesc": "This research task has been manually terminated.",
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
let currentLang = localStorage.getItem("lang") || "zh";
function t(key, params) {
    const dict = I18N[currentLang];
    let text = dict[key];
    if (text === undefined)
        return key;
    if (params) {
        for (const [k, v] of Object.entries(params)) {
            text = text.replace(`{${k}}`, String(v));
        }
    }
    return text;
}
function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem("lang", lang);
    // Update document lang attribute
    document.documentElement.lang = lang === "zh" ? "zh-CN" : "en-US";
    // Update lang-toggle active states
    document.querySelectorAll(".lang-toggle").forEach((btn) => {
        const btnLang = btn.getAttribute("data-lang");
        btn.classList.toggle("active", btnLang === lang);
    });
    // Update all data-i18n elements
    applyI18nToDOM();
    // Re-render current page
    if (currentPage)
        showPage(currentPage);
    // Update sidebar user info
    updateSidebarUser();
}
function applyI18nToDOM() {
    // Update text content for elements with data-i18n
    document.querySelectorAll("[data-i18n]").forEach((el) => {
        const key = el.getAttribute("data-i18n");
        if (key) {
            el.textContent = t(key);
        }
    });
    // Update placeholders for inputs with data-i18n-placeholder
    document.querySelectorAll("[data-i18n-placeholder]").forEach((el) => {
        const key = el.getAttribute("data-i18n-placeholder");
        if (key && (el instanceof HTMLInputElement || el instanceof HTMLTextAreaElement)) {
            el.placeholder = t(key);
        }
    });
    // Update document title
    document.title = t("app.title");
}
let currentTheme = localStorage.getItem("theme") || "dark";
function setTheme(theme) {
    currentTheme = theme;
    localStorage.setItem("theme", theme);
    document.documentElement.setAttribute("data-theme", theme);
    // Update theme switcher active state
    document.querySelectorAll(".theme-dot").forEach((dot) => {
        const dotTheme = dot.getAttribute("data-theme-val");
        dot.classList.toggle("active", dotTheme === theme);
        dot.setAttribute("aria-pressed", String(dotTheme === theme));
    });
}
function initTheme() {
    setTheme(currentTheme);
}
// ====== Application State ======
const API = "http://localhost:8000/api";
let token = localStorage.getItem("token") || "";
let user = null;
let currentPage = "dashboard";
// Restore user from localStorage
try {
    const stored = localStorage.getItem("user");
    if (stored)
        user = JSON.parse(stored);
}
catch { /* ignore */ }
// ====== Auth ======
function showRegister() {
    document.getElementById("loginCard").classList.add("hidden");
    document.getElementById("registerCard").classList.remove("hidden");
}
function showLogin() {
    document.getElementById("registerCard").classList.add("hidden");
    document.getElementById("loginCard").classList.remove("hidden");
}
function showErr(id, msg) {
    const el = document.getElementById(id);
    el.textContent = msg;
    el.style.display = "block";
}
function showFieldError(fieldId, groupId, msg) {
    const fieldEl = document.getElementById(fieldId);
    const groupEl = document.getElementById(groupId);
    fieldEl.textContent = msg;
    fieldEl.classList.add("show");
    groupEl.classList.add("has-error");
}
function clearFieldError(fieldId, groupId) {
    const fieldEl = document.getElementById(fieldId);
    const groupEl = document.getElementById(groupId);
    fieldEl.textContent = "";
    fieldEl.classList.remove("show");
    groupEl.classList.remove("has-error");
}
function clearAllErrors(formPrefix, fieldNames) {
    // Clear banner
    const banner = document.getElementById(formPrefix + "Error");
    if (banner) {
        banner.textContent = "";
        banner.style.display = "none";
    }
    // Clear per-field errors
    for (const name of fieldNames) {
        clearFieldError(formPrefix + name + "Error", formPrefix + name + "Group");
    }
    // Also remove has-error from any other groups
    document.querySelectorAll(".form-group.has-error").forEach((el) => {
        el.classList.remove("has-error");
    });
}
/**
 * Parse API error response — handles both FastAPI 422 (array detail) and
 * regular errors (string detail). Returns a human-readable message.
 */
async function parseApiError(r) {
    try {
        const body = await r.json();
        // FastAPI 422: detail is an array of {loc, msg, type} objects
        if (Array.isArray(body.detail)) {
            return body.detail.map((e) => {
                const field = e.loc[e.loc.length - 1];
                return `${field}: ${e.msg}`;
            }).join("; ");
        }
        // Regular error: detail is a string
        if (typeof body.detail === "string")
            return body.detail;
        // Fallback: unknown format
        return JSON.stringify(body.detail || body);
    }
    catch {
        return `HTTP ${r.status}`;
    }
}
// ====== Client-Side Validation ======
const USERNAME_RE = /^[\w一-鿿㐀-䶿-]{3,50}$/;
const EMAIL_RE = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
function validateRegisterFields(username, email, password, full_name, prefix) {
    let valid = true;
    if (username.length < 3) {
        showFieldError(prefix + "UserError", prefix + "UserGroup", t("auth.usernameTooShort"));
        valid = false;
    }
    else if (!USERNAME_RE.test(username)) {
        showFieldError(prefix + "UserError", prefix + "UserGroup", t("auth.usernameInvalidChars"));
        valid = false;
    }
    if (!EMAIL_RE.test(email)) {
        showFieldError(prefix + "EmailError", prefix + "EmailGroup", t("auth.emailInvalid"));
        valid = false;
    }
    if (password.length < 6) {
        showFieldError(prefix + "PassError", prefix + "PassGroup", t("auth.passwordTooShort"));
        valid = false;
    }
    if (full_name.length > 100) {
        showFieldError(prefix + "NameError", prefix + "NameGroup", t("auth.fullNameTooLong"));
        valid = false;
    }
    return valid;
}
async function doLogin() {
    clearAllErrors("login", ["User", "Pass"]);
    const username = document.getElementById("loginUser").value.trim();
    const password = document.getElementById("loginPass").value;
    // Client-side validation
    if (!username) {
        showFieldError("loginUserError", "loginUserGroup", t("auth.fillAllFields"));
        return;
    }
    if (!password) {
        showFieldError("loginPassError", "loginPassGroup", t("auth.fillAllFields"));
        return;
    }
    try {
        const r = await fetch(`${API}/auth/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password }),
        });
        if (!r.ok) {
            const errMsg = await parseApiError(r);
            return showErr("loginError", errMsg || t("auth.loginFailed"));
        }
        const d = await r.json();
        token = d.access_token;
        user = d.user;
        localStorage.setItem("token", token);
        localStorage.setItem("user", JSON.stringify(user));
        showApp();
    }
    catch (e) {
        showErr("loginError", t("auth.connectionError", { msg: e.message }));
    }
}
async function doRegister() {
    clearAllErrors("reg", ["User", "Email", "Name", "Pass"]);
    const username = document.getElementById("regUser").value.trim();
    const email = document.getElementById("regEmail").value.trim();
    const full_name = document.getElementById("regName").value.trim();
    const password = document.getElementById("regPass").value;
    // Check required fields
    if (!username) {
        showFieldError("regUserError", "regUserGroup", t("auth.fillRequired"));
    }
    if (!email) {
        showFieldError("regEmailError", "regEmailGroup", t("auth.fillRequired"));
    }
    if (!password) {
        showFieldError("regPassError", "regPassGroup", t("auth.fillRequired"));
    }
    if (!username || !email || !password)
        return;
    // Format validation
    if (!validateRegisterFields(username, email, password, full_name, "reg"))
        return;
    try {
        const r = await fetch(`${API}/auth/register`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, email, full_name, password }),
        });
        if (!r.ok) {
            const errMsg = await parseApiError(r);
            return showErr("regError", errMsg || t("auth.registerFailed"));
        }
        const d = await r.json();
        token = d.access_token;
        user = d.user;
        localStorage.setItem("token", token);
        localStorage.setItem("user", JSON.stringify(user));
        showApp();
    }
    catch (e) {
        showErr("regError", t("auth.connectionError", { msg: e.message }));
    }
}
// ====== App Shell ======
function updateSidebarUser() {
    const avatar = document.getElementById("sidebarAvatar");
    const nameEl = document.getElementById("sidebarName");
    avatar.textContent = (user.full_name || user.username)[0].toUpperCase();
    nameEl.textContent = user.full_name || user.username;
}
function showApp() {
    document.getElementById("authPage").classList.add("hidden");
    document.getElementById("appLayout").classList.remove("hidden");
    updateSidebarUser();
    // Apply language setting
    document.documentElement.lang = currentLang === "zh" ? "zh-CN" : "en-US";
    applyI18nToDOM();
    const saved = localStorage.getItem("currentPage");
    const validPages = ["dashboard", "tasks", "articles", "knowledge"];
    showPage(saved && validPages.includes(saved) ? saved : "dashboard");
}
function doLogout() {
    token = "";
    user = null;
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    localStorage.removeItem("currentPage");
    document.getElementById("authPage").classList.remove("hidden");
    document.getElementById("appLayout").classList.add("hidden");
}
function showPage(page) {
    // Clean up any active SSE connection before navigating away
    disconnectSSE();
    currentPage = page;
    localStorage.setItem("currentPage", page);
    document.querySelectorAll(".nav-item").forEach((n) => n.classList.remove("active"));
    const activeNav = document.querySelector(`.nav-item[data-page="${page}"]`);
    if (activeNav)
        activeNav.classList.add("active");
    const mc = document.getElementById("mainContent");
    switch (page) {
        case "dashboard":
            renderDashboard(mc);
            break;
        case "tasks":
            renderTasks(mc);
            break;
        case "articles":
            renderArticles(mc);
            break;
        case "knowledge":
            renderKnowledge(mc);
            break;
    }
}
// ====== API Helper ======
async function api(path, opts = {}) {
    const h = {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
        ...(opts.headers || {}),
    };
    const r = await fetch(`${API}${path}`, { ...opts, headers: h });
    if (r.status === 401) {
        doLogout();
        throw new Error(t("general.unauthorized"));
    }
    return r;
}
// ====== Dashboard ======
async function renderDashboard(mc) {
    mc.innerHTML = `<div class="loading"><div class="spinner"></div></div>`;
    try {
        const [tasksR, articlesR] = await Promise.all([
            api("/research/?limit=100"),
            api("/articles/?limit=100"),
        ]);
        const tasksData = await tasksR.json();
        const articles = await articlesR.json();
        const taskList = tasksData.tasks || tasksData || [];
        const total = taskList.length;
        const completed = taskList.filter((t) => t.status === "完成").length;
        const running = taskList.filter((t) => t.status !== "完成" && t.status !== "失败" && t.status !== "已终止").length;
        mc.innerHTML =
            `<div class="page-header"><h1>${t("dashboard.title")}</h1><p>${t("dashboard.welcome", { name: esc(user.full_name || user.username) })}</p></div>` +
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
    }
    catch (e) {
        mc.innerHTML = `<div class="empty-state"><h3>${t("general.error")}</h3><p>${e.message}</p></div>`;
    }
}
// ====== Natural Chinese Input ======
async function handleQuickInputGeneric(inputId, btnId, btnRestoreText, showAlerts = false) {
    const input = document.getElementById(inputId);
    const btn = document.getElementById(btnId);
    const text = input.value.trim();
    if (!text)
        return;
    btn.textContent = t("dashboard.analyzing");
    btn.disabled = true;
    try {
        const r = await api("/ai/parse-input", {
            method: "POST",
            body: JSON.stringify({ text }),
        });
        const result = await r.json();
        if (result.action === "research") {
            const payload = result.payload;
            const taskR = await api("/research/", {
                method: "POST",
                body: JSON.stringify(payload),
            });
            const task = await taskR.json();
            input.value = "";
            // Navigate directly to the streaming task view — the SSE stream starts the research
            viewTask(task.id);
        }
        else {
            const payload = result.payload;
            await api("/articles/", {
                method: "POST",
                body: JSON.stringify(payload),
            });
            showPage("articles");
            input.value = "";
            if (showAlerts) {
                setTimeout(() => alert(`${t("articles.articleCreatedWithTitle", { title: payload.title })}\n${result.explanation}`), 300);
            }
        }
    }
    catch (e) {
        alert(t("general.error") + ": " + e.message);
    }
    finally {
        btn.textContent = btnRestoreText;
        btn.disabled = false;
    }
}
function handleQuickInput() {
    handleQuickInputGeneric("quickInput", "quickSubmitBtn", t("dashboard.start"), true);
}
function handleQuickInputFromTasks() {
    handleQuickInputGeneric("tasksQuickInput", "tasksQuickBtn", t("tasks.start"));
}
function handleQuickInputFromArticles() {
    handleQuickInputGeneric("articlesQuickInput", "articlesQuickBtn", t("articles.create"));
}
// Handle Enter key in quick input
document.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && document.activeElement?.id === "quickInput") {
        handleQuickInput();
    }
});
// ====== Task Rendering ======
function renderTaskList(tasks) {
    if (!tasks || tasks.length === 0)
        return `<div class="empty-state"><h3>${t("dashboard.noTasks")}</h3><p>${t("dashboard.noTasksDesc")}</p><button class="btn btn-primary" onclick="showNewTaskModal()">${t("dashboard.newResearch")}</button></div>`;
    const statusClass = {
        "待处理": "status-pending",
        "主题分解": "status-running",
        "搜索中": "status-running",
        "内容总结": "status-running",
        "报告生成": "status-running",
        "完成": "status-completed",
        "失败": "status-failed",
        "已终止": "status-cancelled",
    };
    return tasks
        .map((t) => {
        const sc = statusClass[t.status] || "status-pending";
        const progressHtml = t.status !== "完成" && t.status !== "失败" && t.status !== "已终止"
            ? `<div class="progress-bar"><div class="progress-fill" style="width:${(t.progress || 0) * 100}%"></div></div>`
            : "";
        return (`<div class="task-item" onclick="viewTask('${t.id}')">` +
            `<div class="task-left">` +
            `<div class="task-title">${esc(t.title)}</div>` +
            `<div class="task-meta"><span>${esc(t.topic).substring(0, 60)}</span><span>${new Date(t.created_at).toLocaleDateString()}</span></div>` +
            `</div>` +
            `<div class="task-right"><span class="status-badge ${sc}">${t.status}</span>${progressHtml}</div>` +
            `</div>`);
    })
        .join("");
}
async function renderTasks(mc) {
    mc.innerHTML = `<div class="loading"><div class="spinner"></div></div>`;
    try {
        const r = await api("/research/?limit=100");
        const d = await r.json();
        const tasks = d.tasks || d || [];
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
    }
    catch (e) {
        mc.innerHTML = `<div class="empty-state"><h3>${t("general.error")}</h3><p>${e.message}</p></div>`;
    }
}
// ====== Task Modal & Actions ======
function showNewTaskModal() {
    const overlay = document.createElement("div");
    overlay.className = "modal-overlay";
    overlay.innerHTML =
        `<div class="modal"><h3>${t("tasks.newTaskTitle")}</h3>` +
            `<div class="form-group"><label>${t("tasks.titleLabel")}</label><input id="ntTitle" placeholder="${t("tasks.titlePlaceholder")}"></div>` +
            `<div class="form-group"><label>${t("tasks.topicLabel")}</label><textarea id="ntTopic" rows="4" placeholder="${t("tasks.topicPlaceholder")}"></textarea></div>` +
            `<div class="form-group"><label>${t("tasks.notesLabel")}</label><textarea id="ntDesc" rows="2" placeholder="${t("tasks.notesPlaceholder")}"></textarea></div>` +
            `<div class="modal-actions"><button class="btn btn-secondary" id="cancelModalBtn">${t("tasks.cancel")}</button><button class="btn btn-primary" id="createTaskBtn">${t("tasks.startResearch")}</button></div></div>`;
    document.body.appendChild(overlay);
    overlay.querySelector("#cancelModalBtn").addEventListener("click", () => overlay.remove());
    overlay.querySelector("#createTaskBtn").addEventListener("click", () => createTask(overlay));
    overlay.addEventListener("click", (e) => { if (e.target === overlay)
        overlay.remove(); });
}
async function createTask(overlay) {
    const title = overlay.querySelector("#ntTitle").value.trim();
    const topic = overlay.querySelector("#ntTopic").value.trim();
    const description = overlay.querySelector("#ntDesc").value.trim();
    if (!title || !topic)
        return alert(t("tasks.titleRequired"));
    const btn = overlay.querySelector("#createTaskBtn");
    btn.textContent = t("tasks.creating");
    btn.disabled = true;
    try {
        const r = await api("/research/", {
            method: "POST",
            body: JSON.stringify({ title, topic, description }),
        });
        const task = await r.json();
        overlay.remove();
        // Navigate directly to the streaming task view — the SSE stream will start the research
        viewTask(task.id);
    }
    catch (e) {
        alert(t("general.error") + ": " + e.message);
        btn.textContent = t("tasks.startResearch");
        btn.disabled = false;
    }
}
async function viewTask(taskId) {
    const mc = document.getElementById("mainContent");
    mc.innerHTML = `<div class="loading"><div class="spinner"></div></div>`;
    try {
        const r = await api(`/research/${taskId}`);
        const tsk = await r.json();
        if (tsk.final_report) {
            const reportHtml = parseMarkdown(tsk.final_report);
            mc.innerHTML =
                `<div style="margin-bottom:16px"><button class="btn btn-secondary btn-sm" onclick="showPage('tasks')">${t("tasks.back")}</button></div>` +
                    `<div class="report-content">${reportHtml}</div>`;
            // Render LaTeX math formulas with KaTeX
            renderMathInReport(mc);
        }
        else if (tsk.status === "失败" || tsk.status === "已终止") {
            // Terminal error states — show error card
            const statusLabel = tsk.status === "失败" ? "status-failed" : "status-cancelled";
            const isCancelled = tsk.status === "已终止";
            let bodyContent = "";
            if (isCancelled) {
                bodyContent =
                    `<div class="empty-state" style="padding:32px 16px">` +
                        `<span class="empty-icon">⊘</span>` +
                        `<h3 style="color:var(--text-secondary)">${t("tasks.researchCancelled")}</h3>` +
                        `<p style="color:var(--text-secondary);margin-bottom:16px">${t("tasks.researchCancelledDesc")}</p>` +
                        `<button class="btn btn-primary btn-sm" onclick="retryResearch('${tsk.id}')">${t("tasks.retry")}</button>` +
                        `</div>`;
            }
            else {
                const errorMsg = tsk.metadata_json?.error || t("tasks.researchFailed");
                bodyContent =
                    `<div class="empty-state" style="padding:32px 16px">` +
                        `<span class="empty-icon">⚠</span>` +
                        `<h3 style="color:var(--danger)">${t("tasks.researchFailed")}</h3>` +
                        `<p style="color:var(--text-secondary);margin-bottom:8px">${t("tasks.researchFailedDesc")}</p>` +
                        (errorMsg ? `<p style="font-size:0.8rem;color:var(--text-tertiary);margin-bottom:16px">${esc(errorMsg)}</p>` : "") +
                        `<button class="btn btn-primary btn-sm" onclick="retryResearch('${tsk.id}')">${t("tasks.retry")}</button>` +
                        `</div>`;
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
                    `<div style="display:flex;gap:8px;margin-top:16px">` +
                    `<button class="btn btn-danger btn-sm" onclick="deleteTask('${tsk.id}')">${t("tasks.delete")}</button>` +
                    `</div>` +
                    `</div>`;
        }
        else {
            // Task is in progress — use SSE streaming view
            renderStreamingView(mc, tsk);
            connectResearchStream(tsk.id);
        }
    }
    catch (e) {
        mc.innerHTML = `<div class="empty-state"><h3>${t("general.error")}</h3><p>${e.message}</p></div>`;
    }
}
async function deleteTask(id) {
    if (!confirm(t("tasks.confirmDelete")))
        return;
    await api(`/research/${id}`, { method: "DELETE" });
    showPage("tasks");
}
async function cancelResearch(id) {
    if (!confirm(t("tasks.confirmCancel")))
        return;
    try {
        await api(`/research/${id}/cancel`, { method: "POST" });
        // Refresh the task view
        const mc = document.getElementById("mainContent");
        if (mc)
            viewTask(id);
    }
    catch (e) {
        alert(t("general.error") + ": " + e.message);
    }
}
async function retryResearch(id) {
    try {
        await api(`/research/${id}/run`, { method: "POST" });
        // Refresh the task view
        const mc = document.getElementById("mainContent");
        if (mc)
            viewTask(id);
    }
    catch (e) {
        alert(t("general.error") + ": " + e.message);
    }
}
// ====== Articles ======
async function renderArticles(mc) {
    mc.innerHTML = `<div class="loading"><div class="spinner"></div></div>`;
    try {
        const r = await api("/articles/?limit=100");
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
                        .map((a) => `<div class="article-card" onclick="viewArticle('${a.id}')">` +
                        `<div class="title">${esc(a.title)}</div>` +
                        `<div class="abstract">${esc(a.abstract || t("articles.noAbstract"))}</div>` +
                        `<div class="article-tags">` +
                        (a.keywords || []).map((k) => `<span class="tag">${esc(k)}</span>`).join("") +
                        `<span class="tag" style="background:var(--accent);color:#fff">${a.source_type}</span>` +
                        `</div>` +
                        `<div style="font-size:12px;color:var(--text2);margin-top:8px">${new Date(a.updated_at).toLocaleDateString()}</div>` +
                        `</div>`)
                        .join("")
                    : `<div class="empty-state"><h3>${t("articles.noArticles")}</h3><p>${t("articles.noArticlesDesc")}</p></div>`) +
                `</div>`;
    }
    catch (e) {
        mc.innerHTML = `<div class="empty-state"><h3>${t("general.error")}</h3><p>${e.message}</p></div>`;
    }
}
function showNewArticleModal() {
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
    overlay.querySelector("#cxlArt").addEventListener("click", () => overlay.remove());
    overlay.querySelector("#svArt").addEventListener("click", () => createArticle(overlay));
    overlay.addEventListener("click", (e) => { if (e.target === overlay)
        overlay.remove(); });
}
async function createArticle(overlay) {
    const title = overlay.querySelector("#naTitle").value.trim();
    const content = overlay.querySelector("#naContent").value.trim();
    const abstract = overlay.querySelector("#naAbstract").value.trim();
    const keywords = overlay.querySelector("#naKeywords").value
        .split(",")
        .map((k) => k.trim())
        .filter(Boolean);
    if (!title)
        return alert(t("articles.titleRequired"));
    const btn = overlay.querySelector("#svArt");
    btn.textContent = t("articles.saving");
    btn.disabled = true;
    try {
        await api("/articles/", {
            method: "POST",
            body: JSON.stringify({ title, content, abstract, keywords }),
        });
        overlay.remove();
        showPage("articles");
    }
    catch (e) {
        alert(t("general.error") + ": " + e.message);
        btn.textContent = t("articles.save");
        btn.disabled = false;
    }
}
async function viewArticle(id) {
    const mc = document.getElementById("mainContent");
    mc.innerHTML = `<div class="loading"><div class="spinner"></div></div>`;
    try {
        const r = await api(`/articles/${id}`);
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
    }
    catch (e) {
        mc.innerHTML = `<div class="empty-state"><h3>${t("general.error")}</h3><p>${e.message}</p></div>`;
    }
}
async function deleteArticle(id) {
    if (!confirm(t("articles.confirmDelete")))
        return;
    await api(`/articles/${id}`, { method: "DELETE" });
    showPage("articles");
}
// ====== Knowledge Graph ======
async function renderKnowledge(mc) {
    mc.innerHTML = `<div class="loading"><div class="spinner"></div></div>`;
    try {
        const r = await api("/articles/knowledge-nodes");
        const nodes = await r.json();
        mc.innerHTML =
            `<div class="page-header"><h1>${t("knowledge.title")}</h1><p>${t("knowledge.nodeCount", { count: nodes.length })}</p></div>` +
                `<div class="grid-2">` +
                (nodes.length
                    ? nodes
                        .map((n) => `<div class="card">` +
                        `<div class="card-title">${esc(n.title)}</div>` +
                        `<div style="font-size:13px;color:var(--text2);margin:8px 0">${esc(n.content).substring(0, 300)}</div>` +
                        `<div class="article-tags">` +
                        `<span class="tag">${n.node_type}</span>` +
                        `<span class="tag">${t("knowledge.confidence", { pct: Math.round(n.confidence * 100) })}</span>` +
                        `</div>` +
                        `</div>`)
                        .join("")
                    : `<div class="empty-state"><h3>${t("knowledge.noNodes")}</h3><p>${t("knowledge.noNodesDesc")}</p></div>`) +
                `</div>`;
    }
    catch (e) {
        mc.innerHTML = `<div class="empty-state"><h3>${t("general.error")}</h3><p>${e.message}</p></div>`;
    }
}
// ====== Markdown to HTML Parser ======
function parseMarkdown(md) {
    if (!md)
        return "";
    // Split into lines for block-level processing
    const lines = md.split("\n");
    const html = [];
    let i = 0;
    let inCodeBlock = false;
    let codeBlockContent = "";
    let codeBlockLang = "";
    let inTable = false;
    let tableRows = [];
    let tableAligns = [];
    let inList = null; // 'ul' | 'ol'
    function flushList() {
        if (inList) {
            html.push(`</${inList}>`);
            inList = null;
        }
    }
    function flushTable() {
        if (!inTable || tableRows.length === 0)
            return;
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
    function parseTableCellRow(line) {
        // | col1 | col2 | col3 |
        const trimmed = line.replace(/^\||\|$/g, "");
        return trimmed.split("|").map((c) => c.trim());
    }
    function isAlignRow(cells) {
        return cells.every((c) => /^:?-{3,}:?$/.test(c));
    }
    function getAligns(cells) {
        return cells.map((c) => {
            if (c.startsWith(":") && c.endsWith(":"))
                return "center";
            if (c.endsWith(":"))
                return "right";
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
            }
            else {
                // Close code block
                const langAttr = codeBlockLang ? ` class="language-${escHtml(codeBlockLang)}"` : "";
                html.push(`<pre><code${langAttr}>${escHtml(codeBlockContent).replace(/\n$/, "")}</code></pre>`);
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
            }
            else if (inTable && tableRows.length === 1 && isAlignRow(cells)) {
                tableAligns = getAligns(cells);
            }
            else {
                tableRows.push(cells);
            }
            i++;
            continue;
        }
        else if (inTable) {
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
            const qLines = [];
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
                if (inList)
                    flushList();
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
                if (inList)
                    flushList();
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
        const pLines = [];
        while (i < lines.length &&
            lines[i].trim() !== "" &&
            !/^```/.test(lines[i]) &&
            !/^\|.*\|$/.test(lines[i].trim()) &&
            !/^(-{3,}|\*{3,}|_{3,})\s*$/.test(lines[i].trim()) &&
            !/^(#{1,4})\s/.test(lines[i]) &&
            !/^>\s?/.test(lines[i]) &&
            !/^(\s*)[-*+]\s+/.test(lines[i]) &&
            !/^(\s*)\d+\.\s+/.test(lines[i])) {
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
function parseInline(text) {
    if (!text)
        return "";
    // ---- Protect LaTeX math blocks BEFORE any other processing ----
    // Otherwise Markdown syntax (_ * etc.) inside formulas corrupts the LaTeX.
    const mathBlocks = [];
    // Display math: $$...$$ (multi-line allowed)
    let out = text.replace(/\$\$([\s\S]*?)\$\$/g, (_m, formula) => {
        mathBlocks.push(`$$\n${formula.trim()}\n$$`);
        return `\x00MATH${mathBlocks.length - 1}\x00`;
    });
    // Inline math: $...$ (single line, non-empty)
    out = out.replace(/\$([^\$\n]+?)\$/g, (_m, formula) => {
        mathBlocks.push(`$${formula}$`);
        return `\x00MATH${mathBlocks.length - 1}\x00`;
    });
    // Escape HTML first
    out = escHtml(out);
    // Images (before links)
    out = out.replace(/!\[([^\]]*)\]\(([^)\s]+)(?:\s+"([^"]*)")?\)/g, (_m, alt, src, title) => {
        const t = title ? ` title="${escHtml(title)}"` : "";
        return `<img src="${escHtml(src)}" alt="${escHtml(alt)}"${t}>`;
    });
    // Links
    out = out.replace(/\[([^\]]+)\]\(([^)\s]+)(?:\s+"([^"]*)")?\)/g, (_m, text, url, title) => {
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
    // Restore math blocks (raw LaTeX in KaTeX-compatible delimiters)
    out = out.replace(/\x00MATH(\d+)\x00/g, (_m, idx) => {
        return mathBlocks[parseInt(idx)] || "";
    });
    return out;
}
function escHtml(s) {
    return s
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;");
}
function renderMathInReport(container) {
    // Use KaTeX auto-render if available
    const renderMath = window.renderMathInElement;
    if (typeof renderMath !== "function")
        return;
    const reportEl = container.querySelector(".report-content");
    if (!reportEl)
        return;
    try {
        renderMath(reportEl, {
            delimiters: [
                { left: "$$", right: "$$", display: true },
                { left: "$", right: "$", display: false },
            ],
            throwOnError: false,
        });
    }
    catch (_) {
        // KaTeX rendering failure is non-critical
    }
}
// ====== Utilities ======
function esc(s) {
    if (!s)
        return "";
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
    document.querySelectorAll(".theme-dot").forEach((dot) => {
        dot.addEventListener("click", () => {
            const theme = dot.getAttribute("data-theme-val");
            if (theme)
                setTheme(theme);
        });
    });
    // Wire up language toggle buttons
    document.querySelectorAll(".lang-toggle").forEach((btn) => {
        btn.addEventListener("click", () => {
            const lang = btn.getAttribute("data-lang");
            if (lang)
                setLanguage(lang);
        });
    });
    // Auth check
    if (token && user) {
        showApp();
    }
    // Real-time field error clearing on input
    const clearOnInput = (inputId, errorId, groupId) => {
        const input = document.getElementById(inputId);
        if (input) {
            input.addEventListener("input", () => clearFieldError(errorId, groupId));
        }
    };
    clearOnInput("loginUser", "loginUserError", "loginUserGroup");
    clearOnInput("loginPass", "loginPassError", "loginPassGroup");
    clearOnInput("regUser", "regUserError", "regUserGroup");
    clearOnInput("regEmail", "regEmailError", "regEmailGroup");
    clearOnInput("regName", "regNameError", "regNameGroup");
    clearOnInput("regPass", "regPassError", "regPassGroup");
});
// ====== SSE Streaming Client ======
// Track the active EventSource so we can clean up on navigation
let _activeEventSource = null;
let _watchdogTimer = null;
let _lastStreamEvent = 0; // timestamp of last phase/token event
function connectResearchStream(taskId) {
    // Clean up any existing connection
    disconnectSSE();
    // Build SSE URL with JWT as query param (EventSource cannot set headers)
    const streamToken = encodeURIComponent(token);
    const url = `${API}/research/${taskId}/stream?token=${streamToken}`;
    const es = new EventSource(url);
    _activeEventSource = es;
    _lastStreamEvent = Date.now();
    // Accumulate streaming text by source
    let streamedReport = "";
    let streamedSummary = "";
    // Watchdog: if no events for 120s, the research likely hung — check DB directly
    function resetWatchdog() {
        _lastStreamEvent = Date.now();
        if (_watchdogTimer)
            clearTimeout(_watchdogTimer);
        _watchdogTimer = window.setTimeout(async () => {
            // No event for 120s — check if task completed or failed
            const tsk = await checkTaskStatus(taskId);
            if (tsk && (tsk.status === "完成" || tsk.status === "失败" || tsk.status === "已终止")) {
                disconnectSSE();
                const mc = document.getElementById("mainContent");
                if (mc)
                    viewTask(taskId);
            }
            else if (tsk && tsk.status === "待处理") {
                // Task never started — show error
                const container = document.querySelector(".streaming-content");
                if (container) {
                    container.innerHTML +=
                        `<div class="empty-state" style="padding:16px"><span class="empty-icon">⚠</span><p>Research did not start — the server may be overloaded. Please retry.</p></div>`;
                }
                disconnectSSE();
            }
            // If task is still running (DECOMPOSING/SEARCHING/etc.), keep waiting
        }, 120000);
    }
    resetWatchdog();
    es.addEventListener("phase", (e) => {
        try {
            const data = JSON.parse(e.data);
            updateStreamPhase(data.progress, data.message || data.phase);
            resetWatchdog();
        }
        catch (_) { }
    });
    es.addEventListener("token", (e) => {
        try {
            const data = JSON.parse(e.data);
            if (data.source === "report") {
                streamedReport += data.text;
                renderStreamingMarkdown(streamedReport, false);
            }
            else if (data.source === "summary") {
                streamedSummary += data.text;
                renderStreamingSummary(streamedSummary);
            }
            resetWatchdog();
        }
        catch (_) { }
    });
    es.addEventListener("complete", (e) => {
        try {
            const data = JSON.parse(e.data);
            updateStreamPhase(data.progress, "Complete!");
            // Final render with KaTeX math
            renderStreamingMarkdown(streamedReport, true);
            disconnectSSE();
        }
        catch (_) { }
    });
    es.addEventListener("cancelled", () => {
        disconnectSSE();
        // Refresh the view to show cancelled card
        viewTask(taskId);
    });
    es.addEventListener("error", (e) => {
        // Custom "error" event from server (application-level error)
        try {
            const data = JSON.parse(e.data);
            const container = document.querySelector(".streaming-content");
            if (container) {
                container.innerHTML +=
                    `<div class="empty-state" style="padding:16px"><span class="empty-icon">⚠</span><p>${esc(data.message)}</p></div>`;
            }
            // Also show error in phase text
            const phaseEl = document.getElementById("streamPhase");
            if (phaseEl)
                phaseEl.textContent = "Error: " + data.message;
            disconnectSSE();
        }
        catch (_) { }
    });
    es.addEventListener("heartbeat", () => {
        // Keep-alive ping — no action needed (watchdog is reset by phase/token only)
    });
    // Handle connection errors (EventSource auto-reconnects by default)
    es.onerror = () => {
        // Check if task reached a terminal state while we were disconnected
        checkTaskCompleted(taskId).then((completed) => {
            if (completed) {
                disconnectSSE();
                viewTask(taskId);
            }
        });
    };
}
function disconnectSSE() {
    if (_watchdogTimer) {
        clearTimeout(_watchdogTimer);
        _watchdogTimer = null;
    }
    if (_activeEventSource) {
        _activeEventSource.close();
        _activeEventSource = null;
    }
}
async function checkTaskStatus(taskId) {
    try {
        const r = await api(`/research/${taskId}`);
        if (r.ok)
            return await r.json();
    }
    catch (_) { }
    return null;
}
async function checkTaskCompleted(taskId) {
    try {
        const r = await api(`/research/${taskId}`);
        if (r.ok) {
            const tsk = await r.json();
            return tsk.status === "完成" || !!tsk.final_report;
        }
    }
    catch (_) { }
    return false;
}
function renderStreamingView(container, task) {
    const progressPct = ((task.progress || 0) * 100).toFixed(0);
    container.innerHTML =
        `<div style="margin-bottom:16px">` +
            `<button class="btn btn-secondary btn-sm" onclick="showPage('tasks')">${t("tasks.back")}</button>` +
            `<button class="btn btn-danger btn-sm" onclick="cancelResearch('${task.id}')" style="margin-left:8px">${t("tasks.cancelResearch")}</button>` +
            `</div>` +
            `<div class="card">` +
            `<div class="card-header">` +
            `<span class="card-title">${esc(task.title)}</span>` +
            `<span class="status-badge status-running" id="streamStatus">${esc(task.status)}</span>` +
            `</div>` +
            `<p style="color:var(--text2);margin-bottom:4px"><strong>${t("tasks.topic")}</strong> ${esc(task.topic)}</p>` +
            `<div class="progress-bar-container">` +
            `<div class="progress-bar-fill" id="streamProgress" style="width:${progressPct}%"></div>` +
            `</div>` +
            `<div class="stream-phase-text" id="streamPhase"></div>` +
            `<div class="stream-report-container">` +
            `<div class="streaming-content report-content streaming-active" id="streamContent"></div>` +
            `</div>` +
            `</div>`;
}
function updateStreamPhase(progress, message) {
    const phaseEl = document.getElementById("streamPhase");
    const progressEl = document.getElementById("streamProgress");
    const statusEl = document.getElementById("streamStatus");
    if (phaseEl)
        phaseEl.textContent = message;
    if (progressEl) {
        progressEl.style.width = `${(progress * 100).toFixed(0)}%`;
    }
    // Update status badge text based on progress phase
    if (statusEl) {
        // Map progress to Chinese status label
        if (progress >= 1.0) {
            statusEl.textContent = "完成";
            statusEl.className = "status-badge status-completed";
        }
        else if (progress >= 0.85) {
            statusEl.textContent = "报告生成";
        }
        else if (progress >= 0.75) {
            statusEl.textContent = "内容总结";
        }
        else if (progress >= 0.05) {
            statusEl.textContent = "搜索中";
        }
        else {
            statusEl.textContent = "主题分解";
        }
    }
}
function renderStreamingMarkdown(mdText, isFinal) {
    const contentEl = document.getElementById("streamContent");
    if (!contentEl)
        return;
    const html = parseMarkdown(mdText);
    contentEl.innerHTML = html;
    // Auto-scroll to bottom
    const container = contentEl.parentElement;
    if (container) {
        container.scrollTop = container.scrollHeight;
    }
    // Render KaTeX only on final render (expensive)
    if (isFinal) {
        renderMathInReport(contentEl);
        contentEl.classList.remove("streaming-active");
    }
    else {
        contentEl.classList.add("streaming-active");
    }
}
function renderStreamingSummary(text) {
    // Summary text appears above the report during generation
    // For now, just log it — the report content is the primary display
    const phaseEl = document.getElementById("streamPhase");
    if (phaseEl && text.length < 200) {
        // Show short preview of summary in phase area
        phaseEl.textContent = text.slice(0, 100) + (text.length > 100 ? "..." : "");
    }
}
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
});
//# sourceMappingURL=app.js.map