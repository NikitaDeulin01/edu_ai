"""Markdown/HTML → безопасный HTML для Telegram (parse_mode=HTML)."""

from __future__ import annotations

import html
import re

from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message

_CODE_BLOCK = re.compile(r"```(\w*)\n?([\s\S]*?)```", re.DOTALL)
_INLINE_CODE = re.compile(r"`([^`\n]+)`")
_TABLE_SEP = re.compile(r"^\s*\|(?:\s*[:|\-]+\s*\|)+\s*$")
_HEADER = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)
_BOLD = re.compile(r"\*\*(.+?)\*\*")
_ITALIC = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")
_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_HTML_TAG = re.compile(r"<[^>]+>")


def format_for_telegram(text: str) -> str:
    raw = normalize_llm_output(text.strip())
    if not raw:
        return ""
    if _looks_like_markdown(raw):
        return sanitize_telegram_html(markdown_to_telegram_html(raw))
    if _looks_like_html(raw):
        return sanitize_telegram_html(raw)
    return sanitize_telegram_html(markdown_to_telegram_html(raw))


def normalize_llm_output(text: str) -> str:
    """Чистит типичный мусор от LLM перед форматированием."""
    work = html.unescape(text)
    work = re.sub(r"&#x[0-9a-fA-F]+;|&#[0-9]+;", lambda m: html.unescape(m.group(0)), work)
    # Линии из дефисов (docstring numpy) — убираем
    work = re.sub(r"^\s*[-=]{4,}\s*$", "", work, flags=re.M)
    # Секции docstring, которые LLM любит копировать
    work = re.sub(r"^\s*(Parameters|Returns|Raises|Yields)\s*$", "", work, flags=re.M | re.I)
    # Испорченные «табличные» буллеты с ·
    work = re.sub(r"^•\s+(.+)$", lambda m: _split_dot_bullet(m.group(1)), work, flags=re.M)
    return re.sub(r"\n{3,}", "\n\n", work).strip()


def _split_dot_bullet(line: str) -> str:
    if line.count("·") < 2:
        return "• " + line
    parts = [p.strip() for p in line.split("·") if p.strip()]
    return "\n".join("• " + p for p in parts)


def html_to_plain_for_llm(text: str) -> str:
    """Убирает HTML из текста урока, чтобы LLM отвечала Markdown, а не тегами."""
    work = text
    work = re.sub(r"<pre>\s*<code[^>]*>([\s\S]*?)</code>\s*</pre>", r"```\n\1\n```", work, flags=re.I)
    work = re.sub(r"<code>([\s\S]*?)</code>", r"`\1`", work, flags=re.I)
    work = re.sub(r"<b>([\s\S]*?)</b>", r"**\1**", work, flags=re.I)
    work = re.sub(r"<i>([\s\S]*?)</i>", r"*\1*", work, flags=re.I)
    work = re.sub(r"<br\s*/?>", "\n", work, flags=re.I)
    work = _HTML_TAG.sub("", work)
    work = html.unescape(work)
    return re.sub(r"\n{3,}", "\n\n", work).strip()


def sanitize_telegram_html(text: str) -> str:
    """Приводит HTML к тегам, которые принимает Telegram."""
    work = text
    # Telegram: для блока кода — только <pre>, без вложенного <code>
    work = re.sub(
        r"<pre>\s*<code[^>]*>([\s\S]*?)</code>\s*</pre>",
        lambda m: "<pre>" + _escape_pre_content(m.group(1)) + "</pre>",
        work,
        flags=re.I,
    )
    work = re.sub(r"<code>\s*<pre>([\s\S]*?)</pre>\s*</code>", r"<pre>\1</pre>", work, flags=re.I)
    # Лишние теги → убираем
    work = re.sub(r"</?(?:div|span|p|ul|ol|li|h[1-6]|blockquote|br)\b[^>]*>", "\n", work, flags=re.I)
    # Неподдерживаемые теги вырезаем, содержимое оставляем
    work = re.sub(
        r"</?(?!b>|/b|strong>|/strong|i>|/i|em>|/em|u>|/u|ins>|/ins|s>|/s|strike>|/strike|del>|/del|code>|/code|pre>|/pre|a\s|/a>)[a-z][^>]*>",
        "",
        work,
        flags=re.I,
    )
    work = _fix_unescaped_ampersand(work)
    return re.sub(r"\n{3,}", "\n\n", work).strip()


def _escape_pre_content(content: str) -> str:
    plain = html.unescape(content)
    return html.escape(plain, quote=False)


def _fix_unescaped_ampersand(text: str) -> str:
    parts = re.split(r"(<[^>]+>)", text)
    out: list[str] = []
    for part in parts:
        if part.startswith("<") and part.endswith(">"):
            out.append(part)
        else:
            out.append(re.sub(r"&(?!amp;|lt;|gt;|quot;)", "&amp;", part))
    return "".join(out)


