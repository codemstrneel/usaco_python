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
