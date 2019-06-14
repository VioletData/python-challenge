# Modules
import os
import csv

#Set up path for file
csvpath=os.path.join("..", "Resources", "budget_data.csv" )
#print(csvpath)

total_months=0
total_profit=0
previous_value=0
current_value=0
list_changes=[]
list_dates=[]

print("Financial Analysis")
print("---------------------")

#Open the csv file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#print(csvreader)

#Read the header row
    csv_header=next(csvreader)
#print(f"CSV Header: {csv_header}")

#Read each row of data after the header
    for row in csvreader:

        #Determine total number of months
        total_months=total_months+1
        #current_value=(row[0])

        #Determine total profit over entire period
        total_profit=total_profit+int(row[1])
        current_value=int(row[1])

        # Calculate the average of the changes in Profit/Lossess over the entire period, first calculate change
        monthly_diff=current_value-previous_value
        
        #Store changes in list
        list_changes.append(monthly_diff)
        
        #Store dates in list
        list_dates.append(row[0])
       
        previous_value=current_value
        #avg_monthly_diff=sum[list_changes]

del list_changes[0]
del list_dates[0]
#print(list_changes)
#print(list_dates)

# Calculate the average of the changes in Profit/Lossess over the entire period
average = sum(list_changes) / len(list_changes)

# Determine the greatest increase in profits (date and amount) over the entire period
maximum=list_changes.index(max(list_changes))

# Determine the greatest decrease in losses (datea and amount) ove the entire period
minimum=list_changes.index(min(list_changes))

print("Total Months: " + str(total_months))
print("Total: $"+str(total_profit))
print("Average Change: $" +str(round(average, 2)))
print("Greatest Increase in Profits: " + str(list_dates[maximum]) +" "+str(list_changes[maximum]))
print("Greatest Decrease in Profits: " + str(list_dates[minimum]) +" "+ str(list_changes[minimum]))
#print(list_changes)

#print(row)