from translate_gamble.extract import classify_block, detect_chapter_start


def test_classify_block_large_font_is_heading_1():
    assert classify_block(text="STRATEGY", font_size=18.0, is_bold=True) == ("heading", 1)


def test_classify_block_medium_bold_is_heading_2():
    assert classify_block(text="Crafting the Strategy", font_size=14.0, is_bold=True) == ("heading", 2)


def test_classify_block_small_bold_caps_is_heading_3():
    assert classify_block(text="LEARNING OBJECTIVES", font_size=11.5, is_bold=True) == ("heading", 3)


def test_classify_block_bullet_is_list_item():
    assert classify_block(text="• rivalry among competitors", font_size=11.0, is_bold=False) == ("list_item", 0)


def test_classify_block_default_is_body():
    assert classify_block(text="A company's strategy is its game plan.", font_size=11.0, is_bold=False) == ("body", 0)


def test_classify_block_figure_caption():
    assert classify_block(text="FIGURE 1.2 The Five-Forces Model", font_size=10.0, is_bold=True) == ("caption", 0)


def test_detect_chapter_start_matches_chapter_header():
    assert detect_chapter_start("CHAPTER 1") == 1
    assert detect_chapter_start("3 EVALUATING A COMPANY'S EXTERNAL ENVIRONMENT") == 3
    assert detect_chapter_start("A company's strategy is its game plan.") is None


def test_detect_chapter_from_blocks_finds_giant_digit_and_uppercase_title():
    from translate_gamble.extract import detect_chapter_from_blocks
    # Minimal fake PyMuPDF blocks (lines->spans->text/size/flags=0)
    def block(text, size):
        return {"type": 0, "lines": [{"spans": [{"text": text, "size": size, "flags": 0}]}]}
    blocks = [
        block("14", 9.0),                                             # page num — ignored
        block("STRATEGY FORMULATION, EXECUTION, AND GOVERNANCE", 18.0),  # uppercase title
        block("2", 72.0),                                             # giant chapter digit
        block("Crafting and executing strategy ...", 11.0),
    ]
    assert detect_chapter_from_blocks(blocks) == 2


def test_detect_chapter_from_blocks_returns_none_for_body_page():
    from translate_gamble.extract import detect_chapter_from_blocks
    def block(text, size):
        return {"type": 0, "lines": [{"spans": [{"text": text, "size": size, "flags": 0}]}]}
    blocks = [
        block("A company's strategy is its game plan.", 11.0),
        block("Some more body text on a regular page.", 11.0),
    ]
    assert detect_chapter_from_blocks(blocks) is None


def test_detect_chapter_from_blocks_requires_both_signals():
    from translate_gamble.extract import detect_chapter_from_blocks
    def block(text, size):
        return {"type": 0, "lines": [{"spans": [{"text": text, "size": size, "flags": 0}]}]}
    # Only the giant digit, no uppercase title
    blocks = [block("5", 60.0), block("regular body", 11.0)]
    assert detect_chapter_from_blocks(blocks) is None
