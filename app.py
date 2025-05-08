from flask import Flask, render_template, request, send_file, jsonify
import pandas as pd
from datetime import datetime
import os
import re
import json

app = Flask(__name__)

# Load alias map
with open('alias_map.json', 'r', encoding='utf-8') as f:
    alias_map = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    schedule = request.form['schedule']
    
    # Normalize and count DJ appearances
    dj_counts = {}
    
    for line in schedule.splitlines():
        if not line.strip():  # Skip empty lines
            continue
            
        # Skip lines that don't contain time patterns
        if not re.search(r'\d{1,2}[:시]', line):
            continue
            
        # Extract the name part after the time
        # This regex looks for time patterns like "10:00 - 11:30" or "10시-11:30" followed by the name
        match = re.search(r'(?:\d{1,2}[:시]|\d{1,2}:\d{2}).*?(?:[-–—]|~).*?(?:\d{1,2}[:시]|\d{1,2}:\d{2}|마감)\s*(.*?)(?:\s*$)', line)
        if match:
            name_part = match.group(1).strip()
            # Split by x, &, or comma for multiple DJs
            parts = re.split(r'[x&,]', name_part)
            for part in parts:
                name = part.strip()
                if not name:
                    continue
                # Remove any numbers from the name
                name = re.sub(r'\d+', '', name).strip()
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

    # Convert DataFrame to HTML table
    table_html = df.to_html(classes='table table-striped', index=False)
    
    return jsonify({
        'table': table_html,
        'filename': filename
    })

@app.route('/download/<filename>')
def download(filename):
    return send_file(
        os.path.join('output', filename),
        as_attachment=True,
        download_name=filename
    )

if __name__ == '__main__':
    app.run(debug=True) 