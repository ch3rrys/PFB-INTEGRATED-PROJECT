from pathlib import Path
import csv

def calculate_overheads():
    '''
    function reads overhead data from CSV file and identifies the category with the highest value.
    required parameters : none
    '''
    # create a file to csv file
    fp = Path.cwd()/"csv_reports/overheads.csv"

    # initialise list to store all the values of overheads    
    overheads = []

    # read the csv file to append profit and quantity from the csv
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        for row in reader:
            overheads.append([row[0],float(row[1])])

    # initialise variables to track the highest overhead category and value
    highest_category = ""
    highest_value = 0.00

    # iterate through overheads to find the highest category and value
    for category, value in overheads:
            if value > highest_value:
                highest_value = value 
                highest_category = category

    # capitalise the highest category for formatting
    cap_highest_category = highest_category.upper()
    
    # format the output string with the highest category and value
    output = f'[HIGHEST OVERHEAD] {cap_highest_category}: {highest_value:.2f}%\n'
    return output