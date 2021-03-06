"""
ID: neelkolhe
TASK: perimeter
"""
import sys
sys.setrecursionlimit(10**6)



inpFile=open('perimeter.in','r')
outFile=open('perimeter.out','w')

numberLines=int(inpFile.readline())

arr=[]

print(numberLines)
for i in range (numberLines):
  x=(inpFile.readline())
  arr.append(list(x))
  del(arr[i][numberLines])

area=0
visited=[]
for i in range(numberLines):
  tempArr=[]
  for j in range(numberLines):
    tempArr.append(False)
  visited.append(tempArr)
  
#print(visited)
perimeter=0

def recurse(x,y):
  global area
  global perimeter

  visited[x][y]=True
  #print(x,y)
  #print(visited)
  area+=1
  if x>0:
    if arr[x-1][y] =='#':
      if not visited[x-1][y]:
        recurse(x-1,y)
    else:
      perimeter+=1
  else:
    perimeter+=1
  if y>0:
    if arr[x][y-1]== '#':
      if not visited[x][y-1]:
        recurse(x,y-1)
    else:
      perimeter+=1
  else:
    perimeter+=1
  if x<numberLines-1:
    if arr[x+1][y] == '#':
      if not visited[x+1][y]:
        recurse(x+1,y)
    else:
      perimeter+=1
  else:
      perimeter+=1
  if y<numberLines-1:
    if arr[x][y+1] == '#':
      if not visited[x][y+1]:
        recurse(x,y+1)
    else:
      perimeter+=1
  else:
      perimeter+=1


values=[]

for i in range(numberLines):
  for j in range(numberLines):
    if not visited[i][j] and arr[i][j]== '#':
      area=0
      perimeter=0
      recurse(i,j)
      values.append([area,perimeter])
print(values)

answer=[0,0]

for i in range (len(values)):
  if values[i][0]>answer[0]:
    answer=values[i]
  elif values[i][0]==answer[0]:
    if values[i][1]< answer[1]:
      answer=values[i]

print(answer)

