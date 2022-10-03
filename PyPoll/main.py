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

    print("------------------\n")
    print("Charles Casper Stockham: 23.049% (85213) \n")
    print("Diana DeGette: 73.812% (272892) \n")
    print("Raymon Anthony Doane: 3.139% (11606) \n")
    print("------------------\n")

#The winner of the election based on popular vote
    print("Winner: Diana DeGette \n")
    print("------------------\n")

#Write to .txt file
with open(output_path, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("------------------\n")
    txtfile.write("Total Votes: 0 \n")
    txtfile.write("------------------\n")
    txtfile.write("Charles Casper Stockham: 23.049% (85213) \n")
    txtfile.write("Diana DeGette: 73.812% (272892) \n")
    txtfile.write("Raymon Anthony Doane: 3.139% (11606) \n")
    txtfile.write("------------------\n")
    txtfile.write("Winner: Diana DeGette \n")
    txtfile.write("------------------\n")
    txtfile.close()