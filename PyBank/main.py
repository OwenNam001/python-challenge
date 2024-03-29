# os, csv module import to read csv file
import os
import csv

# OS file path creation for budget_data.csv
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# Tells Python to Open file 
with open(csvpath, encoding='UTF-8') as csvfile:

    # Variable initialise
    number_of_months = 0
    net_total_amt = 0
    prev_profit_losses = 0
    monthly_change = 0
    addUp_monthly_change = 0
    average_change = 0
    great_increase_val = -9999999999999
    great_increase_month = ""
    great_decrease_val = 9999999999999
    great_decrease_month = ""

    # csv file reader creation to hold file content
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the first row (header)
    csv_header = next(csvreader)
    
    # Access each row and calculate items
    for row in csvreader:
        date_column = row[0]
        profit_losses_column = int(row[1])

        # Add up number to count the number of row
        number_of_months +=1

        # Sum Profit/Losses column to get net total amount of "Profit/Losses"
        net_total_amt += profit_losses_column

        # Get monthly change from second Month by profit/losses - prev_profit_losses
        if number_of_months > 1:
            monthly_change = profit_losses_column - prev_profit_losses
            addUp_monthly_change += monthly_change
                        
        # Get Greatest Increase in Profits
        if monthly_change > great_increase_val:    
           great_increase_val = monthly_change
           great_increase_month = date_column

        # Get Greatest Decrease in Profits
        if monthly_change < great_decrease_val:    
           great_decrease_val = monthly_change
           great_decrease_month = date_column           

        # Assign Profit/Losses to "prev_profit_losses" to use next loop        
        prev_profit_losses = profit_losses_column 

    # Get average monthly change from second Month, devide by total number month -1 
    average_change = round(addUp_monthly_change / (number_of_months -1),2)      

# Display analysis to terminal
print("Financial Analysis")
print("")
print("-"*30)
print("")
print(f"Total Months: {number_of_months}")
print("")
print(f"Total: ${net_total_amt}")
print("")
print(f"Average Change: ${average_change}")
print("")
print(f"Greatest Increase in Profits: {great_increase_month} (${great_increase_val})")
print("")
print(f"Greatest Decrease in Profits: {great_decrease_month} (${great_decrease_val})")

# Export a text file with the results

# OS file path creation for analysis.txt
output_file = os.path.join('.', 'analysis', 'analysis.txt')

#  Open & write the output file
with open(output_file, "w") as outputfile:
    outputfile.write("Financial Analysis\n")
    outputfile.write("\n")
    outputfile.write("-"*30 + "\n")
    outputfile.write("\n")
    outputfile.write(f"Total Months: {number_of_months}\n")
    outputfile.write("\n")
    outputfile.write(f"Total: ${net_total_amt}\n")
    outputfile.write("\n")
    outputfile.write(f"Average Change: ${average_change}\n")
    outputfile.write("\n")
    outputfile.write(f"Greatest Increase in Profits: {great_increase_month} (${great_increase_val})\n")
    outputfile.write("\n")
    outputfile.write(f"Greatest Decrease in Profits: {great_decrease_month} (${great_decrease_val})\n")