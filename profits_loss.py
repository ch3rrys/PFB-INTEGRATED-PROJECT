from pathlib import Path
import csv

# Create a file path to the CSV file
fp = Path.cwd() / "csv_reports/profits_and_loss.csv"

# Initialize a list to store all the values of net profit
net_profit_data = []

# Read the CSV file to append "Day" and "Net Profit" values
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header

    for row in reader:
        net_profit_data.append([int(row[0]), int(row[4])])

# Calculate the difference in net profit between each day and the previous day
differences = [net_profit_data[i][1] - net_profit_data[i - 1][1] for i in range(1, len(net_profit_data))]

# Calculate the highest net profit surplus
highest_surplus = max(differences)

# Initialize a list to store the cash deficit values
cash_deficits = []

# Iterate through each list object to find cash deficit values (negative differences)
for i in range(1, len(net_profit_data)):
    # Calculate the difference in net profit between the current and previous day
    difference = net_profit_data[i][1] - net_profit_data[i - 1][1]

# Only consider cash deficit (negative difference)
    if difference < 0:
        cash_deficits.append([net_profit_data[i][0], difference])

# Print cash deficit results
#print results; if deficit list is empty (no deficit) we print cash surplus
if not cash_deficits:
    print("[NET PROFIT HIGHEST SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    print(f"[HIGHEST CASH SURPLUS] DAY: {highest_surplus[0]}, AMOUNT: USD{highest_surplus[1]}")
else:
    for deficit in cash_deficits:
         print(f"[CASH DEFICIT] DAY: {deficit[0]}, AMOUNT: USD{deficit[1]}")
if cash_deficits:
    for deficit in cash_deficits:
        print(f"[CASH DEFICIT] DAY: {deficit[0]}, AMOUNT: USD{deficit[1]}")
else:
    print("No cash deficits found.")