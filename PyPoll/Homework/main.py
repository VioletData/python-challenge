# Modules
import os
import csv

#Set up path for file
csvpath=os.path.join("..", "Resources", "election_data.csv" )
#print(csvpath)

total_votes=0
#total_profit=0
#previous_value=0
#current_value=0
#list_changes=[]

print("Election Results")
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
        total_votes=total_votes+1
        current_value=int(row[0])

        #total_profit=total_profit+1
        #current_value=int(row[1])

        #monthly_diff=current_value-previous_value
        #list_changes.append(monthly_diff)
        
    #list_changes.remove("867884")

        #previous_value=current_value
        #avg_monthly_diff=sum[list_changes]

# Calculate the average of the changes in Profit/Lossess over the entire period

# Determine the greateest increase in profits (date and amount) over the entire period
# Determine the greaterst decrease in losses (datea and amount) ove the entire period



print("Total Votes: " + str(total_votes))
print("---------------------")
#print("Total: $"+str(total_profit))
print("---------------------")
#print("Average Change: $" +str(total_profit))
print("---------------------")

#print(row)