def _looks_like_html(text: str) -> bool:
    return bool(re.search(r"<(?:b|i|code|pre|a|strong|em)\b", text, re.I))


def _looks_like_markdown(text: str) -> bool:
    return bool("```" in text or "**" in text or _HEADER.search(text) or _has_table(text))


def _has_table(text: str) -> bool:
    lines = text.splitlines()
    for i, ln in enumerate(lines[:-1]):
        if ln.count("|") >= 2 and _TABLE_SEP.match(lines[i + 1]):
            return True
    return False


def markdown_to_telegram_html(text: str) -> str:
    code_blocks: list[str] = []
    inline_codes: list[str] = []

    def store_codeblock(match: re.Match) -> str:
        body = _escape_pre_content(match.group(2).strip("\n"))
        code_blocks.append(f"<pre>{body}</pre>")
        return f"\x00CB{len(code_blocks) - 1}\x00"

    def store_inline(match: re.Match) -> str:
        inline_codes.append(f"<code>{html.escape(match.group(1), quote=False)}</code>")
        return f"\x00IC{len(inline_codes) - 1}\x00"

    work = _CODE_BLOCK.sub(store_codeblock, text)
    work = _INLINE_CODE.sub(store_inline, work)
    work = _convert_tables(work)
    work = _HEADER.sub(lambda m: f"\n<b>{html.escape(m.group(2).strip(), quote=False)}</b>\n", work)
    work = _LINK.sub(
        lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{html.escape(m.group(1), quote=False)}</a>',
        work,
    )
    work = _BOLD.sub(lambda m: f"<b>{html.escape(m.group(1), quote=False)}</b>", work)
    work = _ITALIC.sub(lambda m: f"<i>{html.escape(m.group(1), quote=False)}</i>", work)
    work = _format_lists(work)
    work = _escape_outside_tags(work)

    for i, block in enumerate(code_blocks):
        work = work.replace(f"\x00CB{i}\x00", block)
    for i, code in enumerate(inline_codes):
        work = work.replace(f"\x00IC{i}\x00", code)

    return re.sub(r"\n{3,}", "\n\n", work).strip()


def _convert_tables(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        if lines[i].count("|") >= 2 and i + 1 < len(lines) and _TABLE_SEP.match(lines[i + 1]):
            headers = _parse_table_row(lines[i])
            i += 2
            while i < len(lines) and "|" in lines[i]:
                cells = _parse_table_row(lines[i])
                if headers and cells:
                    row = " · ".join(f"{h}: {c}" for h, c in zip(headers, cells) if h or c)
                    out.append(f"• {row}")
                elif cells:
                    out.append("• " + " · ".join(c for c in cells if c))
                i += 1
            out.append("")
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def _parse_table_row(line: str) -> list[str]:
    return [p.strip() for p in line.strip().strip("|").split("|") if p.strip()]


def _format_lists(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("- ") or stripped.startswith("* "):
            out.append("• " + stripped[2:].strip())
        else:
            out.append(line)
    return "\n".join(out)


def _escape_outside_tags(text: str) -> str:
    parts = re.split(r"(<[^>]+>|\x00(?:CB|IC)\d+\x00)", text)
    result: list[str] = []
    for part in parts:
        if not part:
            continue
        if part.startswith("<") or part.startswith("\x00"):
            result.append(part)
        else:
            plain = html.unescape(part)
            result.append(html.escape(plain, quote=False))
    return "".join(result)


def split_html_for_telegram(text: str, limit: int = 3800) -> list[str]:
    if len(text) <= limit:
        return [text] if text else []
    chunks: list[str] = []
    current = ""
    for block in re.split(r"\n\n+", text):
        block = block.strip()
        if not block:
            continue
        piece = block if not current else f"{current}\n\n{block}"
        if len(piece) <= limit:
            current = piece
            continue
        if current:
            chunks.append(current)
            current = ""
        if len(block) <= limit:
            current = block
        else:
            for line in block.splitlines(keepends=True):
                if len(current) + len(line) > limit:
                    if current:
                        chunks.append(current.strip())
                    current = line
                else:
                    current += line
            if current:
                chunks.append(current.strip())
                current = ""
    if current:
        chunks.append(current.strip())
    return [c for c in chunks if c]


async def answer_html(message: Message, text: str) -> None:
    """Отправка с форматированием; при ошибке парсинга — повтор после sanitize."""
    formatted = format_for_telegram(text)
    for chunk in split_html_for_telegram(formatted):
        await _send_html_chunk(message, chunk)


async def _send_html_chunk(message: Message, chunk: str) -> None:
    for attempt in (chunk, sanitize_telegram_html(chunk)):
        try:
            await message.answer(attempt, parse_mode=ParseMode.HTML)
            return
        except TelegramBadRequest:
            continue
    plain = _HTML_TAG.sub("", html.unescape(chunk))
    await message.answer(plain)
