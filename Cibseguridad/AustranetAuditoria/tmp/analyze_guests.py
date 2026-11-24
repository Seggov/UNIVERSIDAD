import csv, io, json
from datetime import datetime

REF_DATE = datetime(2026, 10, 28)

with open("usuarios/exportUsers_2026-10-28(in).csv", "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()
header = lines[0].strip().split(",")

guests = []
for line in lines[1:]:
    raw = line.strip()
    if not raw: continue
    if raw.startswith('"') and raw.endswith('"'): raw = raw[1:-1].replace('""', '"')
    row = list(csv.reader(io.StringIO(raw)))[0]
    u = dict(zip(header, row))
    if u.get("userType") == "Guest":
        s = u.get("signInActivity", "").strip()
        u["parsed_signin"] = json.loads(s) if s else {}
        guests.append(u)

g_enabled = [u for u in guests if u.get("accountEnabled") == "True"]
g_disabled = [u for u in guests if u.get("accountEnabled") == "False"]
print(f"Total Guests: {len(guests)}")
print(f"  Guests Enabled: {len(g_enabled)}")
print(f"  Guests Disabled: {len(g_disabled)}")

g_never = []
g_with_dates = []
for u in g_enabled:
    s = u["parsed_signin"]
    dt_str = s.get("lastSuccessfulSignInDateTime") or s.get("lastSignInDateTime") or s.get("lastNonInteractiveSignInDateTime")
    if not dt_str:
        g_never.append(u)
    else:
        try:
            dt = datetime.fromisoformat(dt_str.replace("Z", "+00:00")).replace(tzinfo=None)
            diff_days = (REF_DATE - dt).days
            g_with_dates.append((u, dt, diff_days))
        except Exception:
            g_never.append(u)

print(f"  Guests Enabled sin login: {len(g_never)}")
print(f"  Guests Enabled con fecha: {len(g_with_dates)}")
g_gt_60 = [x for x in g_with_dates if x[2] > 60]
print(f"  Guests Enabled > 60 días inactivos: {len(g_gt_60)}")
print(f"  Guests Enabled < 60 días: {len(g_with_dates) - len(g_gt_60)}")
