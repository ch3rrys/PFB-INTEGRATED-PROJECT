from pathlib import Path
import csv

def calculate_profit_n_loss():

    # create a file to csv file.
    fp_3 = Path.cwd()/"csv_reports/profits_and_loss.csv"

    with fp_3.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        profit_n_loss=[]

        for row in reader:
            profit_n_loss.append([row[0],row[1],row[2],row[3],row[4]])  

        return profit_n_loss
print(calculate_profit_n_loss())