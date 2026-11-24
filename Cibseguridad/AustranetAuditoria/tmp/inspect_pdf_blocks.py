import pymupdf

doc = pymupdf.open("usuarios/Borrador-flujo-gobernanzaEntraID.pdf")
page = doc[0]
blocks = page.get_text("blocks")
for b in blocks:
    print(f"Bbox: {b[:4]} -> Text: {b[4].strip()!r}")
