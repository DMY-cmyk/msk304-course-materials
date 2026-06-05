"""Build Pert. 8 deliverables: markdown -> pandoc (reference.docx) -> final docx."""
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(r"D:\DZAKI\S2\Sem. 1\Manajemen Strategik")
CONTENT = ROOT / "Dev Assistant" / "content" / "pert8"
REFERENCE = ROOT / "Dev Assistant" / "scripts" / "reference.docx"
PANDOC = r"C:\Program Files\Pandoc\pandoc.exe"

JOBS = [
    (CONTENT / "rmk.md",
     ROOT / "RMK" / "01079_Dzaki Muhammad Yusfian_RMK Pert. 8.docx"),
    (CONTENT / "cr13.md",
     ROOT / "Critical Thinking of the Article" / "01079_Dzaki Muhammad Yusfian_Artikel 13.docx"),
    (CONTENT / "cr14.md",
     ROOT / "Critical Thinking of the Article" / "01079_Dzaki Muhammad Yusfian_Artikel 14.docx"),
]


def build(src: Path, dst: Path) -> None:
    cmd = [
        PANDOC, str(src), "-o", str(dst),
        "--reference-doc", str(REFERENCE),
        "--from", "markdown+implicit_figures",
        # image refs are written relative to content/ (e.g. ../temp/...), so the
        # search path must include content/ itself for `..` to land on Dev Assistant/
        "--resource-path", f"{CONTENT};{CONTENT.parent}",
    ]
    subprocess.run(cmd, check=True)
    print(f"built {dst.name} ({dst.stat().st_size:,} bytes)")


if __name__ == "__main__":
    for src, dst in JOBS:
        build(src, dst)
