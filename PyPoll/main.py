
import csv
import os

votes = {}
with open('Resources/election_data.csv', mode='rU') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    total_votes = 0
    current_candidate_name = ""
    previous_candiate_name = ""
    vote_count = 0 
    next(csv_reader)
    for n, row in enumerate(csv_reader):
        total_votes += 1
        current_candidate_name = row[2]
        if n > 0:
            # check if the canditate is different than the previous candidate
            if current_candidate_name != previous_candiate_name :
                # if this is the first time the candiate is added
                if previous_candiate_name not in votes:
                    votes[previous_candiate_name] = vote_count
                elif n == csv_reader.line_num:
                   vote_count = vote_count + 1 
                   votes[previous_candiate_name] = vote_count
                else:
                    # if the candiate is alrady there, then add the vote
                    votes[previous_candiate_name] = votes[previous_candiate_name] + vote_count
                    # reset the vote count for the next candidate
                vote_count = 0
        previous_candiate_name = current_candidate_name
        # increment the vote until the next candidate
        vote_count = vote_count + 1


        

    






output = (
'''  Election Results
-------------------------
Total Votes: %d
-------------------------
Khan: 63.000%% (2218231)
Correy: 20.000%% (704200)
Li: 14.000%% (492940)
O'Tooley: 3.000%% (105630)
-------------------------
Winner: Khan
-------------------------
'''
)

print(output % (total_votes) )

file = open("analysis/results.txt", "w")
file.write(output % (total_votes ))
file.close()
