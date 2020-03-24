"""
ID: neelkolhe
TASK: bcount
"""


inpFile=open('bcount.in','r')
outFile=open('bcount.out','w')

arr=inpFile.readline().split()

numberCows=int(arr[0])

numberRanges=int(arr[1])
allCows=[0]
cow1=0
cow2=0
cow3=0
for i in range (numberCows):
  allCows.append(int(inpFile.readline()))
  if allCows[i+1]==1:
    cow1+=1
  elif allCows[i+1]==2:
    cow2+=1
  elif allCows[i+1]==3:
    cow3+=1

print(allCows)
print(cow1)
print(cow2)
print(cow3)
ranges=[]
for i in range(numberRanges):
  tempArr=inpFile.readline().split()
  ranges.append([int(tempArr[0]),int(tempArr[1])])

for i in range (numberRanges):
  TempCounter1=0
  TempCounter2=0
  TempCounter3=0
  if (ranges[i][1]-ranges[i][0]+1)>(numberCows/2):
    for j in range (1,ranges[i][0]):
      if allCows[j]==1:
        TempCounter1+=1
      elif allCows[j]==2:
        TempCounter2+=1
      elif allCows[j]==3:
        TempCounter3+=1
    for j in range (ranges[i][1]+1,numberCows+1):
      if allCows[j]==1:
        TempCounter1+=1
      elif allCows[j]==2:
        TempCounter2+=1
      elif allCows[j]==3:
        TempCounter3+=1
    outFile.write(str(cow1-TempCounter1)+" "+str(cow2-TempCounter2) + " " + str(cow3-TempCounter3)+ "\n")
  else:
    for j in range(ranges[i][0],ranges[i][1]+1):
      if allCows[j]==1:
        TempCounter1+=1
      elif allCows[j]==2:
        TempCounter2+=1
      elif allCows[j]==3:
        TempCounter3+=1
    outFile.write(str(TempCounter1)+" " +str(TempCounter2)+ " " + str(TempCounter3) + "\n")

outFile.close()
