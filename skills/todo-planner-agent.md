---
name: TODO Planner Agent Skill
description: 学术研究 TODO 计划生成智能体。根据研究主题和已有发现，生成分阶段的、带优先级的研究计划，并通过自评估机制（评分 ≥ 7/10）确保计划质量，不达标则自动重试。
---

# TODO Planner Agent（研究计划智能体）

**Agent 4** — 研究路线图生成器。不仅生成计划，还会自评估计划质量，不达标时自动重试（最多 2 次），确保输出高质量的研究规划。

## 能力

- **分阶段规划**：将研究任务组织为多个逻辑阶段（Phase）
- **任务优先级**：每条 TODO 标注 `high` / `medium` / `low` 优先级
- **顺序编排**：通过 `order_index` 确保任务按合理顺序排列
- **覆盖全面**：包含文献综述、实验分析、写作、验证四类任务
- **自评估机制**：LLM 评估者从 4 个维度打分（1-10），<7 分自动重试
- **反馈驱动重试**：重试时携带具体问题和改进建议
- **语言感知**：中文输入则输出中文计划

## 自评估维度

| 维度 | 说明 |
|------|------|
| **主题相关性** | 计划任务是否直接针对核心研究主题？ |
| **需求覆盖** | 是否覆盖用户陈述的研究描述/目标？ |
| **结构完整性** | 是否包含文献综述、分析、写作、验证？ |
| **逻辑连贯性** | 任务顺序是否合理？阶段是否递进？ |

## 核心方法

### `generate_plan(topic, summary, gaps, feedback="") → dict`

生成研究 TODO 计划。支持携带反馈进行重试生成。

```json
{
    "plan_title": "Research Plan: 主题",
    "phases": [
        {
            "phase": "阶段名称",
            "todos": [
                {
                    "content": "具体任务描述",
                    "priority": "high|medium|low",
                    "order_index": 0
                }
            ]
        }
    ]
}
```

### `evaluate_plan(topic, description, plan) → dict`

评估计划质量。

```json
{
    "is_matching": true,
    "score": 8,
    "feedback": "",
    "issues": []
}
```

### `generate_plan_with_evaluation(topic, description, summary, gaps) → dict`

完整的生成-评估-重试循环（最多 2 次重试）。

```python
plan = await agent.generate_plan_with_evaluation(
    topic="量子计算在药物发现中的应用",
    description="探索应用场景和最新进展",
    summary=final_summary,
    gaps=all_gaps
)
```

## 重试流程

```
generate_plan()
    ↓
evaluate_plan() → score ≥ 7? → ✅ 返回计划
    ↓ 否
generate_plan(feedback=改进建议) → evaluate_plan() → ...
    ↓ 最多 2 次重试
返回最终计划（即使未达标）
```

## 数据持久化

在编排器中，生成的 TODO 项被保存为 `TodoItem` 数据库记录：

```python
TodoItem(
    task_id=task.id,
    content=f"[{phase['phase']}] {t['content']}",
    priority=t.get("priority", "medium"),
    order_index=t.get("order_index", 0),
)
```

## 技术实现

- 继承 `BaseAgent`
- 两个独立 System Prompt：`PLANNER_SYSTEM`（生成）+ `EVALUATOR_SYSTEM`（评估）
- 知识空白输入截断：最多 10 条，每条 topic + reason
- 摘要截断：2000 字符
- 计划文本截断：3000 字符（评估时）
- 结果归一化：确保缺失字段有合理默认值

## 相关技能

- [[summarization-agent]] — 提供研究摘要和知识空白
- [[report-agent]] — 将 TODO 计划嵌入报告
- [[deep-research]] — 编排器中的第四阶段
