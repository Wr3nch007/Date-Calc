# Date-Calc
Quarterly &amp; Bi-Annuel date calculation

# Quarter Schedule Calculator

A simple Python CLI tool to calculate quarterly or bi-annual schedules from a given date.

## Features

- Supports **Quarterly (Q1–Q4)** and **Bi-Annual (H1–H2)** calculations
- Accepts date format **DD/MM/YY**
- Press **Enter** to use today's date
- Color highlighted output in terminal
- Shows:
  - Completed periods
  - Current period
  - Upcoming periods

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/quarter-schedule-calculator.git
cd quarter-schedule-calculator
```

## Install Dependencies
pip install -r requirements.txt

## Useage
python quarter_calc.py

## Example
Enter the date (DD/MM/YY) or press Enter for today's date:
Is this Quarterly or Bi-Annual? (Q/B): Q
This date belongs to which Quarter? (1-4) [Press Enter for Q1]: 2

## Output
------------------------------------------------------
Period     Start Date      Expire Date     Status
------------------------------------------------------
Q1         11/03/2026      09/06/2026      Completed
Q2         09/06/2026      07/09/2026      <<< CURRENT >>>
Q3         07/09/2026      06/12/2026      Upcoming
Q4         06/12/2026      06/03/2027      Upcoming
------------------------------------------------------

## Author 
AK
