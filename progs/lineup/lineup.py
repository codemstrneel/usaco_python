"""
ID: neelkolhe
TASK: lineup
"""



import itertools


  
inpFile=open('lineup.in','r')
outFile=open('lineup.out','w')

numberStatements=int(inpFile.readline())

people=["Beatrice","Belinda", "Bella", "Bessie", "Betsy",  "Blue","Buttercup", "Sue"]

statements=[]

for i in range (numberStatements):
  x=inpFile.readline().split()
  statements.append([x[0],x[5]])



for i in range(numberStatements):
  statements[i].sort()

statements.sort()

allSequences=list(itertools.permutations(people))
answer=0
for i in range(40320):
  a=0
  for j in range(numberStatements):
    tempVar=allSequences[i].index(statements[j][0])
    if tempVar!=0 and tempVar!=7:
      if statements[j][1]==allSequences[i][(tempVar-1)] or statements[j][1]==allSequences[i][(tempVar+1)]:
        a+=1
    elif tempVar==0:
      if statements[j][1]==allSequences[i][1]:
        a+=1
    elif tempVar==7:
      if statements[j][1]==allSequences[i][6]:
        a+=1
  if a==numberStatements:
    answer=i
    break

for i in range(8):
  outFile.write(str(allSequences[answer][i])+"\n")

outFile.close()
    
