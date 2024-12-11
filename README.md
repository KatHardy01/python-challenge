# PYTHON-CHALLENGE

# Module 3 Challenge

# Before You Start:

* New repository created for this project called `python-challenge`

* Cloned repository to my computer.

* Inside the local git repository I have created a directory for each Python challenge. With folder names corresponding to the challenges: **PyBank** and  **PyPoll**.

* Inside of each folder are the following:

  * A new file called `main.py`. The main script to run for each analysis.
  * A `Resources` folder that contains the CSV files used. Including correct csv_path
  * An `analysis` folder that contains a text file with the results from the analysis.

* Pushed to GitHub.

## PyBank Challenge

* Created a Python script to analyze the financial records of a company. Using a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: "Date" and "Profit/Losses".

Created a Python script that analyzes the records to calculate each of the following:

* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* The changes in "Profit/Losses" over the entire period, and then the average of those changes

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in profits (date and amount) over the entire period

The Financial Analysis looks like this:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $22564198
  Average Change: $-8311.11
  Greatest Increase in Profits: Aug-16 ($1862002)
  Greatest Decrease in Profits: Feb-14 ($-1825558)
  ```

* The final script prints the analysis to the terminal and exports a text file with the results.

## PyPoll Instructions

In this challenge the task is helping a small, rural town modernize its vote counting process.

Using a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". The task is to create a Python script that analyzes the votes and calculates each of the following:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote.

The  Polling Analysis looks like this:


  ```text
  Election Results
  -------------------------
  Total Votes: 369711
  -------------------------
  Charles Casper Stockham: 23.049% (85213)
  Diana DeGette: 73.812% (272892)
  Raymon Anthony Doane: 3.139% (11606)
  -------------------------
  Winner: Diana DeGette
  -------------------------
  ```

* It also prints the analysis to the terminal and exports a text file with the results.
