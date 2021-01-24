import os
import csv

# specify output file path
output_txt = os.path.join("Analysis", "summary.txt")

# Specify file to read from
election_data = os.path.join('Resources', 'election_data.csv')

# define variables and give initial values
votes = 0
most_votes = 0
candidates = []
votes_dict = {}
all_votes = []

# open and read the CSV
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file)
    # read the header row
    csv_header = next(csv_reader)
    
    # loop through csv file
    for row in csv_reader:
        
        # get total vote count
        votes += 1

        # get candidates
        if row[2] not in candidates:
            candidates.append(row[2])

        # all votes in all_votes[] lists
        all_votes.append(row[2])
    
    # print total votes
    print(f'There were {votes} votes during this election!')

    # dictionary for each candidate and vote count
    for candidate in candidates:
        votes_received = all_votes.count(candidate)
        votes_dict[candidate] = votes_received
        
        # find the winner
        if votes_received > most_votes:
            most_votes = votes_received
            winner = candidate

        # print results
        print(f'{candidate} received {votes_received} votes ({round((votes_received / votes) * 100, 0)}%)')
        
    # print winner
    print(f'{winner} is the winner!')

# send to text file
with open(output_txt, 'w') as txtfile:

    #print vote count
    txtfile.write(f'There were {votes} votes during this election!')
    txtfile.write('\n')

    # loop through created dictionary
    for candidate, v in votes_dict.items():
        
        txtfile.write(f'{candidate} recieved {votes_received} ({round((votes_received / votes) * 100,0)}%) votes')
        txtfile.write('\n')

    # Print winner
    txtfile.write(f'{winner} is the winner!')    
