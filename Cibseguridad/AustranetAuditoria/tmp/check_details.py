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

# Let's inspect the 12 disabled without login date
dis_no_date = []
for u in members:
    if u.get("accountEnabled") == "False":
        s_raw = u.get("signInActivity", "").strip()
        s_obj = json.loads(s_raw) if s_raw else {}
        dt_str = s_obj.get("lastSuccessfulSignInDateTime") or s_obj.get("lastSignInDateTime") or s_obj.get("lastNonInteractiveSignInDateTime")
        if not dt_str:
            dis_no_date.append(u)

print(f"Deshabilitados sin login date ({len(dis_no_date)}):")
for u in dis_no_date:
    print(f"  {u['displayName']} | {u['userPrincipalName']}")

# Let's inspect the 11 enabled without login date
en_no_date = []
for u in members:
    if u.get("accountEnabled") == "True":
        s_raw = u.get("signInActivity", "").strip()
        s_obj = json.loads(s_raw) if s_raw else {}
        dt_str = s_obj.get("lastSuccessfulSignInDateTime") or s_obj.get("lastSignInDateTime") or s_obj.get("lastNonInteractiveSignInDateTime")
        if not dt_str:
            en_no_date.append(u)

print(f"\nHabilitados sin login date ({len(en_no_date)}):")
for u in en_no_date:
    print(f"  {u['displayName']} | {u['userPrincipalName']}")
