"""Fix reference.docx to match PDF formatting exactly."""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from docx import Document
from docx.shared import Pt, Inches, RGBColor, Emu
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from lxml import etree
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
ref_path = BASE / "scripts" / "reference.docx"
doc = Document(str(ref_path))

print("Fixing reference.docx styles...")

# ============================================================
# PDF FORMAT INVENTORY (from programmatic analysis):
# - Page size: 612 x 792 pts = US Letter
# - Margins: L=72pt (1in), R=~69pt, T=~75pt, B=~80pt
# - H1: Calibri Bold 14pt, yellow background, CENTERED (chapter), LEFT (article)
#   -> Both chapter and article headings are H1 in markdown
#   -> Compromise: LEFT for all H1 (since article headings dominate)
# - H2: Calibri Bold 11pt, LEFT, NO yellow background
# - H3: Calibri Bold 11pt, LEFT, NO yellow background
# - Normal: Calibri 11pt, Justified, line spacing EXACTLY 14.5pt, first-line indent 18pt
# - List: indent 36pt from margin (=108pt total), no first-line indent
# - 'Pertanyaan' phrases: RED BOLD (#EE0000) - handled by post-processing
# ============================================================

# === NORMAL STYLE ===
normal = doc.styles['Normal']
normal_pPr = normal.element.get_or_add_pPr()

# Fix line spacing: EXACTLY 14.5pt = 290 twips
for child in list(normal_pPr):
    if child.tag.endswith('}spacing'):
        normal_pPr.remove(child)
spacing = OxmlElement('w:spacing')
spacing.set(qn('w:line'), '290')
spacing.set(qn('w:lineRule'), 'exact')
spacing.set(qn('w:after'), '120')  # 6pt space after each paragraph
normal_pPr.append(spacing)

# Fix first-line indent: 18pt = 360 twips
for child in list(normal_pPr):
    if child.tag.endswith('}ind'):
        normal_pPr.remove(child)
ind = OxmlElement('w:ind')
ind.set(qn('w:firstLine'), '360')
normal_pPr.append(ind)

# Ensure justified
jc = normal_pPr.find(qn('w:jc'))
if jc is None:
    jc = OxmlElement('w:jc')
    normal_pPr.append(jc)
jc.set(qn('w:val'), 'both')

print("  Normal: line=290 twips EXACT (14.5pt), firstLine=360 twips (18pt), jc=both, after=120")

# === HEADING 1 ===
# H1 = 14pt Bold, LEFT aligned (works for both chapter and article headings),
# Yellow background highlight (already set), no first-line indent
h1 = doc.styles['Heading 1']
h1_pPr = h1.element.get_or_add_pPr()

# Set LEFT alignment (consistent with majority of H1 uses in PDF = article headings)
jc = h1_pPr.find(qn('w:jc'))
if jc is None:
    jc = OxmlElement('w:jc')
    h1_pPr.append(jc)
jc.set(qn('w:val'), 'left')

# Set spacing: 0pt before, 8pt after
for child in list(h1_pPr):
    if child.tag.endswith('}spacing'):
        h1_pPr.remove(child)
spacing = OxmlElement('w:spacing')
spacing.set(qn('w:before'), '0')
spacing.set(qn('w:after'), '160')  # 8pt = 160 twips
h1_pPr.append(spacing)

# First line indent = 0
ind = h1_pPr.find(qn('w:ind'))
if ind is None:
    ind = OxmlElement('w:ind')
    h1_pPr.append(ind)
ind.set(qn('w:firstLine'), '0')
ind.set(qn('w:left'), '0')

# Ensure font size = 14pt = 28 half-points
h1_rPr = h1.element.get_or_add_rPr()
sz = h1_rPr.find(qn('w:sz'))
if sz is None:
    sz = OxmlElement('w:sz')
    h1_rPr.append(sz)
