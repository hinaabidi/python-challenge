
import csv

with open('Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)

    months = 0
    total = 0.00
    max_profit = 0.00
    max_profit_date = ""
    profit = 0.00
    loss = 0.00
    min_profit = 0.00
    min_profit_date = ""
    next(csv_reader)
    
    for row in csv_reader:
        months += 1
        total += float(row[1])
        if float(row[1]) > max_profit:
            max_profit = float(row[1])
            max_profit_date = str(row[0])
        if float(row[1]) < min_profit:
            min_profit = float(row[1])
            min_profit_date = str(row[0])
    

    output = (
    '''  Financial Analysis
    ----------------------------
    Total Months: %s
    Total: $%.2f
    Average  Change: $-2315.12
    Greatest Increase in Profits: %s ($%.2f)
    Greatest Decrease in Profits: %s ($%.2f)'''
    )

    print(output % (months, total, max_profit_date, max_profit, min_profit_date, min_profit ) )