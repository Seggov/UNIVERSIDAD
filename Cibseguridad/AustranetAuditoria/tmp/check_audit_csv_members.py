import csv
from collections import Counter

members = []
with open("output/auditoria_usuarios_2026-10-28.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f, delimiter=";")
    for row in reader:
        if row["userType"] == "Member":
            members.append(row)

print("Total Members in audit CSV:", len(members))
c = Counter(r["estado_auditoria"] for r in members)
for k, v in c.most_common():
    print(f"  {k}: {v} ({v/len(members)*100:.1f}%)")

print("\nDesglose por grupos de riesgo:")
rojo = [r for r in members if r["estado_auditoria"] in ["Inactivo > 60 días", "Bloqueado >= 60 días (Etapa Offboarding)", "Cuenta Especial/Servicio con Inactividad"]]
amarillo = [r for r in members if r["estado_auditoria"] in ["Nuevo / Sin Ingreso Registrado", "Alerta de Inactividad (30-60 días)"]]
verde = [r for r in members if r["estado_auditoria"] in ["Activo Conforme (< 30 días)", "Bloqueado Reciente (< 60 días)", "Cuenta Especial Activa"]]

print(f"Rojo: {len(rojo)} ({len(rojo)/len(members)*100:.1f}%)")
print(f"Amarillo: {len(amarillo)} ({len(amarillo)/len(members)*100:.1f}%)")
print(f"Verde: {len(verde)} ({len(verde)/len(members)*100:.1f}%)")
print("Suma:", len(rojo) + len(amarillo) + len(verde))
