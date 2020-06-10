"""
ID: neel1
LANG: PYTHON3
TASK: holstein
"""

import copy

def recurse(feedNumber, counter):
  global necessaryFeeds
  global numberVit
  global numberFeeds
  global typesOfFeeds
  global currFeeds
  global currList
  global minList
  global minCounter

  localCounter=counter+1
  currList.append(feedNumber)
  
  for i in range(numberVit):
    currFeeds[i]-=typesOfFeeds[feedNumber][i]

  done=0
  for i in range(numberVit):
    if currFeeds[i]<=0:
      done+=1
  if done==numberVit:
    #print("=====")
    #print(done)
    #print(currFeeds)
    #print(currList)
    #print("----")
    if localCounter < minCounter:
      minList = copy.copy(currList)
      #print(minList)
      minCounter = localCounter
    return
 
  if localCounter >= minCounter:
    return

  for i in range(feedNumber+1,numberFeeds):
    tmpList = copy.copy(currList)
    tmpFeeds = copy.copy(currFeeds)
    recurse(i,localCounter)
    currList = copy.copy(tmpList)
    currFeeds = copy.copy(tmpFeeds)

  return  





inpFile=open('holstein.in','r')
outFile=open('holstein.out','w')


numberVit=int(inpFile.readline())
#print(numberVit)
necessaryFeeds=inpFile.readline().split()
for i in range (numberVit):
  necessaryFeeds[i]=int(necessaryFeeds[i])
#print(necessaryFeeds)

numberFeeds=int(inpFile.readline())
#print(numberFeeds)
typesOfFeeds=[0]*numberFeeds
for i in range (numberFeeds):
  typesOfFeeds[i]=inpFile.readline().split()
for i in range (numberFeeds):
  for j in range (numberVit):
    typesOfFeeds[i][j]=int(typesOfFeeds[i][j])
  #print(typesOfFeeds[i])

minList=[]
minCounter=numberFeeds+1


for i in range(numberFeeds):
  currList=[]
  currFeeds = copy.copy(necessaryFeeds)
  recurse(i,0)
  

print(minCounter)
print(minList)

outFile.write(str(minCounter)+" ")

for i in range(minCounter):
  outFile.write(str(minList[i]+1))
  if i<minCounter-1:
    outFile.write(" ")

outFile.write("\n")
outFile.close()
