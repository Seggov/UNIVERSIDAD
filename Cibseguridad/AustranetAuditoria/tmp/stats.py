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

total = len(users)

# Let's read from our generated audit CSV output/auditoria_usuarios_2026-10-28.csv
audit_rows = []
with open("output/auditoria_usuarios_2026-10-28.csv", "r", encoding="utf-8-sig") as f:
    r = csv.DictReader(f, delimiter=";")
    for row in r:
        audit_rows.append(row)

from collections import Counter
counts = Counter(r["estado_auditoria"] for r in audit_rows)

print("Total audit rows:", len(audit_rows))
for k, v in counts.most_common():
    pct = (v / total) * 100
    print(f"{k}: {v} ({pct:.1f}%)")
