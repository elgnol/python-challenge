import os
import csv

election_data_csv = os.path.join('Resources', 'election_data.csv')

candidate = []
voters = []
organized_candidate = []

with open(election_data_csv, 'r') as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    header = next(csv_reader)
    
    for row in csv_reader:
        
        voters.append(row[0])
        candidate.append(row[2])
    
    # Get number of total voters
    total_voters = len(voters)
    
    # sorts the list of candidates so that there won't be
    # changes in candidate names while looking though the voters
    candidate.sort()
    index = 0
    
    # Organized the list of candidate so that we dont have repetition
    # of the same candidate in the list
    while index < len(candidate):
        
        if index == len(candidate) - 1:
            organized_candidate.append(candidate[index])
        elif candidate[index + 1] != candidate[index]:
            organized_candidate.append(candidate[index])
        index += 1
        
    # identify number of candidates before making the next loop
    # to calculate total voters per candidate
    num_of_candidates = len(organized_candidate)
    
    # initialize variables to keep count of each candidate votes
    C_votes = 0 
    D_votes = 0
    R_votes = 0      

    # loop to add up count of votes per candidate
    # can be change if there are more candidates in the data
    for i in range(total_voters):
        
        if organized_candidate[0] == candidate[i]:
            C_votes += 1 
        elif organized_candidate[1] == candidate[i]:
            D_votes += 1
        else:
            R_votes += 1
    
    # Get percentages of votes per candidate out of total votes
    C_votes_percent = round((C_votes/total_voters) * 100, 3)
    D_votes_percent = round((D_votes/total_voters) * 100, 3)
    R_votes_percent = round((R_votes/total_voters) * 100, 3)

    # if statement to find the winner of the votes
    if C_votes > D_votes and C_votes > R_votes:
        winner = organized_candidate[0]
    elif D_votes > C_votes and D_votes > R_votes:
        winner = organized_candidate[1]
    else:
        winner = organized_candidate[2]
    
print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_voters}")
print("---------------------------")
print(f"Charles Casper Stockham: {C_votes_percent}% ({C_votes})")
print(f"Diana DeGette: {D_votes_percent}% ({D_votes})")
print(f"Raymon Anthony Doane: {R_votes_percent}% ({R_votes})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

output_file = os.path.join('analysis', 'results.csv')

with open(output_file, 'w') as csvfile:
    
    csv_writer = csv.writer(csvfile, delimiter=',')
    
    csv_writer.writerow(["Election Results"])
    csv_writer.writerow(["---------------------------"])
    csv_writer.writerow([f"Total Votes: {total_voters}"])
    csv_writer.writerow(["---------------------------"])
    csv_writer.writerow([f"Charles Casper Stockham: {C_votes_percent}% ({C_votes})"])
    csv_writer.writerow([f"Diana DeGette: {D_votes_percent}% ({D_votes})"])
    csv_writer.writerow([f"Raymon Anthony Doane: {R_votes_percent}% ({R_votes})"])
    csv_writer.writerow(["---------------------------"])
    csv_writer.writerow([f"Winner: {winner}"])
    csv_writer.writerow(["---------------------------"])