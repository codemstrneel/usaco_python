"""
Some companies are partial owners of other companies because they have acquired part of their total shares of stock. For example, Ford at one point owned 12% of Mazda. It is said that a company A controls company B if at least one of the following conditions is satisfied:

Company A = Company B
Company A owns more than 50% of Company B
Company A controls K (K >= 1) companies denoted C1, …, CK with each company Ci owning xi% of company B and x1 + …. + xK > 50%.
Given a list of triples (i,j,p) which denote company i owning p% of company j, calculate all the pairs (h,s) in which company h controls company s. There are at most 100 companies.

Write a program to read the list of triples (i,j,p) where i, j and p are positive integers all in the range (1..100) and find all the pairs (h,s) so that company h controls company s.

PROGRAM NAME: concom
INPUT FORMAT
Line 1:	N, the number of input triples to follow
Line 2..n+1:	Three integers per line as a triple (i,j,p) described above.
SAMPLE INPUT (file concom.in)
3
1 2 80
2 3 80
3 1 20
Copy
OUTPUT FORMAT
List 0 or more companies that control other companies. Each line contains two integers that denote that the company whose number is the first integer controls the company whose number is the second integer. Order the lines in ascending order of the first integer (and ascending order of the second integer to break ties). Do not print that a company controls itself.

SAMPLE OUTPUT (file concom.out)
1 2
1 3
2 3
"""


"""
ID: neel1
TASK: concom
LANG: PYTHON3
"""

inpFile = open('concom.in', 'r')
outFile = open('concom.out', 'w')

def controller(i,j):
  global controls
  global owns
  global numberCompanies

  if controls[i][j]:
    return
  controls[i][j]=True
  for k in range(numberCompanies):
    owns[i][k]+=owns[j][k]
  for k in range(numberCompanies):
    if controls[k][i]:
      controller(k,j)
  for k in range(numberCompanies):
    if owns[i][k]>50:
      controller(i,k)
  

def addOwns(a,b,c):
  global controls
  global owns
  global numberCompanies

  for k in range(numberCompanies):
    if controls[k][a]:
      owns[k][b]+=c
  
  for k in range(numberCompanies):
    if owns[k][b]>50:
      controller(k,b)



numberLines=int(inpFile.readline())
controls=[[False]*100 for i in range(100)]
owns=[[0]*100 for i in range(100)]
numberCompanies=100
for i in range (100):
  controls[i][i]=True
print(controls)
for i in range(numberLines):
  temp=inpFile.readline().split()
  #owns[int(temp[0])-1][int(temp[1])-1]+=int(temp[2])
  addOwns(int(temp[0])-1,int(temp[1])-1,int(temp[2]))

answer=[]
for i in range(100):
  for j in range(100):
    if i!=j and owns[i][j]>50:
      answer.append([i+1,j+1])

#print(answer)
answer.sort()

for i in range(len(answer)):
  outFile.write(str(answer[i][0])+' '+str(answer[i][1])+"\n")

outFile.close()
