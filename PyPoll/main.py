# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
inputElectionInfo = os.path.join("Resources", "election_data.csv")  # Input file path
outputElectionSummary = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
totalVotes = 0  # Track the total number of votes cast
candidates = [] # create index of candidates in election
candidateVotes = {} # dictionary for holding votes candidates receive
winner_count = 0
winner_candidate = "" 


# Open the CSV file and process it
with open(inputElectionInfo) as election_data:
    csvreader = csv.reader(election_data)

    # Skip the header row
    header = next(csvreader)

    # Loop through each row of the dataset and process it
    for row in csvreader:
        # Increment the total vote count for each row
        totalVotes = totalVotes + 1


        # Get the candidate's name from the row
        if row[2] not in candidates:
            candidates.append(row[2])
       
        # If the candidate is not already in the candidate list, add them
            # {} "key": value }
            candidateVotes[row[2]] = 1

        else:
            # candidate is in list
            # add vote to candidate count
            candidateVotes[row[2]] += 1


        # Add a vote to the candidate's count
votes_output = ""

# Loop through the candidates to determine vote percentages and identify the winner
for candidate in candidateVotes:
    votes = candidateVotes.get(candidate)
    votesPct = (float(votes) / float(totalVotes)) * 100

# Get the vote count and calculate the percentage
    votes_output += f"\n {candidate}: {votesPct:.3f}%  ({votes})\n"

# Update the winning candidate if this one has more votes    
    if votes > winner_count:
        winner_count = votes
        winner_candidate = candidate

winner_candidate_output = f"Winner: {winner_candidate}\n"

# Print the total vote count (to terminal)
# Generate and print the winning candidate summary

output = (
    f"\n\n Election Results\n"
    f"\n ---------------------------------\n"
    f"\n Total Votes: {totalVotes:} \n"
    f"\n ---------------------------------"
    f"\n{votes_output}  "
    f"\n ---------------------------------\n"
    f"\n {winner_candidate_output}"
    f"\n ---------------------------------\n"
)

print(output)

# Open a text file to save the output
# Write the total vote count to the text file
# Save the winning candidate summary to the text file
with open(outputElectionSummary, "w") as txt_file:
    txt_file.write(output)
