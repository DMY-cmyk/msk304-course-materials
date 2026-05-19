import fitz, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
PDF = r"D:\DZAKI\S2\Sem. 1\Manajemen Strategik\Ebook\(Business professional collection) John E. Gamble_ Arthur A. Thompson_ Margaret Ann Peteraf - Essentials of Strategic Management _ The Quest for Competitive Advantage (2021).pdf"
doc = fitz.open(PDF)

# Find chapter title pages by searching specifically for the opener
print("=== CH8 opener (search 'Corporate Strategy: Diversification') ===")
for i in range(180, 220):
    text = doc.load_page(i).get_text()
    if "Corporate Strategy:" in text and "Diversification" in text and i < 220:
        # Look for big title on early page
        first_lines = "\n".join(text.split("\n")[:20])
        print(f"--- PAGE_IDX={i} ---")
        print(first_lines)
        print()
        if i > 200:
            break

print("=== CH9 opener ===")
for i in range(215, 240):
    text = doc.load_page(i).get_text()
    first_lines = "\n".join(text.split("\n")[:15])
    if "Ethics" in text and ("Corporate Social Responsibility" in text or "Sustainability" in text) and ("9" in first_lines or "CHAPTER" in first_lines.upper()):
        print(f"--- PAGE_IDX={i} ---")
        print(first_lines)
        print()
        break

# Find Ch.8 section headings
print("=== CH8 SECTION HEADINGS (PDF pages 190-218) ===")
for i in range(190, 219):
    page = doc.load_page(i)
    text = page.get_text()
    # Extract blocks with larger fonts (headings)
    blocks = page.get_text("dict")["blocks"]
    for b in blocks:
        if "lines" not in b: continue
        for line in b["lines"]:
            for span in line["spans"]:
                if span["size"] >= 12 and len(span["text"].strip()) > 5 and len(span["text"].strip()) < 100:
                    t = span["text"].strip()
                    # Filter out page headers
                    if "Chapter 8" in t or "Multibusiness Company" in t:
                        continue
                    if t and not t.startswith(("p.", "•")):
                        print(f"p{i} sz{span['size']:.0f}: {t}")

doc.close()
