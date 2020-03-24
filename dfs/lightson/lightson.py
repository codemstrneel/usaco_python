"""
ID: neelkolhe
TASK: lightson
"""


inpFile=open('lightson.in','r')
outFile=open('lightson.out','w')

arr=inpFile.readline().split()

numberRooms=int(arr[0])

numberConnections=int(arr[1])

allConnections=[]

for i in range(numberConnections):
  arr=inpFile.readline().split()
  allConnections.append([[int(arr[0]),int(arr[1])],[int(arr[2]),int(arr[3])]])
  print(allConnections[i])
counter=0
visited=[]
turnedON=[[1,1]]
def recurse(x,y):
  global counter
  counter+=1
  visited.append([x,y])
  for i in range (numberConnections):
    if [x,y]==allConnections[i][0]:
      turnedON.append(allConnections[i][1])
  if [x,y+1] in turnedON and [x,y+1] not in visited:
    print([x,y+1])
    recurse(x,y+1)
  if [x,y-1] in turnedON and [x,y-1] not in visited:
    print
    recurse(x,y-1)
  if [x+1,y] in turnedON and [x+1,y] not in visited:
    recurse(x+1,y)
  if [x-1,y] in turnedON and [x-1,y] not in visited:
    recurse(x-1,y)
  return

print(turnedON)
recurse(1,1)

print(counter)

    
