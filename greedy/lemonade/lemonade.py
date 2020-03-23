"""
ID: neelkolhe
TASK: lemonade
"""


inpFile=open('lemonade.in','r')
outFile=open('lemonade.out','w')

numberCows=int(inpFile.readline())

allCows=inpFile.readline().split()

for i in range(numberCows):
  allCows[i]=int(allCows[i])

print(allCows)

sortedLine=sorted(allCows, reverse = True)
print(sortedLine)

final=numberCows+1

for i in range(numberCows):
  if sortedLine[i]<i:
    final=i
    break


print(final)
