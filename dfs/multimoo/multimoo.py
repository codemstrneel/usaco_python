
"""
ID: neelkolhe
TASK: multimoo
"""



inpFile=open('multimoo.in','r')
outFile=open('multimoo.out','w')

numberRows=int(inpFile.readline())
map=[]
cowNumbers=[]
for i in range(numberRows):
  map.append(inpFile.readline().split())
  

for i in range(numberRows):
  for j in range(numberRows):
    
    map[i][j]=int(map[i][j])
# for i in range(numberRows):
#   print(map[i])


visited=[]

def recurse(cowNumberone,cownumbertwo,x,y):
  global counter
  counter+=1
  visited.append([x,y])
  if x>0 and [x-1,y] not in visited and (cowNumberone==map[x-1][y] or cownumbertwo==map[x-1][y]):
    recurse(cowNumberone,cownumbertwo,x-1,y)
  if y>0 and [x,y-1] not in visited and(cowNumberone==map[x][y-1] or cownumbertwo==map[x][y-1]):
    recurse(cowNumberone,cownumbertwo, x,y-1)
  if x<numberRows-1 and [x+1,y] not in visited and (cowNumberone==map[x+1][y] or cownumbertwo==map[x+1][y]):
    recurse(cowNumberone,cownumbertwo,x+1,y)
  if y<numberRows-1  and [x,y+1] not in visited and (cowNumberone==map[x][y+1] or cownumbertwo==map[x][y+1]):
    recurse (cowNumberone,cownumbertwo,x, y+1)
  
  return

allCombos=[]

for i in range (numberRows):
  for j in range (numberRows):
    counter=0
    visited=[]
    recurse(map[i][j],map[i][j],i,j)
    allCombos.append(counter)

# print(allCombos)

newCombosright=[]
for i in range (numberRows):
  for j in range (numberRows-1):
    counter=0
    visited=[]
    recurse(map[i][j],map[i][j+1],i,j)
    newCombosright.append(counter)
newCombosleft=[]
for i in range(numberRows-1):
  for j in range (numberRows):
    counter=0
    visited=[]
    recurse(map[i][j],map[i+1][j],i,j)
    newCombosleft.append(counter)

answerSmall=max(allCombos)

answerBig=max(max(newCombosleft),max(newCombosright))
print(answerSmall)
print(answerBig)



  

