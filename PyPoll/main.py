
import csv
import os

votes = {}
with open('Resources/election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    row_count = sum(1 for row in csv_reader)
    csv_file.seek(0)
    total_votes = 0
    current_candidate_name = ""
    previous_candiate_name = ""
    vote_count = 0 
    #Get the total number of rows
    
    next(csv_reader)
    for n, row in enumerate(csv_reader):
        #get the totla number of votes
        total_votes += 1
        # increment the vote until the next candidate
        vote_count = vote_count + 1
        current_candidate_name = row[2]
        if n > 0:
            # check if the canditate is different than the previous candidate
            if current_candidate_name != previous_candiate_name :
                # if this is the first time the candiate is added
                if previous_candiate_name not in votes:
                    votes[previous_candiate_name] = vote_count
                elif n == ( row_count - 2 ):
                   votes[previous_candiate_name] = votes[previous_candiate_name] + vote_count
                else:
                    # if the candiate is alrady there, then add the vote
                    votes[previous_candiate_name] = votes[previous_candiate_name] + vote_count
                    # reset the vote count for the next candidate
                vote_count = 0
        previous_candiate_name = current_candidate_name
        
        

list_of_canidates = ""
highest_vote = 0
percentage = 0.0000
winner = ""
for key in votes:
    if int(votes[key]) > highest_vote:
        highest_vote = int(votes[key])
        winner = key
    print(key, '->', votes[key])
    percentage = ( float(votes[key] / total_votes)) * 100
    list_of_canidates = list_of_canidates + "%s : %.4f%% (%d)\n" %(key,percentage, votes[key])
    percentage = 0.0000
    

output = (
'''  Election Results
-------------------------
Total Votes: %d
-------------------------
%s
-------------------------
Winner: %s
-------------------------
'''
)
print(output % (total_votes, list_of_canidates, winner) )

file = open("analysis/results.txt", "w")
file.write(output % (total_votes, list_of_canidates, winner ))
file.close()
