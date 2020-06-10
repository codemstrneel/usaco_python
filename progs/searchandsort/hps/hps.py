"""
ID: neelkolhe
TASK: hps
"""


inpFile=open('hps.in','r')
outFile=open('hps.out','w')

numberTurns=int(inpFile.readline())
arr=[]

for i in range (numberTurns):
  arr.append(inpFile.readline().split())

hLeft=[0]

pLeft=[0]

sLeft=[0]

hRight=[0]

pRight=[0]

sRight=[0]


for i in range(numberTurns):
  if arr[i]==['P']:
    pLeft.append(pLeft[i]+1)
    hLeft.append(hLeft[i])
    sLeft.append(sLeft[i])

  if arr[i]==['H']:
    pLeft.append(pLeft[i])
    hLeft.append(hLeft[i]+1)
    sLeft.append(sLeft[i])

  if arr[i]==['S']:
    pLeft.append(pLeft[i])
    hLeft.append(hLeft[i])
    sLeft.append(sLeft[i]+1)

for i in range(numberTurns):
  if arr[numberTurns-i-1]==['P']:
    pRight.append(pRight[i]+1)
    hRight.append(hRight[i])
    sRight.append(sRight[i])

  if arr[numberTurns-i-1]==['H']:
    pRight.append(pRight[i])
    hRight.append(hRight[i]+1)
    sRight.append(sRight[i])

  if arr[numberTurns-i-1]==['S']:
    pRight.append(pRight[i])
    hRight.append(hRight[i])
    sRight.append(sRight[i]+1)

del sRight[0]
del pRight[0]
del hRight[0]
del sLeft[0]
del pLeft[0]
del hLeft[0]

addition=0
for i in range (numberTurns):
  if ((max(pLeft[i],sLeft[i],hLeft[i]))+(max(pRight[numberTurns-i-1],sRight[numberTurns-i-1], hRight[numberTurns-i-1])))>addition:
    addition=(max(pLeft[i],sLeft[i],hLeft[i])+max(pRight[numberTurns-i-1],sRight[numberTurns-1-i], hLeft[numberTurns-i-1]))
  
print(addition)

