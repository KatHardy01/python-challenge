# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import os
import csv

# CSV Path
csvpath = (r"C:\Users\kaitl\Documents\Vandy_BootCamp\03-Python\Module 3 challenge\python-challenge\PyPoll\Resources\election_data.csv")

# Open the CSV
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    
    total_votes = 0  # Start counter
    candidates_votes = {}  # Store candidates and their votes
    winner_count = 0  # Initialize winner's vote count
    winner = ""  # Initialize winner's name
    percent_candidates_votes = {}  # Store percentages for each candidate
    
    # Loop through rows in the CSV
    for row in csv_reader:
        # Count total votes
        total_votes += 1
        
        candidate = row[2]  # Candidate's name is in the 3rd column (index 2)
        
        # Add to candidate's vote count
        if candidate in candidates_votes:
            candidates_votes[candidate] += 1
        else:
            candidates_votes[candidate] = 1
    
    # Calculate percentages and find the winner
    for candidate, votes in candidates_votes.items():
        percent_candidates_votes[candidate] = round((votes / total_votes) * 100, 3)
        
        # Determine the winner based on vote count (not percentage)
        if votes > winner_count:
            winner_count = votes
            winner = candidate

# Create candidates_section with formatted results
candidates_section = ""
for candidate, votes in candidates_votes.items():
    candidates_section += f"{candidate}: {percent_candidates_votes[candidate]}%   ({votes})\n"

# Prepare the final output string
output = f'''
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{candidates_section.strip()}
-------------------------
Winner: {winner}
-------------------------
'''

# Print the output
print(output)

# Output path to save the result in a text file
output_path = os.path.join(r"C:\Users\kaitl\Documents\Vandy_BootCamp\03-Python\Module 3 challenge\python-challenge\PyPoll\Analysis\election_analysis.txt")
with open(output_path, 'w') as textfile:
    textfile.write(output)
