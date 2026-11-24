import csv, io, json
from datetime import datetime

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

mem_enabled = [u for u in users if u.get("userType") == "Member" and u.get("accountEnabled") == "True"]

never_signed = []
for u in mem_enabled:
    s = u.get("signInActivity", "").strip()
    so = json.loads(s) if s else {}
    dt_str = so.get("lastSuccessfulSignInDateTime") or so.get("lastSignInDateTime") or so.get("lastNonInteractiveSignInDateTime")
    if not dt_str:
        never_signed.append(u)

print("Miembros habilitados sin login registrado (11):")
for u in never_signed:
    print(f"  - {u['displayName']} | {u['userPrincipalName']}")
