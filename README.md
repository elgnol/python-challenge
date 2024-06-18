# **Python-challenge**

## PyPoll
In this challenge, I coded a program to read in the data from elections_data.csv, which has a data set of
candidate names, the voters' ID number, and the county. 
The code calculated:
- The total number of votes cast
- The percentages of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote
And writes it on a new csv file

## PyBank
In this challenge I was given a csv file called budget_data.csv, which included a column of dates and
a column of profits/losses
I had to code a program calculating:
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period
And writes it on a new csv file

## Code Source
In PyPoll folder main.py these code were used to make the code efficient using ChatGPT:
- from collections import Counter
- candidate_votes = Counter()
- candidates = list(candidate_votes.keys())
- votes = list(candidate_votes.values())
- vote_percentages = [(votes[i] / total_votes) * 100 for i in range(len(candidates))]
- vote_percentages_rounded = [round(percentage, 3) for percentage in vote_percentages]

In PyBank folder main.py this code was fixed from Xpert Learning Assistant:
started: for i in range(len(date) 
to: for i in range(len(date)-1)
The loop had a problem with running to an index that didn't exist before


