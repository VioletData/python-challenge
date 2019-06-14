# Modules
import os
import csv

#Set up path for file
csvpath=os.path.join("..", "Resources", "election_data.csv" )
#print(csvpath)

total_votes=0
list_candidates=[]
summary={}
percentage={}
winner_count=0

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
        #current_value=int(row[0]).

        name=row[2]

        if name not in list_candidates:
            list_candidates.append(name)
            summary[name]=0
    #print(summary)        

        summary[name]=summary[name]+1

    print("Election Results")
    print("---------------------")
    print("Total Votes: " + str(total_votes))
    print("---------------------")
    print(summary) 
    for key,value in summary.items():
        percentage[key]=round(value/total_votes * 100,3)
    #print(percentage)
        if winner_count < value:
            winner_count=value
            winner=key
    print("---------------------")
    print(winner, winner_count)
        #current_value=str(row[2])
    #print(list_candidates)
    print("---------------------")
    
        
      



# #print()







