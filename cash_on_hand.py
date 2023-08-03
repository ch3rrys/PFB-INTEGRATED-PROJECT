from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"csv_reports/cash_on_hand.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    cash_on_hand=[]

    for row in reader:
        cash_on_hand.append([row[0],row[1]])  

    print(cash_on_hand)