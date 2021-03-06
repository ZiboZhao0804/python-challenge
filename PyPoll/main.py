#read the csv data file and store voter id and Candidate in two lists - id and candidate
import os,csv
csvpath = os.path.join('Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    id = []
    candidate = []
    for row in csvreader:
        id.append(row[0])
        candidate.append(row[2])

#1. The total number of votes cast
totalVotes = len(id)

#2. A complete list of candidates who received votes
candidate_list = list(set(candidate))

#3. The percentage of votes each candidate won & The total number of votes each candidate won
votes = [0]*len(candidate_list)
percentage = [0]*len(candidate_list)
for i in range(len(candidate_list)):
    for j in range(len(candidate)):
        if candidate[j] == candidate_list[i]:
            votes[i] += 1
for i in range(len(percentage)):
    percentage[i] = round(votes[i]/totalVotes*100,3)

#4. The winner of the election based on popular vote.
vote = votes[0]
winner = candidate_list[0]
for i in range(len(votes)-1):
    if votes[i+1] > vote:
        winner = candidate_list[i+1]
        vote = votes[i+1]

#print out the results
str1 = "Election Results"
str2 = "-------------------------------"
str3 = f"Total Votes: {totalVotes}"
str4 = "-------------------------------"
str_candidate = [""]*len(candidate_list)
for i in range(len(str_candidate)):
    str_candidate[i] = f"{candidate_list[i]}: {percentage[i]}% ({votes[i]})"
str5 = "-------------------------------"
str6 = f"Winner: {winner}"
str7 = "-------------------------------"

lines = [str1, str2, str3, str4] + str_candidate + [str5, str6, str7] 
for line in lines:
    print(line)

#write the results into a text file
output_file = os.path.join('analysis','analysis.txt')
with open(output_file, 'w') as text:
    for line in lines:
        text.write(line)
        text.write('\n')