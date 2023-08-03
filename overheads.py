from pathlib import Path
import csv

# create a file to csv file.
fp_2 = Path.cwd()/"csv_reports/overheads.csv"

with fp_2.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header
    
    overheads=[]

    for row in reader:
        overheads.append([row[0],row[1]])  

    print(overheads)