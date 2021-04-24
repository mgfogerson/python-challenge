import os
import csv
from pathlib import Path
#Learned about Counter online, seems like a perfect tool for assigning pairs of votes/candidates
from collections import Counter
# Objective 2: Set the path for the CSV file in PyBankcsv
PyPollcsv = os.path.join("Resources","election_data.csv")
#Initialize variables to 0
total_votes = 0
winnerpercent = 0
secondpercent = 0
thirdpercent = 0
fourthpercent = 0
#store values in lists
unique_candidate = []
voter_id = []
county = []
candidate = []
#open csv, loop through rows while skipping the header
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
#append values to colummns
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
#count total votes
        total_votes = total_votes + 1
#obtain complete list of unique candidates
        if row[2] not in unique_candidate:
                unique_candidate.append(row[2])
#save candidate vote totals in counter based on candidate list
final_candidate = dict(Counter(candidate))
firstplace = int(final_candidate[unique_candidate[0]])
secondplace = int(final_candidate[unique_candidate[1]])
thirdplace = int(final_candidate[unique_candidate[2]])
fourthplace = int(final_candidate[unique_candidate[3]])
winnerpercent = (firstplace / total_votes) * 100
secondpercent = (secondplace / total_votes) * 100
thirdpercent =  (thirdplace / total_votes) * 100
fourthpercent = (fourthplace / total_votes) * 100
#print statements
print(f"Election Results:")
print(f"--------------------")
print(f"Total Votes")
print(total_votes)
print(f"--------------------")
print(f"Candidates/Percent Won/Votes:")
print(f"{unique_candidate[0]} /  {round(winnerpercent, 3)}% / {firstplace}")
print(f"{unique_candidate[1]} /  {round(secondpercent, 3)}% / {secondplace}") 
print(f"{unique_candidate[2]} /  {round(thirdpercent, 3)}% / {thirdplace}")
print(f"{unique_candidate[3]} /  {round(fourthpercent, 3)}%  {fourthplace}")
print(f"--------------------")
print(f"Winner:")
print(f"{unique_candidate[0]}")
print(f"--------------------")
#print to csv
output_path = Path('Analysis')
with open(output_path, 'w') as file:
        file.write(f"Election Results:\n")
        file.write(f"--------------------\n")
        file.write(f"Total Votes\n")
        file.write(f"{total_votes}\n")
        file.write(f"--------------------\n")
        file.write(f"Candidates/Percent Won/Votes:")
        file.write(f"{unique_candidate[0]} /  {round(winnerpercent, 3)}% / {firstplace}\n")
        file.write(f"{unique_candidate[1]} /  {round(secondpercent, 3)}% / {secondplace}\n") 
        file.write(f"{unique_candidate[2]} /  {round(thirdpercent, 3)}% / {thirdplace}\n")
        file.write(f"{unique_candidate[3]} /  {round(fourthpercent, 3)}%  {fourthplace}\n")
        file.write(f"--------------------\n")
        file.write(f"Winner:\n")
        file.write(f"{unique_candidate[0]}\n")
        file.write(f"--------------------\n")
