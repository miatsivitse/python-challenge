import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print (csvreader)

    csv_header = next(csvreader)
    print(f"csvheader: {csv_header}")

    # for row in csvreader:
    #     print(row[0])

    date = 0
    for row in open('budget_data.csv'):
        date += 1
        print (date)

total_months = date
total_profit = 
average_change = 

print ("Financial Analysis")
print ("------------------")
print ("Total Months: " + str(total_months))
print("Total: $" + str(total_profit))
print (f"Total: ${average_change}")
