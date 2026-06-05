"""Phase-5 gates for Pert. 8: format, figures, identity, concept coverage."""
from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.shared import Mm

ROOT = Path(r"D:\DZAKI\S2\Sem. 1\Manajemen Strategik")
DOCS = {
    "rmk": ROOT / "RMK" / "01079_Dzaki Muhammad Yusfian_RMK Pert. 8.docx",
    "cr13": ROOT / "Critical Thinking of the Article" / "01079_Dzaki Muhammad Yusfian_Artikel 13.docx",
    "cr14": ROOT / "Critical Thinking of the Article" / "01079_Dzaki Muhammad Yusfian_Artikel 14.docx",
}
EXPECTED_IMAGES = {"rmk": 3, "cr13": 3, "cr14": 4}
# concept keyword gates per doc (lower-cased substring match on full text)
KEYWORDS = {
    "rmk": ["diamond", "multidomestik", "transnasional", "greenfield", "lisensi",
            "waralaba", "profit sanctuar", "subsidization", "dumping", "ctrip",
            "four seasons", "walgreens", "kurs", "bric", "ekspor",
            "akuisisi", "joint venture", "wheel", "honeywell", "suzuki",
            "home depot", "hofstede" ],
    "cr13": ["kostruba", "ukraina", "kopi", "jerman", "polandia", "hofstede",
             "internasionalisasi", "diaspora", "bab 7", "tpgs", "crowd"],
    "cr14": ["gregory", "cmo", "generatif", "cisco", "ikea", "agilitas",
             "tata kelola", "transnasional", "bab 7", "tpgs", "panel",
             "mini-hatcheries"],
}
# the RMK does not cover Hofstede (article concept, not Ch.7) — drop it there
KEYWORDS["rmk"].remove("hofstede")

checks: list[tuple[str, bool]] = []


def ok(label: str, cond: bool) -> None:
    checks.append((label, bool(cond)))
    print(("PASS " if cond else "FAIL ") + label)


for key, path in DOCS.items():
    d = Document(str(path))
    sec = d.sections[0]
    ok(f"{key}: file exists", path.exists())
    ok(f"{key}: A4 width 210mm", abs(sec.page_width - Mm(210)) < Mm(2))
    ok(f"{key}: A4 height 297mm", abs(sec.page_height - Mm(297)) < Mm(2))
    full = "\n".join(p.text for p in d.paragraphs).lower()
    ok(f"{key}: identity NIM 01079", "01079" in full)
    ok(f"{key}: identity name", "dzaki muhammad yusfian" in full)
    st = d.styles["Normal"]
    ok(f"{key}: Normal font Times New Roman", st.font.name == "Times New Roman")
    ok(f"{key}: Normal size 12pt", st.font.size is not None and st.font.size.pt == 12)
    ok(f"{key}: line spacing 1.5", st.paragraph_format.line_spacing == 1.5)
    n_img = len(d.inline_shapes)
    ok(f"{key}: embedded images == {EXPECTED_IMAGES[key]} (got {n_img})",
       n_img == EXPECTED_IMAGES[key])
    widths = [sh.width / 914400 for sh in d.inline_shapes]
    ok(f"{key}: image widths in (3.5, 6.11) in ({[round(w, 2) for w in widths]})",
       all(3.5 < w <= 6.11 for w in widths))
    missing = [k for k in KEYWORDS[key] if k not in full]
    ok(f"{key}: concept keywords (missing: {missing})", not missing)

n_fail = sum(1 for _, c in checks if not c)
report = ROOT / "analysis" / "pert8-validation.md"
lines = ["# Pert. 8 Validation Report\n", "## Automated gates\n"]
lines += [f"- {'✅' if c else '❌'} {label}" for label, c in checks]
lines.append(f"\n**Result: {len(checks) - n_fail}/{len(checks)} passed**")
report.write_text("\n".join(lines), encoding="utf-8")
print(f"\n{len(checks) - n_fail}/{len(checks)} passed -> {report}")
raise SystemExit(1 if n_fail else 0)
