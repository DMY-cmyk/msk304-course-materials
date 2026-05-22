from translate_gamble.glossary import mask, unmask, GLOSSARY_VERSION


def test_glossary_version_is_string():
    assert isinstance(GLOSSARY_VERSION, str)
    assert len(GLOSSARY_VERSION) > 0


def test_mask_replaces_known_term_with_sentinel():
    masked, mapping = mask("A firm needs a competitive advantage.")
    assert "competitive advantage" not in masked.lower()
    assert "§T" in masked
    assert len(mapping) == 1


def test_mask_handles_longest_match_first():
    # "competitive advantage" must be masked as one unit, not "competitive" first
    masked, mapping = mask("competitive advantage is core")
    assert len(mapping) == 1
    only_value = next(iter(mapping.values()))
    assert only_value.lower() == "competitive advantage"


def test_mask_is_case_insensitive_but_preserves_original():
    masked, mapping = mask("Competitive Advantage matters.")
    assert len(mapping) == 1
    assert next(iter(mapping.values())) == "Competitive Advantage"


def test_unmask_restores_terms_and_reports_italic_spans():
    masked, mapping = mask("Use SWOT and value chain analysis.")
    # Simulate translator output: same sentinels, Indonesian words around
    translated = masked.replace("Use", "Gunakan").replace("and", "dan").replace("analysis", "analisis")
    text, spans = unmask(translated, mapping)
    assert "SWOT" in text
    assert "value chain" in text
    assert "§T" not in text
    # Two italic spans, one per term, both within text bounds
    assert len(spans) == 2
    for start, end in spans:
        assert 0 <= start < end <= len(text)


def test_unmask_handles_unused_sentinels_gracefully():
    # If translator drops a sentinel, unmask must not crash
    masked, mapping = mask("strategy and SWOT")
    text, spans = unmask("strategi dan", mapping)
    assert "§T" not in text
    # At most one span (the surviving one); zero is also acceptable
    assert len(spans) <= 1


def test_mask_does_not_break_word_boundaries():
    # "strategist" must NOT match "strategy"
    masked, mapping = mask("The strategist studies strategy.")
    assert "strategist" in masked
    assert len(mapping) == 1
    assert next(iter(mapping.values())).lower() == "strategy"
