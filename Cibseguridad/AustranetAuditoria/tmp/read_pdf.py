import pymupdf

doc = pymupdf.open("usuarios/Borrador-flujo-gobernanzaEntraID.pdf")
print("Total pages:", len(doc))
for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text()
    print(f"--- PAGE {page_num + 1} ---")
    print(text)
