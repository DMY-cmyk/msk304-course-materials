"""Stage 2: extracted JSON -> translated JSON with italic spans."""
from __future__ import annotations
import hashlib
import json
import re
import sqlite3
import time
from pathlib import Path
from typing import Any, Protocol

from translate_gamble.glossary import GLOSSARY_VERSION, mask, unmask

_SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s+")


class Translator(Protocol):
    def translate(self, text: str) -> str: ...


def chunk_text(text: str, max_len: int = 4500) -> list[str]:
    """Split text at sentence boundaries so no chunk exceeds max_len chars."""
    if len(text) <= max_len:
        return [text]
    sentences = _SENTENCE_END_RE.split(text)
    chunks: list[str] = []
    buf = ""
    for s in sentences:
        sep = " " if buf else ""
        if len(buf) + len(sep) + len(s) <= max_len:
            buf = buf + sep + s
        else:
            if buf:
                chunks.append(buf)
            while len(s) > max_len:
                chunks.append(s[:max_len])
                s = s[max_len:]
            buf = s
    if buf:
        chunks.append(buf)
    return chunks


class TranslationCache:
    """SQLite cache keyed by sha256(text + glossary_version)."""

    def __init__(self, db_path: Path, glossary_version: str) -> None:
        db_path.parent.mkdir(parents=True, exist_ok=True)
        self.glossary_version = glossary_version
        self.conn = sqlite3.connect(str(db_path))
        self.conn.execute(
            """CREATE TABLE IF NOT EXISTS translations(
                   key TEXT PRIMARY KEY,
                   text TEXT NOT NULL,
                   spans TEXT NOT NULL
               )"""
        )
        self.conn.commit()

    def _key(self, source_text: str) -> str:
        h = hashlib.sha256()
        h.update(self.glossary_version.encode("utf-8"))
        h.update(b"\x00")
        h.update(source_text.encode("utf-8"))
        return h.hexdigest()

    def get(self, source_text: str) -> tuple[str, list[tuple[int, int]]] | None:
        row = self.conn.execute(
            "SELECT text, spans FROM translations WHERE key=?",
            (self._key(source_text),),
        ).fetchone()
        if row is None:
            return None
        spans = [tuple(p) for p in json.loads(row[1])]
        return row[0], spans

    def put(self, source_text: str, translated_text: str, spans: list[tuple[int, int]]) -> None:
        self.conn.execute(
            "INSERT OR REPLACE INTO translations(key, text, spans) VALUES(?,?,?)",
            (self._key(source_text), translated_text, json.dumps(spans)),
        )
        self.conn.commit()


def translate_block(
    text: str,
    *,
    cache: TranslationCache,
    translator: Translator,
    sleep_seconds: float = 0.0,
) -> tuple[str, list[tuple[int, int]]]:
    """Translate one block of text. Cached. Masks glossary terms first."""
    cached = cache.get(text)
    if cached is not None:
        return cached

    parts: list[str] = []
    span_accum: list[tuple[int, int]] = []
    offset = 0
    for chunk in chunk_text(text):
        masked, mapping = mask(chunk)
        try:
            translated = translator.translate(masked)
        except Exception:
            translated = None
        if sleep_seconds:
            time.sleep(sleep_seconds)
        # deep-translator returns None for empty / un-translatable input;
        # fall back to the masked source so the page still renders.
        if not translated:
            translated = masked
        restored, spans = unmask(translated, mapping)
        for s, e in spans:
            span_accum.append((s + offset, e + offset))
        parts.append(restored)
        offset += len(restored) + 1  # +1 for the joining space below
    out_text = " ".join(parts)
    cache.put(text, out_text, span_accum)
    return out_text, span_accum


def _make_google_translator():
    """Return a configured deep_translator.GoogleTranslator instance."""
    from deep_translator import GoogleTranslator
    return GoogleTranslator(source="en", target="id")


def translate_pages(extracted_dir: Path, out_dir: Path, cache_dir: Path) -> None:
    """Translate every page_*.json in extracted_dir into out_dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    cache = TranslationCache(cache_dir / "translations.sqlite", GLOSSARY_VERSION)
    translator = _make_google_translator()

    page_files = sorted((extracted_dir / "pages").glob("page_*.json"))
    total = len(page_files)
    for idx, src in enumerate(page_files, start=1):
        payload = json.loads(src.read_text(encoding="utf-8"))
        for block in payload["blocks"]:
            if block["type"] == "image":
                continue
            original = block["text"]
            translated, spans = translate_block(
                original,
                cache=cache,
                translator=translator,
                sleep_seconds=0.2,
            )
            block["text"] = translated
            block["italic_spans"] = spans
        (out_dir / src.name).write_text(
            json.dumps(payload, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"[{idx}/{total}] {src.name}", flush=True)


if __name__ == "__main__":
    import sys
    base = Path("Dev Assistant/scripts/translate_gamble/build")
    extracted = Path(sys.argv[1]) if len(sys.argv) > 1 else base / "extracted"
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else base / "translated"
    cache = base / "cache"
    translate_pages(extracted, out, cache)
    print(f"Translated to {out}")
