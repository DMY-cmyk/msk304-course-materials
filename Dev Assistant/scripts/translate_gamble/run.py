"""End-to-end orchestrator. Runs extract -> translate -> render with optional stage skipping."""
from __future__ import annotations
import argparse
from pathlib import Path

from translate_gamble.extract import extract_pdf
from translate_gamble.render import render_to_docx
from translate_gamble.translate import translate_pages


def main() -> None:
    parser = argparse.ArgumentParser(description="Gamble Ch1-7 EN -> ID pipeline")
    parser.add_argument(
        "--pdf", type=Path, default=Path("Temu 1-7 Buku Gamble.pdf"),
        help="Source PDF",
    )
    parser.add_argument(
        "--build-dir", type=Path,
        default=Path("Dev Assistant/scripts/translate_gamble/build"),
        help="Where to store intermediate artifacts",
    )
    parser.add_argument(
        "--out", type=Path,
        default=Path("Temu 1-7 Buku Gamble (Bahasa Indonesia).docx"),
        help="Final DOCX output path",
    )
    parser.add_argument(
        "--only-stage", choices=["extract", "translate", "render"],
        help="Run only this stage (assumes prior stages already produced their outputs)",
    )
    args = parser.parse_args()

    extracted = args.build_dir / "extracted"
    translated = args.build_dir / "translated"
    cache = args.build_dir / "cache"
    images = extracted / "images"

    run_extract = args.only_stage in (None, "extract")
    run_translate = args.only_stage in (None, "translate")
    run_render = args.only_stage in (None, "render")

    if run_extract:
        print(f"[1/3] Extracting {args.pdf} -> {extracted}")
        extract_pdf(args.pdf, extracted)
    if run_translate:
        print(f"[2/3] Translating -> {translated}")
        translate_pages(extracted, translated, cache)
    if run_render:
        print(f"[3/3] Rendering -> {args.out}")
        render_to_docx(translated, images, args.out)

    print("Done.")


if __name__ == "__main__":
    main()
