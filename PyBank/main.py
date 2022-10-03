import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")
output_path = os.path.join("Analysis", "PyBank_results.txt")

print ("Financial Analysis")
print ("------------------")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    first_row = next(csvreader)

    for row in csvreader:
        total_months = row[0]
        profit_loss = row[1]
        # total_net = profit_loss
        # net_change = total_net / total_months
        # # net_change_list = net_change

        # total_months += 1
        # total_net += int(first_row[1])
        # prev_net = int(first_row[1])

        # total_months += 1
        # total_net += int(row[1])

        # net_change = int(row[1]) - prev_net
        # prev_net = int(row[1])
        # net_change_list += [net_change]
        
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

        return profit_losses
    var1=profit_loss(total)
    print("Total:" + str(var1))

#Average Change
print("Average Change: 0")
#Greatest Increase in Profits
print("Greatest Increase in Profits: 0")
#Greatest Decrease in Profits
print("Greatest Decrease in Profits: 0")

#Write to .txt file
with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------\n")
    txtfile.write("Total Months: \n")
    txtfile.write("Average Change: 0 \n")
    txtfile.write("Greatest Increase in Profits: 0 \n")
    txtfile.write("Greatest Decrease in Profits: 0 \n")
    txtfile.close()

# total_profit = 
# average_change = 
# profit_increase = 
# profit_decrease = 

# print ("Total Months: " + int(total_months))
# print("Total: $" + str(total_profit))
# print (f"Total: ${average_change}")
