from pathlib import Path
import csv

def calculate_overheads():
    '''
    function reads overhead data from CSV file and identifies the category with the highest value.
    required parameters : none
    '''
    # create a file to csv file.
    fp_2 = Path.cwd()/"csv_reports/overheads.csv"

    with fp_2.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header
            
        overheads = []

        for row in reader:
            overheads.append([row[0],float(row[1])])  
 
    highest_category = ""
    highest_value = 0.00

    for category, value in overheads:
            if value > highest_value:
                highest_value = value 
                highest_category = category

    cap_highest_category = highest_category.upper()

    output = f'[HIGHEST OVERHEAD] {cap_highest_category}: USD{highest_value:.2f}\n'
    return output