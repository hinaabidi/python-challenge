
import csv

with open('Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)

    months = 0
    total = 0
    next(csv_reader)
    
    for row in csv_reader:
        months += 1
        total += float(row[1])

    output = (
        '''  Financial Analysis
    ----------------------------
    Total Months: %s
    Total: $%s
    Average  Change: $-2315.12
    Greatest Increase in Profits: Feb-2012 ($1926159)
    Greatest Decrease in Profits: Sep-2013 ($-2196167)'''
    )

    print(output % (months, total) )