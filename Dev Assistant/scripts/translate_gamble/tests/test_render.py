from pathlib import Path
from translate_gamble.render import italic_runs, render_to_docx


def test_italic_runs_no_spans_returns_single_plain_run():
    assert italic_runs("hello world", []) == [("hello world", False)]


def test_italic_runs_single_span_splits_into_three():
    runs = italic_runs("A is strategy here.", [(5, 13)])
    assert runs == [("A is ", False), ("strategy", True), (" here.", False)]


def test_italic_runs_two_spans():
    runs = italic_runs("Use SWOT and value chain.", [(4, 8), (13, 24)])
    assert runs == [
        ("Use ", False),
        ("SWOT", True),
        (" and ", False),
        ("value chain", True),
        (".", False),
    ]


def test_italic_runs_span_at_start():
    runs = italic_runs("strategy matters.", [(0, 8)])
    assert runs == [("strategy", True), (" matters.", False)]


def test_render_to_docx_smoke(tmp_path: Path):
    pages_dir = tmp_path / "translated"
    images_dir = tmp_path / "extracted" / "images"
    pages_dir.mkdir(parents=True)
    images_dir.mkdir(parents=True)
    import json
    (pages_dir / "page_001.json").write_text(json.dumps({
        "page": 1, "chapter": 1,
        "blocks": [
            {"type": "heading", "level": 1, "text": "BAB 1", "italic_spans": []},
            {"type": "body", "text": "Sebuah strategi adalah rencana.", "italic_spans": [(7, 15)]},
        ],
    }), encoding="utf-8")
    out = tmp_path / "out.docx"
    render_to_docx(pages_dir, images_dir, out)
    assert out.exists()
    from docx import Document
    doc = Document(str(out))
    texts = [p.text for p in doc.paragraphs]
    assert any("BAB 1" in t for t in texts)
    assert any("strategi" in t for t in texts)
