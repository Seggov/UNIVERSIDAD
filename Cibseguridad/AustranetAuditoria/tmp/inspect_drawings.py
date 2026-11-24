import pymupdf

doc = pymupdf.open("usuarios/Borrador-flujo-gobernanzaEntraID.pdf")
page = doc[0]
for idx, d in enumerate(page.get_drawings()):
    rect = d.get("rect")
    fill = d.get("fill")
    color = d.get("color")
    items = d.get("items")
    print(f"Drawing {idx}: rect={rect}, fill={fill}, color={color}, items_count={len(items)}")
