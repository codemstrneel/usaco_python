
temp=input().split()

numberBales=int(temp[0])
numberRanges=int(temp[1])

allDifferences=[0]*(numberBales+1)
for i in range(numberRanges):
  temp=input().split()
  x=int(temp[0])-1
  y=int(temp[1])-1
  allDifferences[x]+=1
  allDifferences[y+1]-=1


allValues=[0]*numberBales
value=0
for i in range(numberBales):
  value+=allDifferences[i]
  if i>0:
    allValues[i]=allValues[i-1]+allDifferences[i]
  else:
    allValues[i]+=allDifferences[i]
allValues.sort()
print(allValues[int(numberBales/2)])
