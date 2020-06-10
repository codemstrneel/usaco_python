"""
ID: neel1
LANG: PYTHON3
TASK: subset
"""



inpFile=open('subset.in','r')
outFile=open('subset.out','w')

steps=0
number=int(inpFile.readline())
sumNum=int((number*(number+1))/2)
necessaryNum=int(sumNum/2)


if sumNum%2==1:
  outFile.write(str(0)+"\n")
else:
  arr=[0]*(necessaryNum+1)
  arr[0]=1
  for i in range(1,number+1):
    print(i)
    for j in range(necessaryNum,i-1,-1):
      arr[j]+=arr[j-i]
      print(str(j)+" "+str(arr[j]))
  answer=arr[necessaryNum]/2
  print(answer)
  outFile.write(str(int(answer))+"\n")

outFile.close()
