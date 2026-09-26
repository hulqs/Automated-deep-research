"""
SSE (Server-Sent Events) event types and formatting utilities.

Used by the streaming research pipeline to emit structured events
that the frontend consumes via EventSource.
"""

import json
from enum import Enum


class SSEEventType(str, Enum):
    """SSE event type names sent to the frontend."""
    PHASE = "phase"           # Phase transition (decomposing/searching/...)
    PROGRESS = "progress"     # Numeric progress update
    TOKEN = "token"           # Streaming Markdown text chunk
    ERROR = "error"           # Non-fatal error/warning
    COMPLETE = "complete"     # Research finished successfully
    CANCELLED = "cancelled"   # Research was cancelled by user
    HEARTBEAT = "heartbeat"   # Keep-alive ping to prevent proxy timeout


def format_sse(event_type: str, data: dict | None = None, comment: str | None = None) -> str:
    """Format a single SSE message.

    Args:
        event_type: The SSE event name (e.g. "phase", "token").
        data: JSON-serializable dict for the data field.
        comment: Optional SSE comment (for keep-alive pings).

    Returns:
        A properly formatted SSE message string ending with \\n\\n.
    """
    if comment is not None:
        return f": {comment}\n\n"

    data_str = json.dumps(data or {}, ensure_ascii=False)
    return f"event: {event_type}\ndata: {data_str}\n\n"
