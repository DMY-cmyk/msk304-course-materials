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
    reconstruct its runs so that the exact phrase is colored red and bold.
    All other text in those paragraphs is left as-is.
    """
    doc = Document(str(docx_path))
    modified = 0

    for para in doc.paragraphs:
        full_text = para.text
        if not _PERTANYAAN_PATTERN.search(full_text):
            continue

        # Preserve existing run properties where possible
        # Strategy: collect all run text, find matches, rebuild
        # First, gather full text broken at run boundaries with their properties
        existing_runs = []
        for run in para.runs:
            existing_runs.append({
                "text": run.text,
                "bold": run.bold,
                "italic": run.italic,
                "underline": run.underline,
                "font_name": run.font.name,
                "font_size": run.font.size,
                "style": run.style,
            })

        # Clear all existing runs
        for run in para.runs:
            run.text = ""

        # Rebuild runs with colored Pertanyaan phrases
        last_end = 0
        for m in _PERTANYAAN_PATTERN.finditer(full_text):
            # Text before match - add as normal run
            before = full_text[last_end:m.start()]
            if before:
                r = para.add_run(before)
                # Try to inherit properties from first original run
                if existing_runs:
                    src = existing_runs[0]
                    if src["bold"] is not None:
                        r.bold = src["bold"]
                    if src["italic"]:
                        r.italic = src["italic"]

            # The match itself - add as RED BOLD run
            colored = para.add_run(full_text[m.start():m.end()])
            _set_run_color_red(colored)
            last_end = m.end()

        # Remainder after last match
        remainder = full_text[last_end:]
        if remainder:
            r = para.add_run(remainder)
            if existing_runs:
                src = existing_runs[0]
                if src["bold"] is not None:
                    r.bold = src["bold"]
                if src["italic"]:
                    r.italic = src["italic"]

        modified += 1

    doc.save(str(docx_path))
    print(f"  apply_red_pertanyaan: {modified} paragraph(s) colored red.")


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
