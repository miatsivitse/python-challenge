import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")
output_path = os.path.join("Analysis", "PyBank_results.txt")

print ("Financial Analysis")
print ("------------------")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    months = csvreader
    def month_year(month):
        month_count = 0
        for i in month:
            month_count +=1

        return month_count
    var=month_year(months)
    print("Total Months:" + str(var))

    

with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------\n")
    txtfile.write("Total Months:" + str(var) + "\n")
    txtfile.close()

# total_profit = 
# average_change = 
# profit_increase = 
# profit_decrease = 

# print ("Total Months: " + int(total_months))
# print("Total: $" + str(total_profit))
# print (f"Total: ${average_change}")
