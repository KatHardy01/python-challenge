# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# path to grab the csv data
csvpath = os.path.join(r"C:\Users\kaitl\Documents\Vandy_BootCamp\03-Python\Module 3 challenge\python-challenge\PyBank\Resources\budget_data.csv")

#starting with loop
with open(csvpath, encoding= 'utf') as csvfile:
    #read the csv file
    #set delimiter
    csvreader = csv.reader(csvfile, delimiter = ',')
   #Skip the first row (header)
    next(csvreader)
   #Exclude first month from loop
    budget_data = [next(csvreader)]
    #Initialize net amount with first profit/loss 
    net_amount = int(budget_data[0][1])
    changes = []
    #Calculate change inside for loop
    previous_profit_loss = net_amount

    for line in csvreader:
        # Total months included in dataset
        budget_data.append(line)
       
        # Net total amount of Profit/Losses over entire period
        net_amount = net_amount + int(line[1])
       
       # Changes in profit/loss over entire period
        changes.append(int(line[1])-previous_profit_loss)

        # Average changes of profit/loss
        previous_profit_loss = int(line[1])


# Greatest increase in profit (date and amount)
max_change = changes.index(max(changes))
# print(budget_data[max_change+1])

#Greatest decrease in profit (date and amount)
max_loss = changes.index(min(changes))
# print(budget_data[max_loss+1])

# Print results to terminal
output = f'''  Financial Analysis
  ----------------------------
  Total Months: {len(budget_data)}
  Total: ${net_amount}
  Average Change: ${round(sum(changes)/(len(changes)),2)}
  Greatest Increase in Profits: {budget_data[max_change+1][0]} (${max(changes)})
  Greatest Decrease in Profits: {budget_data[max_loss+1][0]} (${min(changes)})
  
  '''
print(output)

#output path to txt file
csvpath = os.path.join(r"C:\Users\kaitl\Documents\Vandy_BootCamp\03-Python\Module 3 challenge\python-challenge\PyBank\Analysis\budget_analysis.txt")  

with open(csvpath,'w') as textfile:
    textfile.write(output)