sz.set(qn('w:val'), '28')
szCs = h1_rPr.find(qn('w:szCs'))
if szCs is None:
    szCs = OxmlElement('w:szCs')
    h1_rPr.append(szCs)
szCs.set(qn('w:val'), '28')

print("  Heading 1: LEFT, 14pt Bold, 0pt before, 8pt after, yellow highlight kept")

# === HEADING 2 ===
# H2 = 11pt Bold, LEFT, NO yellow background, no first-line indent
h2 = doc.styles['Heading 2']
h2_pPr = h2.element.get_or_add_pPr()

# REMOVE yellow highlight shading from H2
shd = h2_pPr.find(qn('w:shd'))
if shd is not None:
    h2_pPr.remove(shd)

# Remove highlight from H2 rPr
h2_rPr = h2.element.get_or_add_rPr()
hl = h2_rPr.find(qn('w:highlight'))
if hl is not None:
    h2_rPr.remove(hl)

# Set left alignment
jc = h2_pPr.find(qn('w:jc'))
if jc is None:
    jc = OxmlElement('w:jc')
    h2_pPr.append(jc)
jc.set(qn('w:val'), 'left')

# Set spacing: 12pt before, 4pt after
for child in list(h2_pPr):
    if child.tag.endswith('}spacing'):
        h2_pPr.remove(child)
spacing = OxmlElement('w:spacing')
spacing.set(qn('w:before'), '240')  # 12pt = 240 twips
spacing.set(qn('w:after'), '80')   # 4pt = 80 twips
h2_pPr.append(spacing)

# First line indent = 0
ind = h2_pPr.find(qn('w:ind'))
if ind is None:
    ind = OxmlElement('w:ind')
    h2_pPr.append(ind)
ind.set(qn('w:firstLine'), '0')
ind.set(qn('w:left'), '0')

# Font size = 11pt = 22 half-points
sz = h2_rPr.find(qn('w:sz'))
if sz is None:
    sz = OxmlElement('w:sz')
    h2_rPr.append(sz)
sz.set(qn('w:val'), '22')
szCs = h2_rPr.find(qn('w:szCs'))
if szCs is None:
    szCs = OxmlElement('w:szCs')
    h2_rPr.append(szCs)
szCs.set(qn('w:val'), '22')

print("  Heading 2: LEFT, 11pt Bold, NO yellow, 12pt before, 4pt after")

# === HEADING 3 ===
# H3 = 11pt Bold, LEFT, NO yellow background
h3 = doc.styles['Heading 3']
h3_pPr = h3.element.get_or_add_pPr()

# REMOVE yellow highlight from H3
shd = h3_pPr.find(qn('w:shd'))
if shd is not None:
    h3_pPr.remove(shd)

h3_rPr = h3.element.get_or_add_rPr()
hl = h3_rPr.find(qn('w:highlight'))
if hl is not None:
    h3_rPr.remove(hl)

# Set left alignment
jc = h3_pPr.find(qn('w:jc'))
if jc is None:
    jc = OxmlElement('w:jc')
    h3_pPr.append(jc)
jc.set(qn('w:val'), 'left')

# Spacing: 8pt before, 4pt after
for child in list(h3_pPr):
    if child.tag.endswith('}spacing'):
        h3_pPr.remove(child)
spacing = OxmlElement('w:spacing')
spacing.set(qn('w:before'), '160')  # 8pt
spacing.set(qn('w:after'), '80')   # 4pt
h3_pPr.append(spacing)

# First line indent = 0
ind = h3_pPr.find(qn('w:ind'))
if ind is None:
    ind = OxmlElement('w:ind')
    h3_pPr.append(ind)
ind.set(qn('w:firstLine'), '0')
ind.set(qn('w:left'), '0')

# Font size = 11pt
sz = h3_rPr.find(qn('w:sz'))
if sz is None:
    sz = OxmlElement('w:sz')
    h3_rPr.append(sz)
