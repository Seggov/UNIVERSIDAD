import csv, io, json
from datetime import datetime

REF_DATE = datetime(2026, 10, 28)

with open("usuarios/exportUsers_2026-10-28(in).csv", "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()
header = lines[0].strip().split(",")

users = []
for line in lines[1:]:
    raw = line.strip()
    if not raw: continue
    if raw.startswith('"') and raw.endswith('"'): raw = raw[1:-1].replace('""', '"')
    row = list(csv.reader(io.StringIO(raw)))[0]
    users.append(dict(zip(header, row)))

members = [u for u in users if u.get("userType") == "Member"]
print(f"Total Members: {len(members)}")

mem_enabled = [u for u in members if u.get("accountEnabled") == "True"]
mem_disabled = [u for u in members if u.get("accountEnabled") == "False"]
print(f"  Habilitados (accountEnabled=True): {len(mem_enabled)}")
print(f"  Deshabilitados (accountEnabled=False): {len(mem_disabled)}")

# Let's inspect inactivity for enabled members
inact_gt_60 = []
inact_30_60 = []
active_lt_30 = []
never_signed = []

for u in mem_enabled:
    s_raw = u.get("signInActivity", "").strip()
    s_obj = json.loads(s_raw) if s_raw else {}
    dt_str = s_obj.get("lastSuccessfulSignInDateTime") or s_obj.get("lastSignInDateTime") or s_obj.get("lastNonInteractiveSignInDateTime")
    if not dt_str:
        never_signed.append(u)
    else:
        dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00")).replace(tzinfo=None)
        days = (REF_DATE - dt).days
        if days > 60:
            inact_gt_60.append((u, days))
        elif 30 <= days <= 60:
            inact_30_60.append((u, days))
        else:
            active_lt_30.append((u, days))

print(f"\nHabilitados (Total {len(mem_enabled)}):")
print(f"  - Inactivos > 60 días: {len(inact_gt_60)}")
print(f"  - Inactivos 30 a 60 días: {len(inact_30_60)}")
print(f"  - Activos < 30 días: {len(active_lt_30)}")
print(f"  - Sin inicio de sesión registrado: {len(never_signed)}")

# Let's inspect disabled members
dis_gt_60 = []
dis_lt_60 = []
dis_no_date = []

for u in mem_disabled:
    s_raw = u.get("signInActivity", "").strip()
    s_obj = json.loads(s_raw) if s_raw else {}
    dt_str = s_obj.get("lastSuccessfulSignInDateTime") or s_obj.get("lastSignInDateTime") or s_obj.get("lastNonInteractiveSignInDateTime")
    if not dt_str:
        dis_no_date.append(u)
    else:
        dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00")).replace(tzinfo=None)
        days = (REF_DATE - dt).days
        if days >= 60:
            dis_gt_60.append((u, days))
        else:
            dis_lt_60.append((u, days))

print(f"\nDeshabilitados (Total {len(mem_disabled)}):")
print(f"  - Con último login >= 60 días: {len(dis_gt_60)}")
print(f"  - Con último login < 60 días: {len(dis_lt_60)}")
print(f"  - Sin fecha de login registrada: {len(dis_no_date)}")

