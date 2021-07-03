
import csv
import os

with open('Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)

    months_counter = 0
    total_amount = 0.00
    current_amount = 0.00
    previous_amount = 0.00
    change = 0.00
    change_counter = 0
    max_profit = 0.00
    max_profit_date = ""
    min_profit = 0.00
    min_profit_date = ""
    next(csv_reader)
    average_change = 0.00

    for index, row in enumerate(csv_reader):
        months_counter += 1
        total_amount += float(row[1])
        current_amount = float(row[1])
        if index > 0:
            change = previous_amount- current_amount
            change_counter +=1
        previous_amount = current_amount
        if float(row[1]) > max_profit:
            max_profit = float(row[1])
            max_profit_date = str(row[0])
        if float(row[1]) < min_profit:
            min_profit = float(row[1])
            min_profit_date = str(row[0])

    average_change = change / change_counter






output = (
'''  Financial Analysis
----------------------------
Total Months: %d
Total: $%.2f
Average  Change: $%.2f
Greatest Increase in Profits: %s ($%.2f)
Greatest Decrease in Profits: %s ($%.2f)'''
)

print(output % (months_counter, total_amount, average_change, max_profit_date, max_profit, min_profit_date, min_profit ) )

file = open("analysis/results.txt", "w")
file.write(output % (months_counter, total_amount, average_change, max_profit_date, max_profit, min_profit_date, min_profit ))
file.close()
