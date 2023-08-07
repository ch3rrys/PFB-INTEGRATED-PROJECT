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

# Initialize a list to store the differences in net profit
profit_differences = []

# Initialize variables to keep track of the highest increment
highest_increment_day = None
highest_increment_amount = 0

# Iterate through each list object to compare differences in net profit
for i in range(1, len(net_profit_data)):
    # Calculate the difference in net profit between the current and previous day
    difference = net_profit_data[i][1] - net_profit_data[i - 1][1]
    
    # Append the difference to the list
    profit_differences.append([net_profit_data[i][0], difference])

     # Check if the difference is higher than the highest increment
    if difference > highest_increment_amount:
        highest_increment_day = net_profit_data[i][0]
        highest_increment_amount = difference

