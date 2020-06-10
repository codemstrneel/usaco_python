"""
The cows have not only created their own government but they have chosen to create their own money system. In their own rebellious way, they are curious about values of coinage. Traditionally, coins come in values like 1, 5, 10, 20 or 25, 50, and 100 units, sometimes with a 2 unit coin thrown in for good measure.

The cows want to know how many different ways it is possible to dispense a certain amount of money using various coin systems. For instance, using a system of {1, 2, 5, 10, …} it is possible to create 18 units several different ways, including: 18x1, 9x2, 8x2+2x1, 3x5+2+1, and many others.

Write a program to compute how many ways to construct a given amount of money using supplied coinage. It is guaranteed that the total will fit into both a signed long long (C/C++) and Int64 (Free Pascal).
"""

"""
ID: neel1
TASK: money
LANG: PYTHON3
"""
import time

start_time = time.time()

inpFile = open('money.in', 'r')
outFile = open('money.out', 'w')
temp=inpFile.readline().split()
typesCoins=int(temp[0])
value=int(temp[1])

allCoins=[]
while len(allCoins)<typesCoins:
  temp=inpFile.readline().split()

  for i in range(len(temp)):
    allCoins.append(int(temp[i]))
allCoins.sort()

print("--- %s seconds ---" % (time.time() - start_time))
numberWays=[0]*(value+1)
numberWays[0]=1

for i in range(typesCoins):  
  for j in range(allCoins[i],value+1):
    numberWays[j]+=numberWays[j-allCoins[i]]

print(numberWays)
outFile.write(str(numberWays[value])+"\n")
outFile.close()
print("--- %s seconds ---" % (time.time() - start_time))
