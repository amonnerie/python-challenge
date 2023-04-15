#Part 1 - read file ---------------------------------------
#main.py for PyBank by Andrea Monnerie

#import the libraries
import os
import csv

#initialize any variables
dataList = []

#open and read the file
csvpath = os.path.join( 'Resources', 'budget_data.csv')

#receive the data from file to list
with open(csvpath) as csvopen:
    dataFile = csv.reader(csvopen, delimiter=',')
    header = next(dataFile) #header is excluded

    for row in dataFile:
        dataList.append(row)
csvopen.close() #don't need the file anymore
#Part 2 - analysis/math ---------------------------------------

#total of months
totalMonths = len(dataList) #number of rows = numbers of months
#print(totalMonths)

#total Amount
totalAmount = 0
for i in range(totalMonths):
    totalAmount = totalAmount + int(dataList[i][1])
#print(totalAmount)

#get the average
#averageC = round(totalAmount/totalMonths,2)
profitChange = list()
sum = 0
for row in range(1,totalMonths):
    change = int(dataList[row][1]) - int(dataList[row-1][1])
    profitChange.append(change) #get the change
    sum = sum + profitChange[row-1]
average = round(sum/(totalMonths-1),2)
#print(round(average, 2))

#find the greatest increase
greatestIn = int(profitChange[0])
inMonth = ""
for i in range(totalMonths-2):
     if int(profitChange[i]) > greatestIn:
         greatestIn = profitChange[i] #get the amount
         inMonth = dataList[i+1][0] #get the month
#print(greatestIn)

#find the greatest decrease
greatestDe = int(profitChange[0])
deMonth = ""
for i in range(totalMonths-2):
     if int(profitChange[i]) < greatestDe:
         greatestDe = profitChange[i] #get the amount
         deMonth = dataList[i+1][0] #get the month
#print(f" {greatestDe} {deMonth}")

#part 3 - print to console -------------------------------------
result = "Financial Analysis" + "\n" + "\n----------------------------"
result = result + f"\n\nTotal Months: {totalMonths}"
result = result + f"\n\nTotal: ${totalAmount}"
result = result + f"\n\nAverage Change: ${average}"
result = result + f"\n\nGreatest Increase in Profits: {inMonth} (${greatestIn})"
result = result + f"\n\nGreatest Decrease in Profits: {deMonth} (${greatestDe})"
print(result)
#part 4 - write output file ------------------------------------

textpath = os.path.join("analysis", "FinancialAnalysis.txt")

with open(textpath, 'w') as outputFile:

    # write the result in File
    outputFile.write(result)
outputFile.close()