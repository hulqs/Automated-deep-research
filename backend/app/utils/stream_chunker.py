"""
Markdown-aware streaming text chunker.

Splits a stream of LLM tokens into display-friendly chunks (20–80 chars)
while preserving Markdown syntax integrity. Never splits inside inline
formatting tokens like **bold**, *italic*, [links](url), `code`, $math$.
"""

import re
import logging

logger = logging.getLogger(__name__)

# Regex patterns for inline syntax that must NOT be split across chunks
# Each is a pair: (opening pattern, closing pattern) or a single toggle pattern
INLINE_PAIRS = [
    # Bold: **text** or __text__
    (re.compile(r'\*\*'), re.compile(r'\*\*')),
    (re.compile(r'__'), re.compile(r'__')),
    # Italic: *text* or _text_ (but not ** or __)
    (re.compile(r'(?<!\*)\*(?!\*)'), re.compile(r'(?<!\*)\*(?!\*)')),
    (re.compile(r'(?<!_)_(?!_)'), re.compile(r'(?<!_)_(?!_)')),
    # Strikethrough: ~~text~~
    (re.compile(r'~~'), re.compile(r'~~')),
    # Inline code: `text`
    (re.compile(r'`'), re.compile(r'`')),
    # Math: $text$ and $$text$$
    (re.compile(r'\$\$'), re.compile(r'\$\$')),
    (re.compile(r'\$'), re.compile(r'\$')),
]

# Link/image patterns — tracked separately because they have complex structure
# [text](url) — opening bracket [ tracked, closing is ](non-whitespace)
LINK_OPEN = re.compile(r'!?\[(?=\S)')

# HTML tags: <tag> and </tag>
HTML_TAG = re.compile(r'</?[a-zA-Z][a-zA-Z0-9]*(?:\s[^>]*)?>')

# Characters that indicate sentence endings in Chinese and English
SENTENCE_END = re.compile(r'[。！？\.\!\?]')

# Block-level starters: lines beginning with these mark block boundaries
BLOCK_STARTERS = re.compile(r'^[#\-\*>\|\d]')

# Table separator row pattern (|---|---|)
TABLE_SEP = re.compile(r'^\|?[\s\:\-\|]+\|?$')


