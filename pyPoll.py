import os
import csv

electionFile1 = os.path.join("election_data_1.csv")

totalVotes = 0
candidatesList = []
uniqueCandidates = []
winner = ""
winnerCount = 0

with open(electionFile1, newline="") as csvfile:
    csvReader = csv.reader(csvfile, delimiter = ",")

    #move to the next row in csvReader so that it doesn't include header
    header = next(csvReader)

    for row in csvReader:
        totalVotes = totalVotes + 1
        candidatesList.append(row[2]) #row[2] gives the names of the candidates.


    #Convert the list of candidates to a 'set' to find the names of candidates occuring only once and convert this 'set' back to a list.
    uniqueCandidates = list(set(candidatesList))
    for x in uniqueCandidates:
        #candidatesList.count(x) gives the number of times each candidate appears in the original list
        #This count gives the number of votes each candidate received.
        print(x + " : " + str(round(((candidatesList.count(x) / totalVotes) * 100), 2)) + "%   " + str(
            candidatesList.count(x)) + " votes ")
        if candidatesList.count(x) > winnerCount:
            winnerCount = candidatesList.count(x)
            winner = x

    print("--------------------------------")
    print("winner: " + str(winner))
    print("--------------------------------")
    print("Total votes: " + str(totalVotes))