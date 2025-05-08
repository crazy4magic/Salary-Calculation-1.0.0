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
    if not line.strip():  # Skip empty lines
        continue
    # Split line by & for cases where DJs work together
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
for dj, count in sorted(dj_counts.items()):  # Sort by DJ name
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

# Add totals row
totals = {
    "DJ Name": "합계",
    "Number of Shifts": df["Number of Shifts"].sum(),
    "Gross Pay": df["Gross Pay"].sum(),
    "Tax Amount": df["Tax Amount"].sum(),
    "Net Pay": df["Net Pay"].sum()
}
df = pd.concat([df, pd.DataFrame([totals])], ignore_index=True)

# Create output filename with Korean date format
now = datetime.now()
filename = f"monthly_payouts_{now.year % 100}년_{now.month}월_정산.csv"
output_path = os.path.join('output', filename)

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

# Save to CSV
df.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"✅ CSV saved to '{output_path}'") 