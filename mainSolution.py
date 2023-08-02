from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"cash-on-hand.csv"
fp_2 = Path.cwd()/"operating expenses.csv"
fp_3 = Path.cwd()/"profits and loss.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header
with fp_2.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header
with fp_3.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

