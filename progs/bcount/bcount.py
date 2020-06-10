inpFile=open('bcount.in','r')
outFile=open('bcount.out','w')

arr=inpFile.readline().split()

numberCows=int(arr[0])

numberRanges=int(arr[1])
allCows=[0]
newArr=[[0,0,0]]
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
  newArr.append([cow1,cow2,cow3])
#print(newArr)

allQuer=[]
for i in range(numberRanges):
  x=input().split()
  allQuer.append([int(x[0]),int(x[1])])

#print(allQuer)



for i in range(numberRanges):
  holsteins=newArr[allQuer[i][1]][0]-newArr[allQuer[i][0]-1][0]
  guerneys=newArr[allQuer[i][1]][1]-newArr[allQuer[i][0]-1][1]
  jerseys=newArr[allQuer[i][1]][2]-newArr[allQuer[i][0]-1][2]
  print(str(holsteins)+" "+str(guerneys)+" "+str(jerseys))
