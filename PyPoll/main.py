
#This challenge is to help a rural town modernize its vot-counting process

#Make a script to analyze votes

# Import dependencies
import os
import csv


#create path to csv
election_data_csv=os.path.join("Resources", "election_data.csv")
export_file=os.path.join("analysis", "election_data.txt")

#Variables

vote_list = []
candidates = []
candidate_percent = []
candidate_count = []
totalvote = 0

with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        vote_list.append(row[2])
        
totalvote = len(vote_list)

# assign candidates their indexes
for name in vote_list:
   if name not in candidates:
        candidates.append(name)
        y = name

count = 0
candidate = vote_list[0]
lastCount = 0

# Print Election Results
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {totalvote}")
print("------------------------------")

for candidate in candidates:
    for vote in vote_list:
        if candidate == vote:
            count += 1
    percent = count / len(vote_list)
    candidate_percent.append(percent)
    candidate_count.append(count)
    
    if lastCount < count:
        Winner = candidate    
    print(f"{candidate}: {percent:.3%} ({count})")
    
    lastCount = count
    count = 0

# print winner
print("--------------------------")
print(f"Winner: {Winner}")
print("--------------------------")

#Lastly, export results into txt file
with open(export_file, 'w') as outfile:
    outfile.write("Election Results\n")
    outfile.write("------------------\n")
    outfile.write(f"Total Votes: {totalvote}\n")
    outfile.write("--------------------\n")

    for candidate in candidates:
        index = candidates.index(candidate)
        outfile.write(f"{candidate}: {candidate_percent[index]:.3%} ({candidate_count[index]})\n")
    outfile.write("--------------------------\n")
    outfile.write(f"Winner: {Winner}\n")