from pathlib import Path
import csv

def calculate_profit_loss():
    '''
    function reads profit and loss data from CSV file and analyses it to identify cash surpluses and deficits on different days.
    required parameters : none
    '''
    # create a file to csv file
    fp = Path.cwd() / "csv_reports/profits_and_loss.csv"

    # initialise a list to store all the values of net profit
    net_profit_data = []

    # read the CSV file to append "Day" and "Net Profit" values
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        for row in reader:
            net_profit_data.append([int(row[0]), int(row[4])])

    # calculate the difference in net profit between each day and the previous day
    differences = [net_profit_data[i][1] - net_profit_data[i - 1][1] for i in range(1, len(net_profit_data))]

    # calculate the highest net profit surplus
    highest_surplus = max(differences)

    # initialise a list to store the cash deficit values
    cash_deficits = []

    # iterate through each list object to find cash deficit values (negative differences)
    for i in range(1, len(net_profit_data)):
        # Calculate the difference in net profit between the current and previous day
        difference = net_profit_data[i][1] - net_profit_data[i - 1][1]

    # only consider cash deficit (negative difference)
        if difference < 0:
            cash_deficits.append([net_profit_data[i][0], abs(difference)])

    # print results; if deficit list is empty (no deficit) we print cash surplus
    output = ""
    if not cash_deficits:
        output += "[NET PROFIT HIGHEST SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
        output += f"[HIGHEST CASH SURPLUS] DAY: {highest_surplus[0]}, AMOUNT: USD{highest_surplus[1]}\n"
    else:
        for deficit in cash_deficits:
            output += f"[PROFIT DEFICIT] DAY: {deficit[0]}, AMOUNT: USD{deficit[1]}\n"
    
    return output
