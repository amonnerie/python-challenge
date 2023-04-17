#Part 1 - read file ---------------------------------------
#main.py for PyPoll by Andrea Monnerie

#import the libraries
import os
import csv

#declare and initialize any variables
voteList = []

#open and read the file
csvpath = os.path.join( 'Resources', 'election_data.csv')

#receive the data from file to list
with open(csvpath) as csvopen:
    voteFile = csv.reader(csvopen, delimiter=',')
    
    #header is stored but excluded
    header = next(voteFile) 

    #from data from file to a 2d list
    for row in voteFile:
        voteList.append(row)

#don't need the file anymore
csvopen.close() 

#Part 2 - analysis/math ---------------------------------------

#The total number of votes cast
totalVotes = len(voteList)


#A complete list of candidates who received votes
#declare and initialize needed variables
StockhamVote = 0
DeGetteVote = 0
DoaneVote = 0

#count according to the voted candidate
for vote in voteList:
    if vote[2] == "Charles Casper Stockham":
        StockhamVote += 1
    elif vote[2] == "Diana DeGette":
        DeGetteVote += 1
    elif vote[2] == "Raymon Anthony Doane":
        DoaneVote += 1
    else:
        #in case the voter put someone other than the candidates above
        print(f"Voter ID {voteList[vote][0]}: Unknown Candidate")
        break

#get percentages
StockhamPer = round((StockhamVote/totalVotes)*100, 3)
DeGettePer = round((DeGetteVote/totalVotes)*100,3)
DoanePer = round((DoaneVote/totalVotes)*100, 3)

#The winner of the election based on popular vote
#declare and initialized the needed variable
winner = ""

#conditionals to determine the winner 
if StockhamVote > DeGetteVote:
    winner = "Charles Casper Stockham"
elif DeGetteVote > DoaneVote:
    winner = "Diana DeGette"
elif DoaneVote > StockhamVote:
    winner = "Raymon Anthony Doane"
else:
    #in case the candidates were all a tie
    winner = "N/A: Tie Election"

#Part 3 - print to console -------------------------------------
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

#Part 4 - write output file ------------------------------------

#set up the output file
textpath = os.path.join("analysis", "ElectionResult.txt")

with open(textpath, 'w') as outputFile:

    # write the result in File
    outputFile.write(result)

#done with the file
outputFile.close()