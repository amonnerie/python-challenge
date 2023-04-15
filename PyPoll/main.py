#Part 1 - read file ---------------------------------------
#main.py for PyPoll by Andrea Monnerie

#import the libraries
import os
import csv

#initialize any variables
voteList = []

#open and read the file
csvpath = os.path.join( 'Resources', 'election_data.csv')

#receive the data from file to list
with open(csvpath) as csvopen:
    voteFile = csv.reader(csvopen, delimiter=',')
    header = next(voteFile) #header is stored but excluded

    for row in voteFile:
        voteList.append(row)
csvopen.close() #don't need the file anymore

#Part 2 - analysis/math ---------------------------------------

#The total number of votes cast
totalVotes = len(voteList)
#print(totalVotes) good
#A complete list of candidates who received votes
StockhamVote = 0
DeGetteVote = 0
DoaneVote = 0
for vote in voteList:
    if vote[2] == "Charles Casper Stockham":
        StockhamVote += 1
    elif vote[2] == "Diana DeGette":
        DeGetteVote += 1
    elif vote[2] == "Raymon Anthony Doane":
        DoaneVote += 1
    else:
        print("Unknown Candidate")
        break
#print(f"{StockhamVote} {DeGetteVote} {DoaneVote}")

#get percentages
StockhamPer = round((StockhamVote/totalVotes)*100, 3)
DeGettePer = round((DeGetteVote/totalVotes)*100,3)
DoanePer = round((DoaneVote/totalVotes)*100, 3)

#The winner of the election based on popular vote
winner = ""
if StockhamVote > DeGetteVote:
    winner = "Charles Casper Stockham"
elif DeGetteVote > DoaneVote:
    winner = "Diana DeGette"
elif DoaneVote > StockhamVote:
    winner = "Raymon Anthony Doane"
else:
    #in case the candidates were all a tie
    winner = "N/A: Tie Election"
print(winner)

#part 3 - print to console -------------------------------------
result = "Election Results" + "\n\n-------------------------"
result = result + f"\n\nTotal Votes: {totalVotes}"
result = result + "\n\n-------------------------"
result = result + f"\n\nCharles Casper Stockham: {StockhamPer}% ({StockhamVote})"
result = result + f"\n\nDiana DeGette: {DeGettePer}% ({DeGetteVote})"
result = result + f"\n\nRaymon Anthony Doane: {DoanePer}% ({DoaneVote})"
result = result + "\n\n-------------------------"
result = result + f"\n\nWinner: {winner}"
result = result + "\n\n-------------------------"
print(result)
#part 4 - write output file ------------------------------------

textpath = os.path.join("analysis", "ElectionResult.txt")

with open(textpath, 'w') as outputFile:

    # write the result in File
    outputFile.write(result)
outputFile.close()