class StreamChunker:
    """Accumulates streaming text and emits safe-to-display chunks.

    Usage:
        chunker = StreamChunker(min_chunk=20, max_chunk=80)
        for token in llm_stream:
            for chunk in chunker.feed(token):
                send_to_frontend(chunk)
        final = chunker.flush()
        if final:
            send_to_frontend(final)
    """

    def __init__(self, min_chunk: int = 20, max_chunk: int = 80):
        if min_chunk < 1:
            raise ValueError("min_chunk must be >= 1")
        if max_chunk < min_chunk:
            raise ValueError("max_chunk must be >= min_chunk")
        self.min_chunk = min_chunk
        self.max_chunk = max_chunk
        self.buffer = ""

    def feed(self, text: str) -> list[str]:
        """Feed raw text from the LLM stream. Returns ready-to-send chunks."""
        if not text:
            return []

        self.buffer += text
        chunks: list[str] = []

        # Emit chunks while buffer has enough content
        while len(self.buffer) >= self.min_chunk:
            split_pos = self._find_safe_split()

            if split_pos > 0:
                chunk = self.buffer[:split_pos]
                self.buffer = self.buffer[split_pos:].lstrip('\n')
                if chunk:
                    chunks.append(chunk)
            elif len(self.buffer) >= self.max_chunk:
                # Force split: find the last safe position within max_chunk
                split_pos = self._force_split()
                chunk = self.buffer[:split_pos]
                self.buffer = self.buffer[split_pos:]
                if chunk:
                    chunks.append(chunk)
            else:
                # Buffer is between min_chunk and max_chunk but no safe split found
                # Wait for more text
                break

        return chunks

    def flush(self) -> str:
        """Return all remaining buffered text. Call once at stream end."""
        remaining = self.buffer
        self.buffer = ""
        return remaining

    # ------------------------------------------------------------------
    # Internal: split-point discovery
    # ------------------------------------------------------------------

    def _find_safe_split(self) -> int:
        """Find the best safe split position in buffer, or -1 if none found.

        Priority order (scanning from min_chunk to end or max_chunk):
          1. Paragraph boundary (\\n\\n)
          2. Block-level line boundary (\\n before #, -, *, >, |, digit.)
          3. Sentence boundary (。, ！, ？, ., !, ?)
          4. Word boundary (space)
        Returns the position AFTER the boundary character(s), or -1.
        """
        end = max(self.min_chunk, 1)

        # Only search within the "searchable window":
        # from min_chunk to min(max_chunk * 2, len(buffer))
        search_start = self.min_chunk
        search_end = min(len(self.buffer), max(self.max_chunk * 3, self.min_chunk + 20))

        # Collect all candidate split positions
        candidates: list[tuple[int, int]] = []  # (position, priority) lower priority = better

        # Priority 1: Double newline (paragraph boundary)
        pos = self.buffer.find('\n\n', search_start)
        if pos != -1 and pos < search_end:
            candidates.append((pos + 2, 1))
        elif pos != -1:
            candidates.append((pos + 2, 1))

        # Priority 2: Newline followed by block-level starter or preceded by content
        for m in re.finditer(r'\n(?=[#\-\*>\|]|\d+\.)', self.buffer):
            pos = m.start()
            if search_start <= pos < search_end:
                candidates.append((pos + 1, 2))

        # Also consider single newlines that end a line of content
        for m in re.finditer(r'\n', self.buffer):
            pos = m.start()
            if search_start <= pos < search_end:
                # Make sure we're not inside a code span or other inline syntax
                if self._is_safe_at(pos):
                    candidates.append((pos + 1, 5))

        # Priority 3: Chinese sentence endings
        for ch in ('。', '！', '？'):
            pos = self.buffer.find(ch, search_start)
            while pos != -1 and pos < search_end:
                # Check that the next char is not alphanumeric (e.g. URLs, numbers)
                next_idx = pos + 1
                if next_idx >= len(self.buffer) or self.buffer[next_idx] in (' ', '\n', '\r', '」', '』', ')', '"', '\''):
                    candidates.append((pos + 1, 3))
                pos = self.buffer.find(ch, pos + 1)

        # Priority 3b: English sentence endings
        for ch in ('. ', '! ', '? '):
            pos = self.buffer.find(ch, search_start)
            while pos != -1 and pos < search_end:
                candidates.append((pos + 2, 3))
                pos = self.buffer.find(ch, pos + 1)

        # Priority 4: Space (word boundary)
        pos = self.buffer.find(' ', search_start)
        if pos != -1 and pos < search_end:
            candidates.append((pos + 1, 4))

        if not candidates:
            return -1

        # Sort by priority (lower = better), then by position (closer to min_chunk = better)
        candidates.sort(key=lambda x: (x[1], abs(x[0] - self.min_chunk)))

        best_pos, _ = candidates[0]

        # Only split if the position is safe (not inside inline syntax)
        if self._is_safe_at(best_pos - 1):
            return best_pos

        # Try fallback candidates in order
        for pos, pri in candidates:
            if self._is_safe_at(pos - 1):
                return pos

        return -1

    def _force_split(self) -> int:
        """Force a split at the best possible position within max_chunk.

        Tries: last newline, last sentence end, last space, then raw character split.
        """
        limit = min(self.max_chunk, len(self.buffer))

        # Try to find last newline within limit
        last_nl = self.buffer.rfind('\n', 0, limit)
        if last_nl >= self.min_chunk and self._is_safe_at(last_nl):
            return last_nl + 1

        # Try to find last sentence end within limit
        for m in re.finditer(r'[。！？\.\!\?]\s', self.buffer[:limit]):
            pos = m.start() + 1
            if pos >= self.min_chunk and self._is_safe_at(pos - 1):
                return pos

        # Try to find last space within limit
        last_space = self.buffer.rfind(' ', 0, limit)
        if last_space >= self.min_chunk and self._is_safe_at(last_space):
            return last_space + 1

        # Last resort: split at max_chunk, but check safe position
        if self._is_safe_at(limit - 1):
            return limit

        # Walk backward from limit to find first safe char
        for i in range(limit - 1, max(self.min_chunk, 1) - 1, -1):
            if self._is_safe_at(i):
                return i + 1

        # Absolute fallback: split at min_chunk
        return max(self.min_chunk, 1)

    # ------------------------------------------------------------------
    # Inline syntax tracking
    # ------------------------------------------------------------------

    def _is_safe_at(self, pos: int) -> bool:
        """Check if position `pos` is safe to split (not inside inline syntax).

        We walk through the buffer from the beginning, tracking which inline
        constructs are open. If we reach `pos` and nothing is open, it's safe.

        For performance with frequent calls, we only scan up to `pos`.
        """
        if pos < 0 or pos >= len(self.buffer):
            return True

        i = 0
        depth = {
            'bold': 0,        # ** or __
            'italic_ast': 0,  # * (single)
            'italic_us': 0,   # _ (single)
            'strike': 0,      # ~~
            'code': 0,        # `
            'math_double': 0, # $$
            'math_single': 0, # $
            'link_text': 0,   # [...] — opening bracket for link
            'image_text': 0,  # ![...] — opening bracket for image
        }

        while i <= pos:
            ch = self.buffer[i]

            # Handle backslash escape
            if ch == '\\' and i + 1 < len(self.buffer):
                i += 2
                continue

            # ** or __
            if ch in ('*', '_') and i + 1 < len(self.buffer) and self.buffer[i + 1] == ch:
                # Check it's not a list bullet (line start + space after)
                is_list_bullet = (i == 0 or self.buffer[i - 1] == '\n') and \
                                 (i + 2 < len(self.buffer) and self.buffer[i + 2] == ' ')
                if not is_list_bullet:
                    if depth['bold'] == 0:
                        depth['bold'] = 1
                    else:
                        depth['bold'] = 0
                i += 2
                continue

            # ~~
            if ch == '~' and i + 1 < len(self.buffer) and self.buffer[i + 1] == '~':
                depth['strike'] = 1 - depth['strike']
                i += 2
                continue

            # $$ (double dollar math)
            if ch == '$' and i + 1 < len(self.buffer) and self.buffer[i + 1] == '$':
                depth['math_double'] = 1 - depth['math_double']
                i += 2
                continue

            # $ (single dollar math - only if not inside double dollar)
            if ch == '$' and depth['math_double'] == 0:
                depth['math_single'] = 1 - depth['math_single']
                i += 1
                continue

            # ` (inline code — only toggle if not doubled and not tripled)
            if ch == '`':
                # Count consecutive backticks
                tick_count = 1
                while i + tick_count < len(self.buffer) and self.buffer[i + tick_count] == '`':
                    tick_count += 1
                if tick_count == 1:
                    depth['code'] = 1 - depth['code']
                i += tick_count
                continue

            # ![ or [ (link/image)
            if ch == '!':
                if i + 1 < len(self.buffer) and self.buffer[i + 1] == '[':
                    depth['image_text'] += 1
                    i += 2
                    continue
            if ch == '[':
                depth['link_text'] += 1
                i += 1
                continue

            # ]( — close link text, open URL
            if ch == ']':
                if i + 1 < len(self.buffer) and self.buffer[i + 1] == '(':
                    # Link text ended, URL begins; still "inside" the link
                    pass  # Don't change depth yet — link is still open
                else:
                    # ] without following ( — just a literal bracket
                    pass
                i += 1
                continue

            # ) — close link URL
            if ch == ')':
                if depth['link_text'] > 0:
                    depth['link_text'] -= 1
                elif depth['image_text'] > 0:
                    depth['image_text'] -= 1
                i += 1
                continue

            i += 1

        # Safe if no inline syntax is currently open
        total_depth = sum(abs(v) for v in depth.values())
        return total_depth == 0
