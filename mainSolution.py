from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"TimeSheetAndSales.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header