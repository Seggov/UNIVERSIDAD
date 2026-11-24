import csv
import io
import json

with open("usuarios/exportUsers_2026-10-28(in).csv", "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

print("Total lines:", len(lines))
header = lines[0].strip().split(",")
print("Header:", header)

parsed_rows = []
for idx, line in enumerate(lines[1:], start=1):
    raw = line.strip()
    if not raw:
        continue
    if raw.startswith('"') and raw.endswith('"'):
        raw = raw[1:-1].replace('""', '"')
    
    reader = csv.reader(io.StringIO(raw))
    row = list(reader)[0]
    parsed_rows.append(row)

print("Parsed count:", len(parsed_rows))
print("Sample parsed row 0:")
for k, v in zip(header, parsed_rows[0]):
    print(f"  {k}: {v}")

print("Sample parsed row 1:")
for k, v in zip(header, parsed_rows[1]):
    print(f"  {k}: {v}")
