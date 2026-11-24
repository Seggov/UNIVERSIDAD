import csv
import io
import json
from datetime import datetime

REF_DATE = datetime(2026, 10, 28)

with open("usuarios/exportUsers_2026-10-28(in).csv", "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

header = lines[0].strip().split(",")

users = []
for line in lines[1:]:
    raw = line.strip()
    if not raw:
        continue
    if raw.startswith('"') and raw.endswith('"'):
        raw = raw[1:-1].replace('""', '"')
    row = list(csv.reader(io.StringIO(raw)))[0]
    users.append(dict(zip(header, row)))

def clasificar_cuenta(u):
    upn = u.get("userPrincipalName", "").lower()
    dn = u.get("displayName", "").lower()
    ut = u.get("userType", "")
    
    if ut == "Guest" or "#ext#" in upn:
        return "Invitado Externo (Guest)"
    
    # Heurística para cuentas de servicio / buzones / administración
    admin_terms = ["admin", "soporte", "support", "service", "alerta", "darcuamplimiento", "academis", "backup", "synch"]
    if any(t in upn or t in dn for t in admin_terms):
        if "admin" in upn or "admin" in dn:
            return "Cuenta Administrativa / Privilegiada"
        return "Cuenta de Servicio / Buzón Compartido"
    
    return "Persona Interna (Colaborador)"

output_rows = []

for u in users:
    ut = u.get("userType", "")
    enabled = u.get("accountEnabled", "") == "True"
    
    tipo_cuenta = clasificar_cuenta(u)
    
    s_raw = u.get("signInActivity", "").strip()
    s_obj = json.loads(s_raw) if s_raw else {}
    
    dt_str = s_obj.get("lastSuccessfulSignInDateTime") or s_obj.get("lastSignInDateTime") or s_obj.get("lastNonInteractiveSignInDateTime")
    
    dt = None
    diff_days = None
    if dt_str:
        try:
            dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00")).replace(tzinfo=None)
            diff_days = (REF_DATE - dt).days
        except Exception:
            pass
    
    # Categorización de auditoría según diagrama base y SGSI
    estado_auditoria = ""
    accion_recomendada = ""
    
    if ut == "Guest":
        if not enabled:
            estado_auditoria = "Invitado Bloqueado"
            accion_recomendada = "Evaluar eliminación directa tras 60-90 días"
        elif diff_days is None:
            estado_auditoria = "Invitado Sin Acceso Registrado"
            accion_recomendada = "Verificar invitación pendiente o revocar acceso"
        elif diff_days > 60:
            estado_auditoria = "Invitado Inactivo > 60 días"
            accion_recomendada = "Revocar acceso / eliminar usuario externo"
        else:
            estado_auditoria = "Invitado Activo"
            accion_recomendada = "Mantener y recertificar en próxima revisión"
    else:
        # Miembro interno
        if not enabled:
            if diff_days is not None and diff_days >= 60:
                estado_auditoria = "Bloqueado >= 60 días (Etapa Offboarding)"
                accion_recomendada = "Verificar respaldo (OneDrive/Correo) y evaluar eliminación formal"
            else:
                estado_auditoria = "Bloqueado Reciente (< 60 días)"
                accion_recomendada = "Mantener período de retención/bloqueo conforme a política"
        else:
            # Habilitado
            if tipo_cuenta in ["Cuenta Administrativa / Privilegiada", "Cuenta de Servicio / Buzón Compartido"]:
                if diff_days is None or diff_days > 60:
                    estado_auditoria = "Cuenta Especial/Servicio con Inactividad"
                    accion_recomendada = "Excepción formal documentada; NO bloquear automáticamente"
                else:
                    estado_auditoria = "Cuenta Especial Activa"
                    accion_recomendada = "Control estricto de MFA y revisión semestral (PRO-06)"
            else:
                if diff_days is None:
                    estado_auditoria = "Nuevo / Sin Ingreso Registrado"
                    accion_recomendada = "Regla 5 días: Notificar solicitante; bloquear si no justifica necesidad"
                elif diff_days > 60:
                    estado_auditoria = "Inactivo > 60 días"
                    accion_recomendada = "Notificar jefatura y proceder a bloqueo justificado (PRO-06/PRO-07)"
                elif 30 <= diff_days <= 60:
                    estado_auditoria = "Alerta de Inactividad (30-60 días)"
                    accion_recomendada = "Monitorear en lista de cuarentena/aviso preventivo"
                else:
                    estado_auditoria = "Activo Conforme (< 30 días)"
                    accion_recomendada = "Mantener conforme; recertificar periódicamente"

    output_rows.append({
        "id": u.get("id"),
        "displayName": u.get("displayName"),
        "userPrincipalName": u.get("userPrincipalName"),
        "userType": ut,
        "accountEnabled": "True" if enabled else "False",
        "tipo_clasificado": tipo_cuenta,
        "ultimo_acceso_fecha": dt.strftime("%Y-%m-%d %H:%M:%S") if dt else "Sin registro",
        "dias_inactividad_al_28_10_2026": str(diff_days) if diff_days is not None else "N/A",
        "estado_auditoria": estado_auditoria,
        "accion_recomendada_iso27001": accion_recomendada
    })

fieldnames = [
    "id", "displayName", "userPrincipalName", "userType", "accountEnabled",
    "tipo_clasificado", "ultimo_acceso_fecha", "dias_inactividad_al_28_10_2026",
    "estado_auditoria", "accion_recomendada_iso27001"
]

out_path = "output/auditoria_usuarios_2026-10-28.csv"
with open(out_path, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";")
    writer.writeheader()
    writer.writerows(output_rows)

print(f"Exportación exitosa generada en: {out_path} con {len(output_rows)} registros.")

# Conteos
from collections import Counter
counts = Counter(r["estado_auditoria"] for r in output_rows)
print("\nResumen de clasificación:")
for k, v in counts.most_common():
    print(f"  {k}: {v}")
