"""
ID: neelkolhe
TASK: castle
LANG: PYTHON3
"""


def recurse(i,j):
  global visited
  global arr
  global numberCol
  global numberRow
  global allAreas
  global currRoom
  global allSquares
  allSquares[i][j]=currRoom
  visited[i][j]=True
  currArea=0
  currArea+=1
  
  if (j>0) and (visited[i][j-1]==False) and (arr[i][j][0]!=1):
    currArea+=recurse(i,j-1)
  if i>0 and visited[i-1][j]==False and arr[i][j][1]!=2:
    currArea+=recurse(i-1,j)
  if j<numberCol-1 and visited[i][j+1]==False and arr[i][j][2]!=4:
    currArea+=recurse(i,j+1)
  if i<numberRow-1 and visited[i+1][j]==False and arr[i][j][3]!=8:
    currArea+=recurse(i+1,j)
  return(currArea)

  
  

  


inpFile=open('castle.in','r')
outFile=open('castle.out','w')

temp=inpFile.readline().split()

numberCol=int(temp[0])
numberRow=int(temp[1])

arr=[]
for i in range(numberRow):
  temp=inpFile.readline().split()
  appender=[]
  for j in range(numberCol):
    temp[j]=int(temp[j])
    x=[]
    x.append((temp[j] & 1))
    x.append((temp[j] & 2))
    x.append((temp[j] & 4))
    x.append((temp[j] & 8))
    appender.append(x)
  arr.append(appender)

#print(arr)


visited=[]

for i in range(numberRow):
  temp=[]
  for j in range(numberCol):
    temp.append(False)  
  visited.append(temp)



currRoom=0
allSquares=[[0 for i in range(numberCol)]  for j in range(numberRow)]


allAreas=[]
for i in range(numberRow):
  for j in range(numberCol):
    if not visited[i][j]:
      currRoom+=1
      x=recurse(i,j)
      allAreas.append(x)

#print(allAreas)
#
#print(allSquares)

maxDouble=0
places=[]

for i in range(numberRow):
  for j in range(numberCol):
    if i<numberRow-1 and allSquares[i][j]!=allSquares[i+1][j]:
      #print(str(i)+" " + str(j))
      doubleArea=allAreas[allSquares[i][j]-1]+allAreas[allSquares[i+1][j]-1]
      if doubleArea>maxDouble:
        maxDouble=doubleArea
        places=[[i+2,j+1,'N']]
      elif doubleArea==maxDouble:
        places.append([i+2,j+1,'N'])
    if j<numberCol-1 and allSquares[i][j]!=allSquares[i][j+1]:
      doubleArea=allAreas[allSquares[i][j]-1]+allAreas[allSquares[i][j+1]-1]
      if doubleArea>maxDouble:
        maxDouble=doubleArea
        places=[[i+1,j+1,'E']]
      elif doubleArea==maxDouble:
        places.append([i+1,j+1,'E'])

places.sort()
#print(maxDouble)
print(places)
lenPlac=len(places)


currIdx=[]
currAnswer=[10000000,10000000,'E']
for i in range(len(places)):
  if places[i][1]<currAnswer[1]:
    currIdx=i
    currAnswer=places[i]
  elif places[i][1]==currAnswer[1]:
    if places[i][0]>currAnswer[0]:
      currAnswer=places[i]
    else:
      if places[i][0]==currAnswer[0]:
        if currAnswer[2]=='E':
          currAnswer=places[i]


outFile.write(str(len(allAreas))+ "\n" + str(max(allAreas)) + "\n" + str(maxDouble) + "\n")
print(currAnswer)
outFile.write(str(currAnswer[0])+" ")
outFile.write(str(currAnswer[1])+" ")
outFile.write(str(currAnswer[2]))

outFile.write("\n")
outFile.close()
