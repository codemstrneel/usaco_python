
"""
ID: neelkolhe
TASK: planting
"""



inpFile=open('planting.in','r')
outFile=open('planting.out','w')

grass=[0]*100001

numberFields=int(inpFile.readline())

for i in range (numberFields-1):
  x=inpFile.readline().split()
  grass[int(x[0])]+=1
  grass[int(x[1])]+=1


answer=max(grass)+1

print(answer)
