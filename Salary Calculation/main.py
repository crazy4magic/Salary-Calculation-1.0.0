import re
import json
import pandas as pd
from datetime import datetime
import os

# Load alias map
with open('alias_map.json', 'r', encoding='utf-8') as f:
    alias_map = json.load(f)

# Load schedule text
with open('april_schedule.txt', 'r', encoding='utf-8') as f:
    schedule = f.read()

# Normalize and count DJ appearances
dj_counts = {}

for line in schedule.splitlines():
    parts = re.split(r'[,&]', line)
    for part in parts:
        name = part.strip()
        if not name:
            continue
        # Normalize via alias_map
        normalized = next((real for alias, real in alias_map.items() if name.lower() == alias.lower()), None)
        if not normalized:
            normalized = name.title()
        dj_counts[normalized] = dj_counts.get(normalized, 0) + 1

# Build DataFrame
rows = []
for dj, count in dj_counts.items():
    gross = count * 150000
    tax = int(gross * 0.033)
    net = gross - tax
    rows.append({
        "DJ Name": dj,
        "Number of Shifts": count,
        "Gross Pay": gross,
        "Tax Amount": tax,
        "Net Pay": net
    })

df = pd.DataFrame(rows)

# Excel with tab named like "25년 4월 정산"
now = datetime.now()
sheet_name = f"{now.year % 100}년 {now.month}월 정산"
output_path = 'output/monthly_payouts.xlsx'

os.makedirs('output', exist_ok=True)

if os.path.exists(output_path):
    with pd.ExcelWriter(output_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)
else:
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"✅ Excel saved to '{output_path}' in tab '{sheet_name}'")