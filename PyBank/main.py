#Create script in Python that does an analysis of PyBank finances to calculate:

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

#1st step import dependencies
import os
import csv

#Then create variables just like VBA (sort of)


profit_loss_delta=[]
monthly_change=[]
date=[]

number_months=0
net_profit_losses=0
PL_change=0
starting_profit_losses = 0



#Path to Resources folder and csv budget file
budget_csv_path=os.path.join("Resources","budget_data.csv")

#Open and read csv file
with open(budget_csv_path, newline="") as csvfile:
    
    csv_reader=csv.reader(csvfile, delimiter=",")

    #Make it read the header row
    csv_header=next(csvfile)

    #Make it read each row of data
    for row in csv_reader:

        number_months = number_months + 1

        #Need to Append each month to the months
        date.append(row[0])

        #Append profit info & calculate
        profit_loss_delta.append(row[1])
        net_profit_losses= net_profit_losses +int(row[1])

        #calculate avg change in profits from month to month
        total_profit_losses=int(row[1])
        monthly_change_profits=total_profit_losses - starting_profit_losses


        #Put into list
        monthly_change.append(monthly_change_profits)


        PL_change = PL_change + monthly_change_profits
        starting_profit_losses = total_profit_losses

        #calculate average in profits
        average_change= (PL_change/number_months)


        greatest_increase= max(monthly_change)
        greatest_decrease = min(monthly_change)


        increase_start= date[monthly_change.index(greatest_increase)]
        decrease_start= date[monthly_change.index(greatest_decrease)]


#Print analysis
print(f"Financial Analysis")
print(f"-----------------------------")
print(f"Total Months: {number_months}")
print(f"Total: ${net_profit_losses}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {increase_start} (${greatest_increase})")
print(F"Greatest Decrease in Losses: {decrease_start} (${greatest_decrease})")

#export with results
budget_file=os.path.join("budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write(f"Financial Analysis\n")
    outfile.write(f"----------------------------")
    outfile.write(f"Total Months: {number_months}\n")
    outfile.write(f"Total: ${net_profit_losses}\n")
    outfile.write(f"Average Change: {average_change}\n")
    outfile.write(f"Greatest Increase in Profits: {increase_start} (${greatest_increase})\n")
    outfile.write(F"Greatest Decrease in Losses: {decrease_start} (${greatest_decrease})\n")
