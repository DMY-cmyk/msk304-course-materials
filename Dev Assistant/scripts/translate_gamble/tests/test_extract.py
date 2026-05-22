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
