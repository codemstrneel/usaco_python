"""
ID: neelkolhe
TASK: lifeguards
"""
from enum import Enum
class Lap(Enum):
  START = 0
  END = 1

class Idx(Enum):
  TIME=0
  LAP=1
  NUM=2

inpFile=open('lifeguards.in','r')
outFile=open('lifeguards.out','w')

numberLifeGuards=int(inpFile.readline())

times=[]
for i in range (numberLifeGuards):
  arr=inpFile.readline().split()
  times.append([int(arr[0]),0,i])
  times.append([int(arr[1]),1,i])

times.sort()
#print(times)
totalTime=0
countActive=0
currActive=[]
minimumOverlap=[0]*numberLifeGuards
for i in range (2*numberLifeGuards):
  #print(totalTime, " ", " ", countActive )
  if countActive>0:
    totalTime+=(times[i][0]-times[i-1][0])
  if countActive==1 :
    minimumOverlap[currActive[0]]+=(times[i][0]-times[i-1][0])
  if times[i][1]==int(1):
    currActive.remove(times[i][2])
    countActive-=1
  else:
    currActive.append(times[i][2])
    countActive += 1


#print(totalTime)

print(totalTime-min(minimumOverlap))

outFile.write(str(totalTime-min(minimumOverlap)))
outFile.close()

