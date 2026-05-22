from pathlib import Path
from translate_gamble.translate import TranslationCache, chunk_text, translate_block


def test_chunk_text_short_returns_single_chunk():
    assert chunk_text("Hello world.") == ["Hello world."]


def test_chunk_text_splits_at_sentence_boundaries():
    long_sentence = "This is one. " * 500  # ~6500 chars
    chunks = chunk_text(long_sentence, max_len=4500)
    assert len(chunks) >= 2
    assert all(len(c) <= 4500 for c in chunks)
    assert "".join(chunks).replace(" ", "") == long_sentence.replace(" ", "")


def test_translation_cache_stores_and_retrieves(tmp_path: Path):
    cache = TranslationCache(tmp_path / "c.sqlite", glossary_version="1.0.0")
    assert cache.get("hello") is None
    cache.put("hello", "halo", [(0, 4)])
    got = cache.get("hello")
    assert got is not None
    text, spans = got
    assert text == "halo"
    assert spans == [(0, 4)]


def test_translation_cache_invalidates_on_version_change(tmp_path: Path):
    db = tmp_path / "c.sqlite"
    c1 = TranslationCache(db, glossary_version="1.0.0")
    c1.put("hello", "halo", [])
    c2 = TranslationCache(db, glossary_version="2.0.0")
    assert c2.get("hello") is None


class FakeTranslator:
    def __init__(self, mapping: dict[str, str]) -> None:
        self.mapping = mapping
        self.calls = 0

    def translate(self, text: str) -> str:
        self.calls += 1
        return self.mapping.get(text, text)


def test_translate_block_masks_and_unmasks_using_glossary(tmp_path: Path):
    cache = TranslationCache(tmp_path / "c.sqlite", glossary_version="1.0.0")
    fake = FakeTranslator({})  # passthrough
    out_text, spans = translate_block(
        "A firm needs a strategy.", cache=cache, translator=fake
    )
    assert "strategy" in out_text
    assert len(spans) == 1


def test_translate_block_hits_cache_on_second_call(tmp_path: Path):
    cache = TranslationCache(tmp_path / "c.sqlite", glossary_version="1.0.0")
    fake = FakeTranslator({})
    translate_block("hello", cache=cache, translator=fake)
    translate_block("hello", cache=cache, translator=fake)
    assert fake.calls == 1  # second call served from cache
