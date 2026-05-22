"""Build the MSK304 master consolidated study document."""
import re
import subprocess
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import RGBColor

BASE = Path(__file__).resolve().parent.parent  # Dev Assistant/
CONTENT = BASE / "content" / "master_consolidated"
TEMP = BASE / "temp"
TEMP.mkdir(exist_ok=True)
REFERENCE = BASE / "scripts" / "reference.docx"
OUTPUT = BASE.parent / "01079_Dzaki Muhammad Yusfian_Master Consolidated Study Document.docx"

# Order matters: front matter, Part I synthesis, Part II RMK 2-7, Part III CR 1-12
SECTIONS = [
    "00_front_matter.md",
    "01_part1_synthesis.md",
    "10_part2_pert2.md",
    "11_part2_pert3.md",
    "12_part2_pert4.md",
    "13_part2_pert5.md",
    "14_part2_pert6.md",
    "15_part2_pert7.md",
    "20_part3_art01.md",
    "21_part3_art02.md",
    "22_part3_art03.md",
    "23_part3_art04.md",
    "24_part3_art05.md",
    "25_part3_art06.md",
    "26_part3_art07.md",
    "27_part3_art08.md",
    "28_part3_art09.md",
    "29_part3_art10.md",
    "30_part3_art11.md",
    "31_part3_art12.md",
]

PAGE_BREAK = "\n\n\\newpage\n\n"

# Red bold phrases from PDF: "Pertanyaan pertama" through "ketujuh" appear in Ch.3 and Ch.4
# They are inline phrase openers that must be red bold (#EE0000)
PERTANYAAN_PHRASES = [
    "Pertanyaan pertama",
    "Pertanyaan kedua",
    "Pertanyaan ketiga",
    "Pertanyaan keempat",
    "Pertanyaan kelima",
    "Pertanyaan keenam",
    "Pertanyaan ketujuh",
]
_PERTANYAAN_PATTERN = re.compile(
    "|".join(re.escape(p) for p in PERTANYAAN_PHRASES)
)


def _set_run_color_red(run) -> None:
    """Set run font color to #EE0000 bold using direct XML manipulation."""
    run.bold = True
    rPr = run._r.get_or_add_rPr()
    # Remove any existing color element
    for existing_color in rPr.findall(qn('w:color')):
        rPr.remove(existing_color)
    color_elem = OxmlElement('w:color')
    color_elem.set(qn('w:val'), 'EE0000')
    color_elem.set(qn('w:themeColor'), 'none')
    rPr.append(color_elem)


def apply_red_pertanyaan(docx_path: Path) -> None:
    """
    Post-processing pass: find every paragraph containing a Pertanyaan phrase,
    SURGICALLY split the matching run so the exact phrase becomes red+bold while
    all other text and formatting in the paragraph is preserved unchanged.

    Algorithm: for each run that contains a match, split it into three runs
    (before / match / after) by manipulating XML in-place. The before and after
    runs inherit the original run's full rPr (bold, italic, font, etc.); the
    middle run inherits rPr + overrides color=EE0000 and ensures bold.
    """
    from copy import deepcopy

    doc = Document(str(docx_path))
    modified = 0

    for para in doc.paragraphs:
        if not _PERTANYAAN_PATTERN.search(para.text):
            continue

        # Snapshot the run list because we will mutate the XML by inserting siblings
        runs_snapshot = list(para.runs)
        for run in runs_snapshot:
            text = run.text
            if not text:
                continue
            m = _PERTANYAAN_PATTERN.search(text)
            if not m:
                continue

            before_text = text[:m.start()]
            match_text = text[m.start():m.end()]
            after_text = text[m.end():]

            # Original rPr (formatting properties of this run)
            original_rpr = run._element.find(qn('w:rPr'))

            # Modify original run -> "before" portion (preserves original formatting)
            run.text = before_text

            # Build middle run (red + bold), inheriting original rPr then overriding
            mid_run = OxmlElement('w:r')
            if original_rpr is not None:
                mid_rpr = deepcopy(original_rpr)
            else:
                mid_rpr = OxmlElement('w:rPr')
            # Strip any existing color
            for ex_color in mid_rpr.findall(qn('w:color')):
                mid_rpr.remove(ex_color)
            color_elem = OxmlElement('w:color')
            color_elem.set(qn('w:val'), 'EE0000')
            mid_rpr.append(color_elem)
            # Ensure bold is present (don't double-add)
            if mid_rpr.find(qn('w:b')) is None:
                mid_rpr.append(OxmlElement('w:b'))
            mid_run.append(mid_rpr)

            mid_t = OxmlElement('w:t')
            mid_t.set(qn('xml:space'), 'preserve')
            mid_t.text = match_text
            mid_run.append(mid_t)

            # Insert middle run immediately after the original run
            run._element.addnext(mid_run)

            # Build after run if there's trailing text, preserving original rPr
            if after_text:
                after_run = OxmlElement('w:r')
                if original_rpr is not None:
                    after_rpr = deepcopy(original_rpr)
                    after_run.append(after_rpr)
                after_t = OxmlElement('w:t')
                after_t.set(qn('xml:space'), 'preserve')
                after_t.text = after_text
                after_run.append(after_t)
                mid_run.addnext(after_run)

            modified += 1
            # In practice each paragraph has only one Pertanyaan phrase; stop after first match per run

    doc.save(str(docx_path))
    print(f"  apply_red_pertanyaan: {modified} phrase(s) colored red bold.")


def main() -> None:
    combined_path = TEMP / "master_consolidated.md"
    chunks: list[str] = []
    missing: list[str] = []

    for name in SECTIONS:
        path = CONTENT / name
        if not path.exists():
            missing.append(name)
            continue
        chunks.append(path.read_text(encoding="utf-8"))

    if missing:
        print(f"WARNING: {len(missing)} section file(s) missing — output will be partial:")
        for m in missing:
            print(f"  - {m}")

    combined_path.write_text(PAGE_BREAK.join(chunks), encoding="utf-8")
    print(f"Combined markdown written: {combined_path} ({combined_path.stat().st_size} bytes)")

    cmd = [
        "pandoc",
        str(combined_path),
        f"--reference-doc={REFERENCE}",
        "-o",
        str(OUTPUT),
    ]
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)
    print(f"Generated: {OUTPUT} ({OUTPUT.stat().st_size} bytes)")

    # Post-processing: apply red color to Pertanyaan phrases
    print("Applying post-processing: red Pertanyaan phrases...")
    apply_red_pertanyaan(OUTPUT)
    print(f"Final output: {OUTPUT} ({OUTPUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
