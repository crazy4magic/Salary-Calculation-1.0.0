# DJ Payment Tracker

This project calculates DJ payments for each month based on how many shifts they worked.

## 📂 Files
- `main.py`: Script that processes schedules and outputs Excel files
- `alias_map.json`: Name alias map (e.g. 민호 = Drako = DJ Drake)
- `april_schedule.txt`: Raw input schedule
- `output/april_payouts.xlsx`: Auto-generated monthly payment report

## ⚙️ Usage
1. Add your schedule to `april_schedule.txt`
2. Run `main.py` inside Cursor
3. The output will be saved in `/output/april_payouts.xlsx`

## 👨‍💻 Example Alias Map
```json
{
  "Drako": "DJ Drako",
  "DJ Drako": "DJ Drako",
  "민호": "DJ Drako"
}
