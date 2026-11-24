import csv, io
from collections import Counter

with open("usuarios/exportUsers_2026-10-28(in).csv", "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()
header = lines[0].strip().split(",")
users = []
for line in lines[1:]:
    raw = line.strip()
    if not raw: continue
    if raw.startswith('"') and raw.endswith('"'): raw = raw[1:-1].replace('""', '"')
    users.append(dict(zip(header, list(csv.reader(io.StringIO(raw)))[0])))

print("Total:", len(users))
print("userType:", Counter(u["userType"] for u in users))
print("creationType:", Counter(u["creationType"] for u in users))
print("Sample Guests:", [(u["displayName"], u["userPrincipalName"]) for u in users if u["userType"]=="Guest"][:5])
print("Sample Members:", [(u["displayName"], u["userPrincipalName"]) for u in users if u["userType"]=="Member"][:5])
domains_mem = Counter(u["userPrincipalName"].split("@")[-1].lower() for u in users if u["userType"]=="Member")
print("Member domains:", domains_mem)
mem_inv = [u for u in users if u["userType"]=="Member" and u["creationType"]=="Invitation"]
print("Member with Invitation:", len(mem_inv), [(u["displayName"], u["userPrincipalName"]) for u in mem_inv[:10]])
guest_no_inv = [u for u in users if u["userType"]=="Guest" and u["creationType"]!="Invitation"]
print("Guest without Invitation:", len(guest_no_inv), [(u["displayName"], u["userPrincipalName"], u["creationType"]) for u in guest_no_inv[:10]])

