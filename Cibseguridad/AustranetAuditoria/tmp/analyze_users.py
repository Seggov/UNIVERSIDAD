import csv
import io
import json
from datetime import datetime

# Reference date is the export date: 2026-10-28
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
    reader = csv.reader(io.StringIO(raw))
    row = list(reader)[0]
    user = dict(zip(header, row))
    users.append(user)

print(f"Total usuarios en el CSV: {len(users)}")

user_types = {}
account_enabled = {}
creation_types = {}
has_signin = 0
no_signin = 0

# For active members
members_active = []
members_disabled = []
guests = []

for u in users:
    ut = u.get("userType", "").strip() or "Empty"
    ae = u.get("accountEnabled", "").strip()
    ct = u.get("creationType", "").strip() or "Empty"
    
    user_types[ut] = user_types.get(ut, 0) + 1
    account_enabled[ae] = account_enabled.get(ae, 0) + 1
    creation_types[ct] = creation_types.get(ct, 0) + 1
    
    signin_str = u.get("signInActivity", "").strip()
    signin_obj = {}
    if signin_str:
        try:
            signin_obj = json.loads(signin_str)
        except Exception:
            pass
    u["parsed_signin"] = signin_obj
    
    if signin_obj:
        has_signin += 1
    else:
        no_signin += 1

print("\n--- Distribución por userType ---")
for k, v in user_types.items():
    print(f"  {k}: {v}")

print("\n--- Distribución por accountEnabled ---")
for k, v in account_enabled.items():
    print(f"  {k}: {v}")

print("\n--- Con actividad de signInActivity registrada ---")
print(f"  Con signInActivity: {has_signin}")
print(f"  Sin signInActivity (vacío): {no_signin}")

# Analyze Members vs Guests
members = [u for u in users if u.get("userType") == "Member"]
guests = [u for u in users if u.get("userType") == "Guest"]

print(f"\nTotal Members: {len(members)}")
print(f"Total Guests: {len(guests)}")

# Analyze Members
mem_enabled = [u for u in members if u.get("accountEnabled") == "True"]
mem_disabled = [u for u in members if u.get("accountEnabled") == "False"]
print(f"  Members Enabled (Activos): {len(mem_enabled)}")
print(f"  Members Disabled (Bloqueados/Deshabilitados): {len(mem_disabled)}")

# Inactivity analysis for Enabled Members
mem_never_signed_in = []
mem_with_dates = []

for u in mem_enabled:
    s = u["parsed_signin"]
    # Check lastSignInDateTime or lastSuccessfulSignInDateTime
    dt_str = s.get("lastSuccessfulSignInDateTime") or s.get("lastSignInDateTime") or s.get("lastNonInteractiveSignInDateTime")
    if not dt_str:
        mem_never_signed_in.append(u)
    else:
        # parse ISO date
        try:
            dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00")).replace(tzinfo=None)
            diff_days = (REF_DATE - dt).days
            mem_with_dates.append((u, dt, diff_days))
        except Exception as e:
            mem_never_signed_in.append(u)

print(f"\n--- Miembros Habilitados (Enabled = True) ({len(mem_enabled)}) ---")
print(f"  Sin ningún registro de inicio de sesión: {len(mem_never_signed_in)}")
print(f"  Con fecha de inicio de sesión: {len(mem_with_dates)}")

# Inactivity buckets for enabled members
inactive_gt_60 = [x for x in mem_with_dates if x[2] > 60]
inactive_30_60 = [x for x in mem_with_dates if 30 <= x[2] <= 60]
active_lt_30 = [x for x in mem_with_dates if x[2] < 30]

print(f"    Inactivos > 60 días: {len(inactive_gt_60)}")
print(f"    Inactivos 30 a 60 días: {len(inactive_30_60)}")
print(f"    Activos < 30 días: {len(active_lt_30)}")

# Disabled members analysis
dis_never = []
dis_with_dates = []
for u in mem_disabled:
    s = u["parsed_signin"]
    dt_str = s.get("lastSuccessfulSignInDateTime") or s.get("lastSignInDateTime") or s.get("lastNonInteractiveSignInDateTime")
    if not dt_str:
        dis_never.append(u)
    else:
        try:
            dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00")).replace(tzinfo=None)
            diff_days = (REF_DATE - dt).days
            dis_with_dates.append((u, dt, diff_days))
        except Exception:
            dis_never.append(u)

print(f"\n--- Miembros Deshabilitados (Enabled = False) ({len(mem_disabled)}) ---")
print(f"  Sin registro de inicio de sesión: {len(dis_never)}")
print(f"  Con fecha de inicio de sesión: {len(dis_with_dates)}")
dis_gt_60 = [x for x in dis_with_dates if x[2] > 60]
print(f"    Cuentas deshabilitadas con último login hace > 60 días (candidatas offboarding/eliminación): {len(dis_gt_60)}")
