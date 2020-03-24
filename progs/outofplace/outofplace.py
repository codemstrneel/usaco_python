"""
ID: neel1
LANG: PYTHON3
TASK: outofplace
"""



inpFile=open('outofplace.in','r')
outFile=open('outofplace.out','w')

numberCows=int(inpFile.readline())

cowHeights=[]
for i in range (numberCows):
  cowHeights.append(int(inpFile.readline()))

sortedHeights=[0]*numberCows

for i in range(numberCows):
  sortedHeights[i]=cowHeights[i]
sortedHeights.sort()
print(sortedHeights)
print(cowHeights)

counter=0
for i in range (numberCows):
  if cowHeights[i]!=sortedHeights[i]:
    counter+=1

print(counter)

answer=counter-1
if answer<0:
  answer=0

outFile.write(str(answer)+"\n")

outFile.close()
