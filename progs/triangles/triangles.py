"""
ID: neelkolhe
TASK: triangles
"""
from bisect import bisect_left

inpFile=open('triangles.in','r')
outFile=open('triangles.out','w')

numberOfVertices=int(inpFile.readline())

allVertices=[]
otherAllVertices=[]
for i in range (numberOfVertices):
  temp=inpFile.readline().split()
  allVertices.append([int(temp[0]), int (temp[1])])
  otherAllVertices.append([int(temp[0]), int (temp[1])])

otherAllVertices.sort(key=lambda k: [k[1], k[0]])
allVertices.sort()
xcords=[]
ycords=[]
for i in range(numberOfVertices):
  xcords.append(allVertices[i][0])
  ycords.append(otherAllVertices[i][1])
#print(allVertices)
#print(otherAllVertices)
areas=0
for i in range(numberOfVertices):
  x=allVertices[i][0]
  y=allVertices[i][1]
  firstx=bisect_left(xcords, x, lo=0,hi=numberOfVertices)
  secondx=bisect_left(xcords, x+1, lo=0,hi=numberOfVertices)
  allY=0
  if secondx!=-1:
    #print([firstx,secondx])
    for j in range(firstx,secondx):
      allY+=abs(allVertices[j][1]-y)
      #print("AllY + " + str(abs(allVertices[j][1]-y )))
  else:
    for j in range(firstx,numberOfVertices):
      allY+=abs(allVertices[j][1]-y)
        
  firsty=bisect_left(ycords, y, lo=0,hi=numberOfVertices)
  secondy=bisect_left(ycords, y+1, lo=0,hi=numberOfVertices)
  allX=0
  if secondy!=-1:
    for j in range(firsty,secondy):
      allX+=abs(otherAllVertices[j][0]-x)
  else:
    for j in range(firsty,numberOfVertices):
      allX+=abs(otherAllVertices[j][0]-x)
  #print(firstx,secondx,firsty,secondy)
  #print([allX,allY])
  areas+=((allY*allX)%(10^9+7))

outFile.write(str(areas%(10^9+7))+"\n")
outFile.close()
