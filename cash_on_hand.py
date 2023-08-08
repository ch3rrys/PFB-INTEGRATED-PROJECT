from pathlib import Path
import csv

def calculate_cash_on_hand():
    '''
    function reads cash flow data from CSV file and analyses it to identify cash surpluses and deficits on different days.
    required parameters : none
    '''
    # create a file to csv file.
    fp = Path.cwd()/"csv_reports/cash_on_hand.csv"

    # initialise list to store all the values of cash on hand
    cash_on_hand = []

    # read the csv file to append profit and quantity from the csv.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        for row in reader:
            cash_on_hand.append([int(row[0]), int(row[1])])

    # initialise list to store values for cash deficit days
    cash_deficit = []

    # initialise list to store highest cash surplus, we put day 0 values in first
    highest_surplus = [cash_on_hand[0][0], 0]

    # iterate through each list object to compare difference in cash
    for i in range(1, len(cash_on_hand)):
        # calculate the surplus as the difference between current and previous cash values
        surplus = cash_on_hand[i][1] - cash_on_hand[i - 1][1]
        
        if surplus > 0:
            # check if surplus is higher than the highest surplus
            if surplus > highest_surplus[1]:
                highest_surplus[0] = cash_on_hand[i][0]
                highest_surplus[1] = surplus
        else:
            # append deficit to deficit list
            cash_deficit.append([cash_on_hand[i][0], cash_on_hand[i][1]])

    # print results; if deficit list is empty (no deficit) we print cash surplus
    output = ""
    if not cash_deficit:
        output += "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
        output += f"[HIGHEST CASH SURPLUS] DAY: {highest_surplus[0]}, AMOUNT: USD{highest_surplus[1]}\n"
    else:
        for deficit in cash_deficit:
            output += f"[CASH DEFICIT] DAY: {deficit[0]}, AMOUNT: USD{deficit[1]}\n"

    return output