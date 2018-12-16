import os
import csv

csvpath = os.path.join("resources/election_data.csv")

#The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`.

with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file)

#Skip header
    skip_header = next(csv_reader)

#Establish empty variables for votes & candidates, and an empty candidate/vote dictionary
    total_votes = 0
    candidates = []
    candidate_summary = {}

#Iterate through data and aggregate candidate names and votes
    for row in csv_reader:
        total_votes += 1
        if not row[2] in candidates:
            candidates.append(row[2])
            candidate_summary[row[2]] = 1
        else:  
            candidate_summary[row[2]] += 1

#Establish winner, print results, export to a text file
print(f'''Election Results
-----------------
Total Votes: {total_votes} 
-----------------''', file=open("election_results.txt", "a"))
most_votes = 0
winner = ""
for key in candidate_summary:
    percent = round((candidate_summary[key]/total_votes)*100,3)
    candidate_votes = candidate_summary[key]
    print(f"{key}: {percent}% ({candidate_votes})", file=open("election_results.txt", "a"))
    if candidate_summary[key] > most_votes:
        most_votes = candidate_summary[key]
        winner = key
print(f'''-----------------
Winner: {winner}
-----------------''', file=open("election_results.txt", "a"))