sz.set(qn('w:val'), '22')
szCs = h3_rPr.find(qn('w:szCs'))
if szCs is None:
    szCs = OxmlElement('w:szCs')
    h3_rPr.append(szCs)
szCs.set(qn('w:val'), '22')

print("  Heading 3: LEFT, 11pt Bold, NO yellow, 8pt before, 4pt after")

# === BODY TEXT STYLE ===
# Used by pandoc for some elements - match Normal but without first-line indent
bt = doc.styles['Body Text']
bt_pPr = bt.element.get_or_add_pPr()

for child in list(bt_pPr):
    if child.tag.endswith('}spacing'):
        bt_pPr.remove(child)
spacing = OxmlElement('w:spacing')
spacing.set(qn('w:line'), '290')
spacing.set(qn('w:lineRule'), 'exact')
spacing.set(qn('w:after'), '120')
bt_pPr.append(spacing)

jc = bt_pPr.find(qn('w:jc'))
if jc is None:
    jc = OxmlElement('w:jc')
    bt_pPr.append(jc)
jc.set(qn('w:val'), 'both')

# Ensure no yellow highlight on Body Text
bt_rPr = bt.element.get_or_add_rPr()
hl = bt_rPr.find(qn('w:highlight'))
if hl is not None:
    bt_rPr.remove(hl)

print("  Body Text: line=290 EXACT, justified, no yellow")

# === LIST PARAGRAPH ===
# PDF lists: text at x=108pt (margin 72 + indent 36)
# left_indent = 720 twips = 36pt is already set, no change needed
# Just ensure no first-line indent that would over-indent
lp = doc.styles['List Paragraph']
lp_pPr = lp.element.get_or_add_pPr()

ind = lp_pPr.find(qn('w:ind'))
if ind is None:
    ind = OxmlElement('w:ind')
    lp_pPr.append(ind)
ind.set(qn('w:left'), '720')
# Remove any firstLine
if ind.get(qn('w:firstLine')):
    del ind.attrib[qn('w:firstLine')]
if ind.get(qn('w:hanging')):
    del ind.attrib[qn('w:hanging')]

# Add spacing element - small space between list items
for child in list(lp_pPr):
    if child.tag.endswith('}spacing'):
        lp_pPr.remove(child)
spacing = OxmlElement('w:spacing')
spacing.set(qn('w:after'), '60')  # 3pt after list items
lp_pPr.append(spacing)

print("  List Paragraph: left=720 (36pt), no firstLine, 3pt after")

# === PAGE SETUP (document-level) ===
# Ensure 1-inch margins all around
# Check current section
from docx.shared import Inches
sections = doc.sections
for section in sections:
    section.page_width = 12240  # 612pt * 20 = 12240 twips = 8.5in
    section.page_height = 15840  # 792pt * 20 = 15840 twips = 11in
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.header_distance = Inches(0.5)
    section.footer_distance = Inches(0.5)

print("  Page setup: 8.5x11in (US Letter), 1in margins all around")

# Save
doc.save(str(ref_path))
print()
print("reference.docx saved successfully!")

# Verify the saved file
doc_check = Document(str(ref_path))
n = doc_check.styles['Normal']
from docx.shared import Pt
print("\nVerification:")
print(f"  Normal line spacing: {n.paragraph_format.line_spacing} (expected ~184150 EMU = 14.5pt)")
print(f"  Normal line spacing rule: {n.paragraph_format.line_spacing_rule}")
print(f"  Normal first-line indent: {n.paragraph_format.first_line_indent} (expected ~228600 EMU = 18pt)")
print(f"  Normal space after: {n.paragraph_format.space_after}")
h2_check = doc_check.styles['Heading 2']
from lxml import etree
h2_xml = etree.tostring(h2_check.element, pretty_print=True).decode('utf-8')
print("\nHeading 2 XML (checking for highlight removal):")
print("  'highlight' in H2 xml:", "'highlight'" in h2_xml.lower())
print("  'FFFF00' in H2 xml:", 'FFFF00' in h2_xml)
