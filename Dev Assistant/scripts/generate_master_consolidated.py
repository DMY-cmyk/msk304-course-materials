"""Build the MSK304 master consolidated study document."""
import subprocess
from pathlib import Path

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


if __name__ == "__main__":
    main()
