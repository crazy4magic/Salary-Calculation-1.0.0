# 🎧 DJ Payroll System Guide

This tool calculates how much to pay each DJ per month based on the shift schedule you paste in.

---

## 📂 Project Files

- `main.py` → Python script that reads the schedule and calculates payroll
- `alias_map.json` → Maps DJ nicknames to official names (e.g., "illi" → "DJ Illi")
- `april_schedule.txt` → Raw text version of DJ schedule input
- `output/` → Folder where `.csv` files are saved
- `monthly_payouts_25년_5월_정산.csv` → Auto-generated payment report

---

## 💡 How It Works

1. You paste your monthly DJ schedule into `april_schedule.txt`
2. The script finds DJ names, counts shifts, calculates gross and net pay
3. Each shift is ₩150,000  
   Tax: 3.3% withheld  
   Net = Gross × 0.967
4. At the bottom, it adds a row with totals: gross, tax, and net

---

## ▶️ How to Run It (No Terminal)

1. Open `main.py` in Cursor
2. Click the ▶️ **Run** button in the top right
3. The script will output a `.csv` file into the `output/` folder
4. Open the `.csv` in Google Sheets

---

## 🧪 If You Use Terminal (Optional)

```bash
cd "/Users/caleb/Desktop/Cursor Projects/salary calculation"
python main.py
pyenv global 3.11.8
## 🔀 Alias Map Format (`alias_map.json`)

```json
{
  "illi": "DJ Illi",
  "Ellia": "DJ Ellia",
  "bigma": "DJ Bigma",
  "민호": "DJ Drako"
}
```

You can add more nicknames here if needed.

## 🔀 Alias Map Format (`alias_map.json`)

```json
{
  "illi": "DJ Illi",
  "Ellia": "DJ Ellia",
  "bigma": "DJ Bigma",
  "민호": "DJ Drako"
}
```

You can add more nicknames here if needed.

## **🛠️ To-Do**

- Setup folder
    
- Create main.py
    
- Create alias_map.json
    
- Paste schedule into april_schedule.txt
    
- Add new DJs to alias map
    
- Automate monthly run

## 🚀 How to Use

1. Open `alias_map.json`  
   - Add any nicknames or alternate spellings for your DJs  
   - Example:
     ```json
     {
       "illi": "DJ Illi",
       "민호": "DJ Drako"
     }
     ```

2. Open `april_schedule.txt`  
   - Paste your raw DJ schedule for the month  
   - Example:
     ```
     4/4 금요일
     10시-11:30 illi
     11:30-12:45 Ellia
     ```

3. Run `main.py`  
   - In Cursor: open the file and click ▶️ **Run**  
   - OR in Terminal:
     ```bash
     cd "/Users/caleb/Desktop/Cursor Projects/salary calculation"
     python main.py
     ```

4. Check the `output/` folder  
   - You'll find a CSV file like:  
     `monthly_payouts_25년_5월_정산.csv`  
   - Open it with Google Sheets to see full payment details

5. Confirm the last row — it shows total shifts, gross, tax, and net payments
