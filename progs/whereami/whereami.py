"""
ID: neelkolhe
TASK: whereami
"""


  
inpFile=open('whereami.in','r')
outFile=open('whereami.out','w')

numberHouses=int(inpFile.readline())

houseColors=list(str(inpFile.readline()))
del houseColors[numberHouses]

smallestrepeatingsequence=100
allSequences=[[] for i in range (numberHouses)]

for i in range (numberHouses):
  for j in range(numberHouses-i):
    startingPoint=j
    endPoint=j+i
    currSequence=[]
    for a in range(startingPoint,endPoint+1):
      currSequence.append(houseColors[a])
    allSequences[i].append(currSequence)

badArrays=[]
for i in range (numberHouses):
  for j in range (len(allSequences[i])):
    if allSequences[i].count(allSequences[i][j])>1:
      badArrays.append(i)
      break


answer=100

for i in range (101):
  if i not in badArrays:
    answer=i
    break

answer+=1

outFile.write(str(answer)+"\n")

outFile.close()
