import fitz
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

PDF = r"D:\DZAKI\S2\Sem. 1\Manajemen Strategik\Ebook\(Business professional collection) John E. Gamble_ Arthur A. Thompson_ Margaret Ann Peteraf - Essentials of Strategic Management _ The Quest for Competitive Advantage (2021).pdf"
doc = fitz.open(PDF)
print("TOTAL_PAGES:", doc.page_count)
print()
print("=== CHAPTER 8 / 9 / TAILORING markers ===")
for i in range(doc.page_count):
    text = doc.load_page(i).get_text()
    up = text.upper()
    # Look for chapter heading patterns - skip TOC/index by requiring early-page chapter title formatting
    if i > 5 and ("CHAPTER 8" in up or "CHAPTER 9" in up or "TAILORING STRATEGY" in up):
        snippet = text[:250].replace("\n", " | ")
        print(f"PAGE_IDX={i} :: {snippet}")
print()
print("=== FIGURE 8.x occurrences ===")
for i in range(doc.page_count):
    page = doc.load_page(i)
    text = page.get_text()
    hits = page.search_for("FIGURE 8.")
    if hits:
        # Extract the figure label and following text
        lines = text.split("\n")
        for idx, line in enumerate(lines):
            if "FIGURE 8." in line.upper():
                following = " | ".join(lines[idx:idx+4])
                print(f"PAGE_IDX={i} :: {following[:300]}")
print()
print("=== CHAPTER 9 anchor lookup (first occurrences after page 200) ===")
for i in range(200, min(doc.page_count, 320)):
    text = doc.load_page(i).get_text()
    if text.strip().startswith("CHAPTER 9") or "\nCHAPTER 9\n" in text[:500]:
        snippet = text[:300].replace("\n", " | ")
        print(f"PAGE_IDX={i} :: {snippet}")
doc.close()
