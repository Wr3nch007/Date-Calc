from datetime import datetime, timedelta
from colorama import Fore, init

init(autoreset=True)

def calculate_dates():

    date_input = input("Enter the date (DD/MM/YY) or press Enter for today's date: ").strip()

    if date_input == "":
        given_date = datetime.today()
    else:
        try:
            given_date = datetime.strptime(date_input, "%d/%m/%y")
        except ValueError:
            print("Invalid date format. Use DD/MM/YY")
            return

    period_type = input("Is this Quarterly or Bi-Annual? (Q/B): ").strip().upper()

    if period_type == "Q":
        q_input = input("This date belongs to which Quarter? (1-4) [Press Enter for current quarter]: ").strip()
        quarter = int(q_input) if q_input else 1
        total_periods = 4
        days = 90
        label = "Q"

    elif period_type == "B":
        h_input = input("This date belongs to which Half? (1-2) [Press Enter for current half]: ").strip()
        quarter = int(h_input) if h_input else 1
        total_periods = 2
        days = 180
        label = "H"

    else:
        print("Invalid option")
        return

    start_date = given_date - timedelta(days=(quarter - 1) * days)

    print("\n------------------------------------------------------")
    print("{:<10} {:<15} {:<15} {:<15}".format("Period","Start Date","Expire Date","Status"))
    print("------------------------------------------------------")

    current_start = start_date

    for i in range(1, total_periods + 1):

        expire_date = current_start + timedelta(days=days)

        if i < quarter:
            status = Fore.LIGHTBLACK_EX + "Completed"
        elif i == quarter:
            status = Fore.GREEN + "<<< CURRENT >>>"
        else:
            status = Fore.YELLOW + "Upcoming"

        print("{:<10} {:<15} {:<15} {:<15}".format(
            f"{label}{i}",
            current_start.strftime("%d/%m/%Y"),
            expire_date.strftime("%d/%m/%Y"),
            status
        ))

        current_start = expire_date

    print("------------------------------------------------------")

calculate_dates()
