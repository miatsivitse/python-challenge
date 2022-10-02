import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")
output_path = os.path.join("Analysis", "PyBank_results.txt")

print ("Financial Analysis")
print ("------------------")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# Calculate Total Months
    months = csvreader
    def month_year(month):
        month_count = 0
        for i in month:
            month_count +=1

        return month_count
    var=month_year(months)
    print("Total Months:" + str(var))

#Calculate net total amount of "Profit/Losses" over the entire period
    total = csvreader
    def profit_loss(total):
        profit_losses = 0
        for i in total:
            profit_losses +=1

        return total
    var1=profit_loss(total)
    print("Total:" + str(var1))

#Write to .txt file
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
