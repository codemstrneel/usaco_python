"""
ID: neelkolhe
TASK: highcard
"""


inpFile=open('highcard.in','r')
outFile=open('highcard.out','w')

numberCards=int(inpFile.readline())

maxCard=2*numberCards
elsieBool=[False]*(2*numberCards+1)
for i in range(numberCards):
  tempVar=int(inpFile.readline())
  elsieBool[tempVar]=True

elsieCard=[]


bessieCard=[]
for i in range(1,2*numberCards+1):
  if elsieBool[i]:
    elsieCard.append(i)
  else:
    bessieCard.append(i)
points=0
j=0
usedCards=[]
x=0
bessieNumber=0
elsieNumber=0

while bessieNumber<numberCards and elsieNumber<numberCards:
  if bessieCard[bessieNumber] > elsieCard[elsieNumber]:
    points+=1
    bessieNumber+=1
    elsieNumber+=1
  else:
    bessieNumber+=1

print(points)
