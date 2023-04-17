#Part 1 - read file ---------------------------------------
#main.py for PyBank by Andrea Monnerie

#import the libraries
import os
import csv

#declare and initialize any variables
dataList = []

#open and read the file
csvpath = os.path.join( 'Resources', 'budget_data.csv')

#receive the data from file to list
with open(csvpath) as csvopen:
    dataFile = csv.reader(csvopen, delimiter=',')
   
    #header is excluded but stored
    header = next(dataFile) 

    #from data from file to a 2d list
    for row in dataFile:
        dataList.append(row)

#don't need the file anymore
csvopen.close() 

#Part 2 - analysis/math ---------------------------------------

#get total of months
totalMonths = len(dataList) #number of rows = numbers of months

#get total Amount
#declare and initalize needed variables
totalAmount = 0

for i in range(totalMonths):
    totalAmount = totalAmount + int(dataList[i][1])

#get the average change
#declare and initalize needed variables
profitChange = list()
sum = 0

for row in range(1,totalMonths):
    
    #calculate the change
    change = int(dataList[row][1]) - int(dataList[row-1][1])
    
    #store the change in a list
    profitChange.append(change)

    #compute the sum
    #index of the list off since the change starts on the 2nd month
    sum = sum + profitChange[row-1]

#compute the average
average = round(sum/(totalMonths-1),2)

#find the greatest increase
#declare and initalize needed variables
greatestIn = int(profitChange[0])
inMonth = ""

for i in range(totalMonths-2):
     if int(profitChange[i]) > greatestIn:
         
        #get the amount
        greatestIn = profitChange[i] 

        #get the month
        inMonth = dataList[i+1][0]

#find the greatest decrease
#declare and initalize needed variables
greatestDe = int(profitChange[0])
deMonth = ""

for i in range(totalMonths-2):
     if int(profitChange[i]) < greatestDe:
        
        #get the amount
         greatestDe = profitChange[i] 
         
         #get the month
         deMonth = dataList[i+1][0] 

#Part 3 - print to console -------------------------------------
result = "Financial Analysis" + "\n" + "\n----------------------------"
result = result + f"\n\nTotal Months: {totalMonths}"
result = result + f"\n\nTotal: ${totalAmount}"
result = result + f"\n\nAverage Change: ${average}"
result = result + f"\n\nGreatest Increase in Profits: {inMonth} (${greatestIn})"
result = result + f"\n\nGreatest Decrease in Profits: {deMonth} (${greatestDe})"
print(result)


#Part 4 - write output file ------------------------------------

#set up the output file
textpath = os.path.join("analysis", "FinancialAnalysis.txt")

with open(textpath, 'w') as outputFile:

    # write the result in File
    outputFile.write(result)

#done with the file
outputFile.close()