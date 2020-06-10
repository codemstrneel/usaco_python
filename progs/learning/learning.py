

temp=input().split()

numberLines=int(temp[0])

leftSide=int(temp[1])

rightSide=int(temp[2])

allKnown=[]

for i in range(numberLines):
  temp=input().split()
  currArr=[int(temp[1])]
  if temp[0]=="S":
    currArr.append(1)
  else:
    currArr.append(0)
  allKnown.append(currArr)
#print(allKnown)
allKnown.sort()
#print(allKnown)
answer=0
for i in range(numberLines-1):
  LHS=allKnown[i][0]
  RHS=allKnown[i+1][0]
  middle=int((LHS+RHS)/2)
  if allKnown[i][1]==1:
    a=max(leftSide,LHS+1)
    b=min(rightSide,middle)
    if b>=a:
      answer+=(b-a+1)
  if allKnown[i+1][1]==1:
    a=max(leftSide,middle+1)
    b=min(rightSide,RHS)
    if b>=a:
      answer+=(b-a+1)
  if allKnown[i+1][1]==1 and allKnown[i][1]==0 and (LHS%2==RHS%2) and leftSide<=middle and middle<=rightSide:
    #print(i)
    answer+=1
#print(answer)
if allKnown[0][1]==1 and allKnown[0][0]>=leftSide:
  answer+=(allKnown[0][0]-leftSide+1)
  #print(allKnown[0][0])
  #print(leftSide)
if allKnown[numberLines-1][1]==1 and allKnown[numberLines-1][0]<rightSide:
  answer+=(rightSide-allKnown[numberLines-1][0]+1)
  #print(rightSide)
  #print(allKnown[numberLines-1])
 
print(answer)
