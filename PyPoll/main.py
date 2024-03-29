# os, csv module import to read csv file
import os
import csv

# OS file path creation for budget_data.csv
csv_file_path = os.path.join('.', 'Resources', 'election_data.csv')

# Initialise dictionary to populate {candidate : number of votes}
candidates = {}

# Initialise variable
total_votes = 0
winner_votes = 0
winner = ""

# Read the CSV file
with open(csv_file_path, mode='r') as csvfile:
    csvreader = csv.reader(csvfile)   

    # Skip the first row (header)
    csv_header = next(csvreader)

    for row in csvreader:          
        # Assign Candidate column row[2] to candidate_col
        candidate_col = row[2]

        # populate {candidate : number of votes}
        # if candidate does not exist in candidates dictionary, add {candidate : 1} to dictionary
        # if candidate exists in candidates dictionary, add {candidate : +=1} to dictionary
        if candidate_col not in candidates:
           candidates[candidate_col] = 1
        else:
           candidates[candidate_col] += 1    

        total_votes += 1

# Display result to the terminal
print("Election Results")
print("-"*30)
print(f"Total Votes: {total_votes}")
print("-"*30)

for candidate in candidates:
    candi_vote_percent = round((candidates[candidate] / total_votes) * 100,3)
    print(f"{candidate}: {candi_vote_percent}% ({candidates[candidate]})")

    if candidates[candidate] > winner_votes:
       winner_votes = candidates[candidate]
       winner = candidate     

print("-"*30)
print(f"Winner: {winner}")
print("-"*30)


# Export a text file with the results

# OS file path creation for analysis.txt
output_file = os.path.join('.', 'analysis', 'analysis.txt')

#  Open & write the output file
with open(output_file, "w") as outputfile:
    outputfile.write("Election Results\n")    
    outputfile.write("-"*30 + "\n")    
    outputfile.write(f"Total Votes: {total_votes}\n")
    outputfile.write("-"*30 + "\n")        

    for candidate in candidates:
        candi_vote_percent = round((candidates[candidate] / total_votes) * 100,3)
        outputfile.write(f"{candidate}: {candi_vote_percent}% ({candidates[candidate]})\n")

        if candidates[candidate] > winner_votes:
            winner_votes = candidates[candidate]
            winner = candidate     

    outputfile.write("-"*30 + "\n")
    outputfile.write(f"Winner: {winner}\n")
    outputfile.write("-"*30)
