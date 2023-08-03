from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"cash_on_hand.csv"
fp_2 = Path.cwd()/"overheads.csv"
fp_3 = Path.cwd()/"profits_and_loss.csv"

# read the csv file to append profit and quantity from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    cash_on_hand=[]

    for row in reader:
        cash_on_hand.append([row[0],row[1]])  

    print(cash_on_hand)

with fp_2.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header
    
    overheads=[]

    for row in reader:
        overheads.append([row[0],row[1]])  

    print(overheads)

with fp_3.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    profit_n_loss=[]

    for row in reader:
        profit_n_loss.append([row[0],row[1],row[2],row[3],row[4]])  

    print(profit_n_loss)