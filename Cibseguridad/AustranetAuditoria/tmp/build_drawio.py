import xml.etree.ElementTree as ET

def create_drawio():
    mxfile = ET.Element("mxfile", host="app.diagrams.net", agent="Antigravity", version="21.0.0", type="device")
    diagram = ET.SubElement(mxfile, "diagram", id="Macroflujo", name="Macroflujo de Gobernanza ISO 27001")
    model = ET.SubElement(diagram, "mxGraphModel", dx="1600", dy="900", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="1920", pageHeight="1080", math="0", shadow="0")
    root = ET.SubElement(model, "root")
    
    ET.SubElement(root, "mxCell", id="0")
    ET.SubElement(root, "mxCell", id="1", parent="0")
    
    # Helper to add cells
    cell_id = 2
    def add_node(label, x, y, w, h, style):
        nonlocal cell_id
        cid = str(cell_id)
        cell_id += 1
        cell = ET.SubElement(root, "mxCell", id=cid, value=label, style=style, vertex="1", parent="1")
        ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h), **{"as": "geometry"})
        return cid

    def add_edge(source_id, target_id, label=""):
        nonlocal cell_id
        cid = str(cell_id)
        cell_id += 1
        edge = ET.SubElement(root, "mxCell", id=cid, value=label, style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;strokeColor=#4A5568;", edge="1", parent="1", source=source_id, target=target_id)
        ET.SubElement(edge, "mxGeometry", relative="1", **{"as": "geometry"})
        return cid

    # 1. INPUT
    input_style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#EBF8FF;strokeColor=#3182CE;fontStyle=1;fontSize=13;fontColor=#2B6CB0;strokeWidth=2;"
    c_input = add_node("<b>INPUT MAESTRO</b><br/>exportUsers_2026-10-28.csv<br/><small>(495 usuarios Entra ID)</small>", 60, 320, 240, 100, input_style)
    
    # 2. ROUTER
    router_style = "rhombus;whiteSpace=wrap;html=1;fillColor=#FAF5FF;strokeColor=#805AD5;fontStyle=1;fontSize=12;fontColor=#553C9A;strokeWidth=2;"
    c_router = add_node("<b>ENRUTADOR DE<br/>GOBERNANZA</b><br/><small>Clasificación de cuentas</small>", 380, 290, 180, 160, router_style)
    add_edge(c_input, c_router)

    # 3. PROTOCOLOS
    # P5: MFA
    p5_style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#EBF8FF;strokeColor=#2B6CB0;strokeWidth=2;fontColor=#1A365D;align=left;spacingLeft=15;"
    c_p5 = add_node("<b>PROTOCOLO 5 (MFA Admins)</b><br/>• Censo de 15 roles privilegiados<br/>• Exclusión de Break-Glass<br/>• Control ISO A.5.17 / A.8.2", 660, 60, 320, 90, p5_style)
    add_edge(c_router, c_p5, "Roles Admin")

    # P1: Cuentas Nuevas
    p1_style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#FEFCBF;strokeColor=#D69E2E;strokeWidth=2;fontColor=#744210;align=left;spacingLeft=15;"
    c_p1 = add_node("<b>PROTOCOLO 1 (Cuentas Nuevas - 5d)</b><br/>• Exclusión de cuentas servicio<br/>• Alerta día 3 | Bloqueo día 5<br/>• 11 cuentas evaluadas (ISO A.5.16)", 660, 190, 320, 90, p1_style)
    add_edge(c_router, c_p1, "Sin Login")

    # P2: Inactivos > 60d
    p2_style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#FED7D7;strokeColor=#E53E3E;strokeWidth=2;fontColor=#742A2A;align=left;spacingLeft=15;"
    c_p2 = add_node("<b>PROTOCOLO 2 (Inactivos > 60d)</b><br/>• Cuarentena a 30 días<br/>• Bloqueo con justificación día 60<br/>• 53 cuentas evaluadas (ISO A.5.15)", 660, 320, 320, 90, p2_style)
    add_edge(c_router, c_p2, "Inactivo >60d")

    # P3: Offboarding
    p3_style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#E9D8FD;strokeColor=#805AD5;strokeWidth=2;fontColor=#44337A;align=left;spacingLeft=15;"
    c_p3 = add_node("<b>PROTOCOLO 3 (Offboarding / Baja)</b><br/>• Respaldo OneDrive y Buzón Compartido<br/>• Retiro licencias | Purga a día 60<br/>• 46 cuentas bloqueadas (ISO A.8.10)", 660, 450, 320, 90, p3_style)
    add_edge(c_router, c_p3, "Bloqueadas")

    # P4: Guests
    p4_style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#EDF2F7;strokeColor=#718096;strokeWidth=2;fontColor=#2D3748;align=left;spacingLeft=15;"
    c_p4 = add_node("<b>PROTOCOLO 4 (Gobernanza Guests)</b><br/>• Purga de invitaciones no aceptadas<br/>• Baja por inactividad >60d sin buzón<br/>• 306 usuarios externos (ISO A.5.19)", 660, 580, 320, 90, p4_style)
    add_edge(c_router, c_p4, "Guest")

    # Inter-protocol edge: P1 y P2 van a P3 cuando se bloquean
    add_edge(c_p1, c_p3, "Al bloquear")
    add_edge(c_p2, c_p3, "Al bloquear")

    # 4. OUTPUTS
    out_style = "rounded=1;whiteSpace=wrap;html=1;fillColor=#F0FFF4;strokeColor=#38A169;strokeWidth=2;fontColor=#22543D;align=left;spacingLeft=15;"
    c_out = add_node("<b>OUTPUTS GLOBALES UNIFICADOS</b><br/><br/>" +
                     "<b>1. Acciones Cloud (Graph API / Exchange):</b><br/>" +
                     "• Deshabilitar cuenta / Revocar tokens<br/>" +
                     "• Convertir a Shared Mailbox / Quitar licencia<br/><br/>" +
                     "<b>2. Notificaciones y Alertas:</b><br/>" +
                     "• Correo preventivo a jefaturas (días 3 y 50)<br/>" +
                     "• Alerta de uso Break-Glass<br/><br/>" +
                     "<b>3. Evidencias ISO 27001 (AustranetGRC):</b><br/>" +
                     "• Matriz actualizada de identidades (9.1)<br/>" +
                     "• Expediente trazable para auditoría (9.2)", 1070, 180, 360, 380, out_style)

    add_edge(c_p5, c_out)
    add_edge(c_p1, c_out)
    add_edge(c_p2, c_out)
    add_edge(c_p3, c_out)
    add_edge(c_p4, c_out)

    tree = ET.ElementTree(mxfile)
    ET.indent(tree, space="  ", level=0)
    out_path = "output/Flujo_Gobernanza_ISO27001_Austranet.drawio"
    tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"Archivo draw.io generado exitosamente: {out_path}")

create_drawio()
