import xml.etree.ElementTree as ET

def build_clean_drawio():
    mxfile = ET.Element("mxfile", host="app.diagrams.net", agent="Antigravity", version="21.0.0", type="device")
    diagram = ET.SubElement(mxfile, "diagram", id="MacroflujoLimpio", name="Macroflujo Ordenado ISO 27001")
    model = ET.SubElement(diagram, "mxGraphModel", dx="2000", dy="1200", grid="1", gridSize="10", guides="1", 
                          tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", 
                          pageWidth="2200", pageHeight="1100", math="0", shadow="0")
    root = ET.SubElement(model, "root")
    
    ET.SubElement(root, "mxCell", id="0")
    ET.SubElement(root, "mxCell", id="1", parent="0")
    
    cell_id = 2
    def get_id():
        nonlocal cell_id
        cid = str(cell_id)
        cell_id += 1
        return cid

    # -------------------------------------------------------------
    # 0. CONTENEDORES DE FASES (BACKGROUND SWIMLANES/COLUMNAS)
    # -------------------------------------------------------------
    def add_phase_box(title, x, y, w, h, bg_color, border_color):
        cid = get_id()
        style = (f"swimlane;startSize=35;horizontal=1;fillColor={bg_color};strokeColor={border_color};"
                 f"fontStyle=1;fontSize=13;fontColor=#2D3748;rounded=1;dashed=0;strokeWidth=1.5;shadow=0;")
        cell = ET.SubElement(root, "mxCell", id=cid, value=title, style=style, vertex="1", parent="1")
        ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h), **{"as": "geometry"})
        return cid

    # Columnas principales
    add_phase_box("FASE 1: INGESTA Y CLASIFICACIÓN", 50, 40, 520, 800, "#F8FAFC", "#CBD5E1")
    add_phase_box("FASE 2: PROTOCOLOS DE DETECCIÓN Y ACCESO", 610, 40, 360, 800, "#F8FAFC", "#CBD5E1")
    add_phase_box("FASE 3: OFFBOARDING Y RETENCIÓN", 1010, 40, 360, 800, "#F8FAFC", "#CBD5E1")
    add_phase_box("FASE 4: SALIDAS Y EVIDENCIAS ISO 27001", 1410, 40, 360, 800, "#F8FAFC", "#CBD5E1")

    # -------------------------------------------------------------
    # 1. NODOS
    # -------------------------------------------------------------
    def add_node(label, x, y, w, h, style):
        cid = get_id()
        cell = ET.SubElement(root, "mxCell", id=cid, value=label, style=style, vertex="1", parent="1")
        ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h), **{"as": "geometry"})
        return cid

    # FASE 1
    input_style = ("rounded=1;whiteSpace=wrap;html=1;fillColor=#EBF8FF;strokeColor=#3182CE;strokeWidth=2;"
                   "fontColor=#1A365D;fontSize=12;shadow=1;")
    c_input = add_node("<b>📥 DATASET MAESTRO (CSV)</b><br/>"
                       "<code>exportUsers_2026-10-28.csv</code><br/>"
                       "<hr style='margin:4px 0;'/>"
                       "• 495 Cuentas Microsoft Entra ID<br/>"
                       "• UserType: 189 Member / 306 Guest<br/>"
                       "• Actividad de login y roles admin", 80, 370, 220, 130, input_style)

    router_style = ("rhombus;whiteSpace=wrap;html=1;fillColor=#FAF5FF;strokeColor=#805AD5;strokeWidth=2;"
                    "fontColor=#44337A;fontStyle=1;fontSize=12;shadow=1;")
    c_router = add_node("<b>ENRUTADOR<br/>CENTRAL</b><br/><small>Clasificación<br/>por atributos</small>", 350, 360, 180, 150, router_style)

    # FASE 2: PROTOCOLOS DE DETECCIÓN
    # P5: MFA
    p5_style = ("rounded=1;whiteSpace=wrap;html=1;fillColor=#EBF8FF;strokeColor=#2B6CB0;strokeWidth=2;"
                "fontColor=#1A365D;fontSize=11;align=left;spacingLeft=12;shadow=1;")
    c_p5 = add_node("<b>🛡️ PROTOCOLO 5: MFA Roles Críticos</b><br/>"
                    "• Censo de 15 roles administrativos<br/>"
                    "• Verificación política en modo Enforce<br/>"
                    "• <b>Exclusión explícita de Break-Glass</b><br/>"
                    "<small style='color:#4A5568;'>ISO 27001: A.5.17 / A.8.2</small>", 630, 90, 320, 110, p5_style)

    # P1: Cuentas Nuevas
    p1_style = ("rounded=1;whiteSpace=wrap;html=1;fillColor=#FEFCBF;strokeColor=#D69E2E;strokeWidth=2;"
                "fontColor=#744210;fontSize=11;align=left;spacingLeft=12;shadow=1;")
    c_p1 = add_node("<b>⚡ PROTOCOLO 1: Cuentas Nuevas (5d)</b><br/>"
                    "• Exclusión de cuentas de servicio (6)<br/>"
                    "• Alerta a jefatura al día 3 hábil<br/>"
                    "• <b>Bloqueo al día 5 sin inicio de sesión</b><br/>"
                    "<small style='color:#4A5568;'>Población: 11 sin login | ISO A.5.16</small>", 630, 240, 320, 110, p1_style)

    # P2: Inactivos > 60d
    p2_style = ("rounded=1;whiteSpace=wrap;html=1;fillColor=#FED7D7;strokeColor=#E53E3E;strokeWidth=2;"
                "fontColor=#742A2A;fontSize=11;align=left;spacingLeft=12;shadow=1;")
    c_p2 = add_node("<b>⏳ PROTOCOLO 2: Inactividad &gt; 60 Días</b><br/>"
                    "• Cuarentena lógica a los 30 días<br/>"
                    "• Notificación preventiva día 50<br/>"
                    "• <b>Bloqueo formal + Revocar sesiones día 60</b><br/>"
                    "<small style='color:#4A5568;'>Población: 53 inactivas | ISO A.5.15</small>", 630, 390, 320, 110, p2_style)

    # P4: Guests Externos
    p4_style = ("rounded=1;whiteSpace=wrap;html=1;fillColor=#EDF2F7;strokeColor=#718096;strokeWidth=2;"
                "fontColor=#2D3748;fontSize=11;align=left;spacingLeft=12;shadow=1;")
    c_p4 = add_node("<b>🌐 PROTOCOLO 4: Ciclo de Vida Guests</b><br/>"
                    "• 117 sin canje: revocar invitaciones &gt; 30d<br/>"
                    "• 101 inactivos &gt; 60d: baja directa sin buzón<br/>"
                    "• 79 activos: recertificación periódica<br/>"
                    "<small style='color:#4A5568;'>Población: 306 invitados | ISO A.5.19</small>", 630, 560, 320, 110, p4_style)

    # FASE 3: OFFBOARDING (POST-BLOQUEO)
    p3_style = ("rounded=1;whiteSpace=wrap;html=1;fillColor=#E9D8FD;strokeColor=#6B46C1;strokeWidth=2;"
                "fontColor=#44337A;fontSize=11;align=left;spacingLeft=12;shadow=1;")
    c_p3 = add_node("<b>📦 PROTOCOLO 3: Offboarding &amp; Retención</b><br/>"
                    "• <b>Paso 1:</b> Convertir buzón a Shared Mailbox<br/>"
                    "• <b>Paso 2:</b> Respaldar / delegar OneDrive<br/>"
                    "• <b>Paso 3:</b> Desasignar licencias de pago M365<br/>"
                    "• <b>Paso 4:</b> Espera de retención legal (60 días)<br/>"
                    "• <b>Paso 5:</b> Evaluar borrado final en Entra ID<br/>"
                    "<small style='color:#4A5568;'>Población: 46 bloqueadas | ISO A.8.10</small>", 1030, 310, 320, 160, p3_style)

    # FASE 4: OUTPUTS (3 TARJETAS SEPARADAS)
    out_notif_style = ("rounded=1;whiteSpace=wrap;html=1;fillColor=#FEFCBF;strokeColor=#D69E2E;strokeWidth=2;"
                       "fontColor=#744210;fontSize=11;align=left;spacingLeft=12;shadow=1;")
    c_out_notif = add_node("<b>📧 1. NOTIFICACIONES &amp; ALERTAS</b><br/>"
                           "• Correo preventivo a jefaturas (días 3 y 50)<br/>"
                           "• Alerta de seguridad por uso de Break-Glass<br/>"
                           "• Aviso formal de cuenta bloqueada", 1430, 120, 320, 100, out_notif_style)

    out_cloud_style = ("rounded=1;whiteSpace=wrap;html=1;fillColor=#EBF8FF;strokeColor=#3182CE;strokeWidth=2;"
                       "fontColor=#1A365D;fontSize=11;align=left;spacingLeft=12;shadow=1;")
    c_out_cloud = add_node("<b>☁️ 2. ACCIONES CLOUD (Graph / M365)</b><br/>"
                           "• <code>accountEnabled: false</code> ejecutado<br/>"
                           "• Tokens de sesión revocados en Graph<br/>"
                           "• Buzón compartido activo sin costo de licencia<br/>"
                           "• Eliminación definitiva de cuentas purgadas", 1430, 340, 320, 120, out_cloud_style)

    out_evid_style = ("rounded=1;whiteSpace=wrap;html=1;fillColor=#F0FFF4;strokeColor=#38A169;strokeWidth=2;"
                      "fontColor=#22543D;fontSize=11;align=left;spacingLeft=12;shadow=1;")
    c_out_evid = add_node("<b>📁 3. EVIDENCIAS ISO 27001 (GRC)</b><br/>"
                          "• Matriz actualizada de identidades (9.1)<br/>"
                          "• Trazabilidad de excepciones y justificaciones<br/>"
                          "• Expedientes listos para Auditoría Interna (9.2)<br/>"
                          "• Registro histórico en SharePoint / AustranetGRC", 1430, 560, 320, 120, out_evid_style)

    # -------------------------------------------------------------
    # 2. CONECTORES (EDGES) CON PUERTOS PRECISOS SIN COLISIONES
    # -------------------------------------------------------------
    def add_edge(source_id, target_id, label="", exit_port=(1, 0.5), entry_port=(0, 0.5), stroke_color="#4A5568", dashed=0):
        cid = get_id()
        ex, ey = exit_port
        enx, eny = entry_port
        style = (f"edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;"
                 f"strokeWidth=2;strokeColor={stroke_color};fontSize=11;fontColor={stroke_color};"
                 f"exitX={ex};exitY={ey};exitDx=0;exitDy=0;entryX={enx};entryY={eny};entryDx=0;entryDy=0;"
                 f"dashed={dashed};")
        edge = ET.SubElement(root, "mxCell", id=cid, value=label, style=style, edge="1", parent="1", source=source_id, target=target_id)
        ET.SubElement(edge, "mxGeometry", relative="1", **{"as": "geometry"})
        return cid

    # INGEST -> ROUTER
    add_edge(c_input, c_router, "495 cuentas", exit_port=(1, 0.5), entry_port=(0, 0.5))

    # ROUTER -> P5 (Hacia arriba)
    add_edge(c_router, c_p5, "Roles Admin", exit_port=(0.5, 0), entry_port=(0, 0.5), stroke_color="#2B6CB0")

    # ROUTER -> P1 (Arriba-Centro)
    add_edge(c_router, c_p1, "Sin Login (11)", exit_port=(1, 0.2), entry_port=(0, 0.5), stroke_color="#D69E2E")

    # ROUTER -> P2 (Centro)
    add_edge(c_router, c_p2, "Inactivos >60d (53)", exit_port=(1, 0.5), entry_port=(0, 0.5), stroke_color="#E53E3E")

    # ROUTER -> P4 (Hacia abajo)
    add_edge(c_router, c_p4, "Guests (306)", exit_port=(0.5, 1), entry_port=(0, 0.5), stroke_color="#718096")

    # ROUTER -> P3 (Cuentas ya deshabilitadas directamente al offboarding: 46 cuentas)
    add_edge(c_router, c_p3, "Bloqueadas (46)", exit_port=(1, 0.8), entry_port=(0, 0.8), stroke_color="#6B46C1")

    # TRANSICIONES POST-BLOQUEO (P1 y P2 pasan a P3 de forma limpia)
    add_edge(c_p1, c_p3, "Al bloquear", exit_port=(1, 0.5), entry_port=(0, 0.2), stroke_color="#D69E2E", dashed=1)
    add_edge(c_p2, c_p3, "Al bloquear", exit_port=(1, 0.5), entry_port=(0, 0.5), stroke_color="#E53E3E", dashed=1)

    # PROTOCOLOS -> OUTPUTS
    # P5 -> Alertas (Break-Glass) & Evidencia (MFA Conforme)
    add_edge(c_p5, c_out_notif, "Alerta Break-Glass", exit_port=(1, 0.3), entry_port=(0, 0.3), stroke_color="#2B6CB0")
    add_edge(c_p5, c_out_evid, "MFA Conforme", exit_port=(1, 0.7), entry_port=(0, 0.1), stroke_color="#2B6CB0")

    # P1 -> Notificación (Aviso día 3)
    add_edge(c_p1, c_out_notif, "Aviso día 3", exit_port=(1, 0.8), entry_port=(0, 0.7), stroke_color="#D69E2E")

    # P3 -> Acciones Cloud & Evidencias GRC
    add_edge(c_p3, c_out_cloud, "Ejecutar Offboarding", exit_port=(1, 0.4), entry_port=(0, 0.5), stroke_color="#6B46C1")
    add_edge(c_p3, c_out_evid, "Expediente de Baja", exit_port=(1, 0.7), entry_port=(0, 0.5), stroke_color="#38A169")

    # P4 -> Acciones Cloud (Purga Guests)
    add_edge(c_p4, c_out_cloud, "Purga de Externos", exit_port=(1, 0.5), entry_port=(0, 0.8), stroke_color="#718096")

    # SERIALIZAR
    tree = ET.ElementTree(mxfile)
    ET.indent(tree, space="  ", level=0)
    out_path = "output/Flujo_Gobernanza_ISO27001_Austranet.drawio"
    tree.write(out_path, encoding="utf-8", xml_declaration=True)
    print(f"Archivo Draw.io actualizado con éxito en: {out_path}")

build_clean_drawio()
