

temp=input().split()

N=int(temp[0])

K=int(temp[1])
arr=[]
for i in range(K):
  temp=input().split()
  for j in range (2):
    temp[j]=int(temp[j])
  if temp[0]<temp[1]:
    arr.append(temp)
  
  else:
    arr.append([temp[1],temp[0]])
  #print(temp)

LHS=1
count=0
while LHS<=N:
  RHS=N
  for i in range(K):
    if LHS<=arr[i][0] and RHS>=arr[i][1]:
      RHS=arr[i][1]-1
  count+=1
  LHS=RHS+1
print(count)
  
