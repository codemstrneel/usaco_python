"""
ID: neelkolhe
TASK: moocast
"""


inpFile=open('div7.in','r')
outFile=open('div7.out','w')

numberCows=int(inpFile.readline())

allCows=[]
sums=[]
for i in range(numberCows):
  x=int(inpFile.readline())
  allCows.append(x%7)
  if i ==0:
    sums.append(x%7)
  else:
    sums.append((x+sums[i-1])%7)

print(allCows)
print(sums)

minimums=[]
counter=0
for i in range(7):
  for j in range(numberCows):
    if sums[j]==i:
      minimums.append(j)
      counter+=1
      break
  if counter!=i+1:
    minimums.append("none")
    counter+=1
  
print(counter)
counter=0
maximums=[]
for i in range(7):
  for j in range(numberCows):
    if sums[numberCows-j-1]==i:
      maximums.append(numberCows-j-1)
      counter+=1
      break
  if counter!=i+1:
    maximums.append("none")
    counter+=1

print(minimums)

print(maximums)


lists=[]
for i in range(7):
  if minimums[i]!="none":
    lists.append(maximums[i]-minimums[i])

print(lists)

answer=max(lists)
print(answer)

  
