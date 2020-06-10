

numberGames=int(input())

allGames=[]

for i in range(numberGames):
  allGames.append(input())


arr=[[0,0,0]]

for i in range(numberGames):
  if allGames[i]=="H":
    arr[0][0]+=1
  if allGames[i]=="P":
    arr[0][1]+=1
  if allGames[i]=="S":
    arr[0][2]+=1
for i in range(numberGames):
  if allGames[numberGames-i-1]=="H":
    arr.append([arr[i][0]-1,arr[i][1],arr[i][2]])
  if allGames[numberGames-i-1]=="P":
    arr.append([arr[i][0],arr[i][1]-1,arr[i][2]])
  if allGames[numberGames-1-i]=="S":
    arr.append([arr[i][0],arr[i][1],arr[i][2]-1])

arr.reverse()

#print(arr)
maximum=0

for i in range(numberGames):
  x=0
  for j in range(3):
    if arr[numberGames][j]-arr[i][j]>x:
      x=arr[numberGames][j]-arr[i][j]
  maximum=max(maximum,max(arr[i])+x)


print(maximum)
