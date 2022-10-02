import os
import csv

csvpath = os.path.join("Resources","election_data.csv")
output_path = os.path.join("Analysis", "PyPoll_results.txt")

print ("Election Results")
print ("------------------")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    first_row = next(csvreader)
    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]

#The total number of votes cast

    votes = csvreader
    def voter_id(votes):
        vote_count = 0
        for i in votes:
            vote_count +=1

        return voter_id
    var=voter_id(votes)
    print("Total Votes:" + str(var))

#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

#Write to .txt file
with open(output_path, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("------------------\n")
    # txtfile.write("Total Votes:" + str(var) + "\n")
    txtfile.close()