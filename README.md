# DJ Payroll Calculator

A desktop application for calculating DJ payroll based on their shifts. The application processes schedule text and generates detailed payroll reports.

## Features

- Process schedule text with DJ shifts
- Calculate gross pay, tax deductions, and net pay
- Generate CSV reports with Korean date format
- Support for multiple DJs per shift
- Automatic browser launch for web interface
- Dark mode support
- Offline functionality

## Installation

### Option 1: Using the Command File (Recommended)

1. Copy `dj_payroll_calculator.command` to your Applications folder:
   ```bash
   cp dj_payroll_calculator.command /Applications/
   ```

2. Make it executable:
   ```bash
   chmod +x /Applications/dj_payroll_calculator.command
   ```

3. Double-click the file in Applications to run

### Option 2: Building from Source

1. Ensure you have Python 3.11.8 installed via pyenv:
   ```bash
   pyenv install 3.11.8
   pyenv global 3.11.8
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Build the application:
   ```bash
   python setup.py py2app
   ```

## Usage

1. Launch the application by double-clicking `dj_payroll_calculator.command` in Applications
2. The application will:
   - Open Terminal (required for the Flask server)
   - Launch your default web browser to the calculator interface
3. Paste your schedule text into the input field
4. Click "Calculate" to process the schedule
5. View the results in the browser
6. Download the CSV report from the Documents/DJ Payroll folder

## Schedule Format

The application supports various time formats:
- `10:00 - 11:30 DJ Name`
- `10시-11:30 DJ Name`
- `10:00~마감 DJ Name`

Multiple DJs can be specified using:
- `DJ1 & DJ2`
- `DJ1, DJ2`
- `DJ1 x DJ2`

## Output

The application generates a CSV file in your Documents/DJ Payroll folder with:
- DJ Name
- Number of Shifts
- Gross Pay (150,000 won per shift)
- Tax Amount (3.3%)
- Net Pay

## Requirements

- macOS 10.10 or later
- Python 3.11.8
- Required Python packages (automatically installed):
  - Flask
  - pandas
  - numpy
  - jinja2
  - werkzeug
  - click
  - itsdangerous
  - markupsafe
  - dateutil
  - pytz
  - six

## Troubleshooting

1. If the application doesn't start:
   - Check if Terminal has permission to run the script
   - Ensure Python 3.11.8 is installed
   - Verify all required packages are installed

2. If the web interface doesn't open:
   - Check if port 5000 is available
   - Try accessing http://127.0.0.1:5000 manually

3. If the CSV isn't generated:
   - Check if you have write permissions in Documents/DJ Payroll
   - Verify the schedule format is correct

## License

© 2024 DJ Payroll Calculator
