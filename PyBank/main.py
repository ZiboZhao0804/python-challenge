#read the csv data file and store date and profit/losses in two lists - date and amount
import os,csv
csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    date = []
    amount = []
    for row in csvreader:
        date.append(row[0])
        amount.append(int(row[1]))
#uncomment below to check whether the items returned are correct
#print(date)
#print(amount)

#1. The total number of months included in the dataset
totalMonth = 0
for month in date:
    totalMonth += 1
#print(totalMonth)

#2. The net total amount of "Profit/Losses" over the entire period
totalAmount = 0
for i in range(len(amount)):
    totalAmount = totalAmount + amount[i]
#print(totalAmount)

#3. Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
change = []
for i in range(len(amount)-1):
    change.append(amount[i+1]-amount[i])
totalChange = 0
for i in range(len(change)):
    totalChange = totalChange + change[i]
averageChange = totalChange / ((totalMonth) - 1)
averageChange = round(averageChange,2)
#print(averageChange)


#4. The greatest increase in profits (date and amount) over the entire period
profit_Inc = change[0]
for i in range(len(change)-1):
    if change[i+1] > profit_Inc:
        date_Inc = date[i+2]
        profit_Inc = change[i+1]
#print(date_Inc)
#print(profit_Inc)

#5. The greatest decrease in profits (date and amount) over the entire period
profit_Dec = change[0]
for i in range(len(change)-1):
    if change[i+1] < profit_Dec:
        date_Dec = date[i+2]
        profit_Dec = change[i+1]
#print(date_Dec)
#print(profit_Dec)

#print out the results
str1 = "Financial Analysis"
str2 = "-------------------------------"
str3 = f"Total Months: {totalMonth}"
str4 = f"Total: ${totalAmount}"
str5 = f"Average Change: ${averageChange}"
str6 = f"Greatest Increase in Profits: {date_Inc} (${profit_Inc})"
str7 = f"Greatest Decrease in Profits: {date_Dec} (${profit_Dec})"
lines = [str1, str2, str3, str4, str5, str6, str7] 
for line in lines:
    print(line)

#write the results into a text file
output_file = os.path.join('analysis','analysis.txt')
with open(output_file, 'w') as text:
    for line in lines:
        text.write(line)
        text.write('\n')