# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:18:42 2019

@author: andrewd
"""

import os
import csv

date = []
pnl = []
totalMonths = 0
pnlTotal = 0
pnlAvgChange = 0
pnlTotalChange = 0
greatestIncrease = 0
greatestDecrease = 0


csvpath = os.path.join("..","..","..","UCBBEL201902DATA2","03-Python","Homework","Instructions","PyBank","Resources","budget_data.csv")
outputpath = os.path.join(".","output.txt")

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    
    for row in csvreader:
        date.append(row[0])
        pnl.append(int(row[1]))
        
totalMonths = len(date)

for i in pnl:
#calculate Total PnL    
    pnlTotal +=i
    
#calculate Average PnL Change    
    if pnl.index(i) < (len(pnl) - 1):
        pnlTotalChange += pnl[pnl.index(i) + 1] - pnl[pnl.index(i)]

pnlAvgChange = pnlTotalChange / (totalMonths - 1) 

greatestIncrease = pnl.index(max(pnl))
greatestDecrease = pnl.index(min(pnl))

#print results to text file
with open(outputpath, 'w') as textfile:
    textfile.write("""Financial Analysis
--------------------------------
Total Months: {}
Total: ${:,.0f}
Average Change: ${:,.2f}
Greatest Increase in Profits: {} (${:,.0f})
Greatest Decrease in Profits: {} (${:,.0f})
""".format(totalMonths,pnlTotal,pnlAvgChange,date[greatestIncrease],pnl[greatestIncrease], date[greatestDecrease], pnl[greatestDecrease]))

#print results to console           
print("""Financial Analysis
--------------------------------      
Total Months: {}
Total: ${:,.0f}
Average Change: ${:,.2f}
Greatest Increase in Profits: {} (${:,.0f})
Greatest Decrease in Profits: {} (${:,.0f})
""".format(totalMonths,pnlTotal,pnlAvgChange,date[greatestIncrease],pnl[greatestIncrease], date[greatestDecrease], pnl[greatestDecrease])
)



    

