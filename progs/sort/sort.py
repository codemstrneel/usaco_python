"""
ID: neelkolhe
TASK: sort
"""

inpFile=open('sort.in','r')
outFile=open('sort.out','w')

numbers=int(inpFile.readline())

arr=[]
sortedArr=[]
for i in range(numbers):
  x=int(inpFile.readline())
  arr.append(x)
  sortedArr.append([x,i])

sortedArr.sort()

eachDifference=[]

for i in range(numbers):
  eachDifference.append(abs(i-sortedArr[i][1]))

print(eachDifference)

answer=max(eachDifference)+1
print(answer)

