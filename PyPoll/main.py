import os
import csv
from collections import Counter

election_data_csv = os.path.join('Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidate_votes = Counter()

# Read data and count votes
with open(election_data_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)  # Skip header
    
    for row in csv_reader:
        total_votes += 1
        candidate_votes[row[2]] += 1

# Extract candidate names and vote counts
candidates = list(candidate_votes.keys())
votes = list(candidate_votes.values())

# Calculate percentages
vote_percentages = [(votes[i] / total_votes) * 100 for i in range(len(candidates))]
vote_percentages_rounded = [round(percentage, 3) for percentage in vote_percentages]

# Determine the winner
winner_index = votes.index(max(votes))
winner = candidates[winner_index]

# Print and write results
output_file = os.path.join('analysis', 'results.csv')

with open(output_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    csv_writer.writerow(["Election Results"])
    csv_writer.writerow(["---------------------------"])
    csv_writer.writerow([f"Total Votes: {total_votes}"])
    csv_writer.writerow(["---------------------------"])
    
    for i in range(len(candidates)):
        csv_writer.writerow([f"{candidates[i]}: {vote_percentages_rounded[i]}% ({votes[i]})"])
    
    csv_writer.writerow(["---------------------------"])
    csv_writer.writerow([f"Winner: {winner}"])
    csv_writer.writerow(["---------------------------"])

# Print to terminal
print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")

for i in range(len(candidates)):
    print(f"{candidates[i]}: {vote_percentages_rounded[i]}% ({votes[i]})")

print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")
