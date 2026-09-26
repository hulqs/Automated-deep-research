---
name: Image Agent Skill
description: 学术报告图像增强智能体。分析源材料中是否存在图片、图表或插图，仅在源材料明确包含图片时才为报告添加图像。从 Wikimedia Commons 获取 CC 许可图片并嵌入 Markdown 报告。
---

# Image Agent（图像增强智能体）

**Agent 6** — 报告图像增强器。遵循「宁缺毋滥」原则：仅当源材料明确包含或引用图片时，才为报告添加图像。不要装饰性图片，每张图必须有学术价值。

## 设计原则

> **宁缺毋滥 — better no image than an irrelevant one**

1. **有据可查**：仅当源材料中明确包含或引用了图片/图表/插图时才建议添加
2. **学术价值**：每张图片必须有助于理解报告内容——解释概念、展示数据、说明方法或呈现框架
3. **来源可追溯**：每个 placement 必须标注图片来源 URL 或标题
4. **0-4 张图片**：零张是完全正确的答案，不要为了填充而建议图片
5. **不发明图片**：搜索查询必须源自实际源材料的术语

## 三阶段流水线

### 阶段 1：识别图片位置 (`identify_image_placements`)

LLM 分析报告内容和源材料，识别适合放置图片的位置。

```json
{
    "placements": [
        {
            "section_title": "报告中确切的章节标题",
            "position_after": "用于定位插入点的文本摘录",
            "caption": "学术描述性图注（注明图片来源）",
            "search_query": "从源材料派生的搜索关键词",
            "visual_type": "photo|diagram|chart|infographic|map|illustration",
            "importance": "high|medium|low",
            "source_reference": "包含此图片的源 URL 或标题"
        }
    ]
}
```

**关键规则**：
- 报告截断至 4000 字符
- 源材料截断至 30 条，每条 snippet 200 字符
- 使用 `temperature=0.2` 确保保守判断
- 过滤掉没有 `source_reference` 的 placement

### 阶段 2：获取图片 (`fetch_images_for_placements`)

为每个 placement 从 Wikimedia Commons 搜索图片。

- 每次搜索返回最多 3 张图片（`thumb_width=800`）
- 选质量最佳的图片作为主图
- 提供最多 2 张备选图片（`alternatives`）
- **找不到图片则跳过**——不使用占位符

```python
# 返回的 enriched placement 增加字段：
{
    "image_url": "https://upload.wikimedia.org/...",
    "image_source": "wikimedia",
    "image_license": "CC BY-SA 4.0",
    "image_attribution": "作者名",
    "image_title": "图片标题",
    "image_width": 800,
    "image_height": 400,
    "alternatives": [{"url": "...", "title": "..."}, ...]
}
```

### 阶段 3：嵌入报告 (`embed_images_in_report`)

将图片以 Markdown 格式插入报告。

**插入策略（按优先级）**：
1. **章节标题匹配**：在匹配的章节标题后立即插入
2. **内容摘录匹配**：在匹配 `position_after` 的行后插入
3. **最近章节回退**：在最近的章节标题附近插入
4. **参考文献前回退**：在参考文献章节前追加

**Markdown 输出格式**：
```markdown
![图注文本](图片URL)

*[Diagram] 描述性学术图注（注明来源）*
 图片来源: 作者名 | 许可: CC BY-SA 4.0 | 来源: Wikimedia
```

## 使用示例

```python
from app.agents.image_agent import ImageAgent

agent = ImageAgent(api_key="...", base_url="...", model="...")

# 阶段 1: 识别位置
placements = await agent.identify_image_placements(
    topic="量子计算",
    report_content=final_report,
    key_concepts=["量子比特", "量子门"],
    search_results=all_results,
)

# 阶段 2: 获取图片
enriched = await agent.fetch_images_for_placements(placements)

# 阶段 3: 嵌入报告
if enriched:
    final_report = await agent.embed_images_in_report(final_report, enriched)
```

## 容错设计

- ImageAgent 是整个流水线的**非关键阶段**
- 任何异常都会被捕获并记录警告，不会中断报告生成
- 编排器中的异常处理：
  ```python
  try:
      placements = await self.image_agent.identify_image_placements(...)
      # ... fetch and embed ...
  except Exception as e:
      logger.warning(f"Image enhancement skipped (non-critical): {e}")
  ```

## 技术实现

- 继承 `BaseAgent`
- 使用 `ImageSearchTool.search()` 搜索 Wikimedia Commons
- 插入算法使用辅助函数 `_is_section_header()`、`_line_contains_excerpt()`、`_find_best_insertion_point()`
- 图片格式化函数 `_format_image_markdown()` 生成完整 Markdown
- 日志记录每个 placement 的处理结果（成功/跳过/过滤）

## 相关技能

- [[report-agent]] — 提供待增强的 Markdown 报告
- [[deep-research]] — 编排器中的第六阶段（最后一步）
