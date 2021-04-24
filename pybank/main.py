import os
import csv
from pathlib import Path
# Objective 2: Set the path for the CSV file in PyBankcsv
PyBankcsv = os.path.join("Resources","budget_data.csv")
#Initialize total and maximum variables
max_increase = 0
max_decrease = 0
total_profit = 0
#add empty lists for variables needing looping
date = []
profit = []
monthly_change = []
#open csv, skip header
with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
#loop through rows
    for row in csvreader:
#append date and profit to be retrieved later
        date.append(row[0])
        profit.append(row[1])
#count months
        month_count = len(date)
#total profit is the sum of every profit row, final profit used to calculate average
        total_profit = total_profit + int(row[1])
#use a for loop to create list of changes, then min/max to get the largest profit/loss
    for i in range(1,len(profit)):
        monthly_change.append(int(profit[i]) - (int(profit[i-1])))
        max_increase = max(monthly_change)
        max_decrease = min(monthly_change)
#calculate average change
        average_change = sum(monthly_change)/len(monthly_change)
#Set the dates of the increase and decrease for retrieval, needs to be +1 because of the i loop
max_increase_date = date[monthly_change.index(max_increase)+1]
max_decrease_date = date[monthly_change.index(max_decrease)+1]

print ("Financial Analysis")
print ("----------------------------")
print(f"Total Months: {str(month_count)}.")
print(f"Total Profits: ${str(total_profit)}.")
print(f"Greatest Profit Increase: ${int(max_increase)}, on {str(max_increase_date)}.")
print(f"Greatest Profit Decrease:  ${str(max_decrease)}, on {max_decrease_date}.")
print(f"Average Change in Profits: ${(round(average_change, 2))}")
#export to file
output_path = Path('Financial Analysis')
with open(output_path, 'w') as file:
        file.write("Financial Analysis\n")
        file.write("----------------------------\n")
        file.write(f"Total Months: {str(month_count)}.\n")
        file.write(f"Total Profits: ${str(total_profit)}.\n")
        file.write(f"Greatest Profit Increase: ${int(max_increase)}, on {str(max_increase_date)}.\n")
        file.write(f"Greatest Profit Decrease:  ${str(max_decrease)}, on {max_decrease_date}.\n")
        file.write(f"Average Change in Profits: ${(round(average_change, 2))}\n")

