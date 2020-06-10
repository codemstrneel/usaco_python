"""
The structure of some biological objects is represented by the sequence of their constituents, where each part is denoted by an uppercase letter. Biologists are interested in decomposing a long sequence into shorter sequences called primitives.

We say that a sequence S can be composed from a given set of primitives P if there is a some sequence of (possibly repeated) primitives from the set whose concatenation equals S. Not necessarily all primitives need be present. For instance the sequence ABABACABAAB can be composed from the set of primitives

{A, AB, BA, CA, BBC}
Copy
The first K characters of S are the prefix of S with length K. Write a program which accepts as input a set of primitives and a sequence of constituents and then computes the length of the longest prefix that can be composed from primitives.

PROGRAM NAME: prefix
INPUT FORMAT
First, the input file contains the list (length 1..200) of primitives (length 1..10) expressed as a series of space-separated strings of upper-case characters on one or more lines. The list of primitives is terminated by a line that contains nothing more than a period (‘.’). No primitive appears twice in the list. Then, the input file contains a sequence S (length 1..200,000) expressed as one or more lines, none of which exceeds 76 letters in length. The “newlines” (line terminators) are not part of the string S.

SAMPLE INPUT (file prefix.in)
A AB BA CA BBC
.
ABABACABAABC

OUTPUT FORMAT
A single line containing an integer that is the length of the longest prefix that can be composed from the set P.

SAMPLE OUTPUT (file prefix.out)
11
"""


"""
ID: neel1
TASK: prefix
LANG: PYTHON3
"""
def matchesPattern(p1, startingPoint, p2):
  global allPrefix
  global lensOfArr
  
  if lensOfArr[p2]+startingPoint <= lensOfArr[p1]:
    for  j in range(lensOfArr[p2]):
      if allPrefix[p2][j]!=allPrefix[p1][startingPoint+j]:
        return False
  else:
    return False
  return True

def matches(startingPoint, prefIDX):
  global allLetters
  global realWord
  global allPrefix
  global lensOfArr
  lp=lensOfArr[prefIDX]
  #print(lp)
  pattern=allPrefix[prefIDX]
  if lp+startingPoint<=allLetters:
    for j in range(lp):
      if pattern[j]!=realWord[startingPoint+j]:
        return False
  else:
    return False
  return True



inpFile = open('prefix.in', 'r')
outFile = open('prefix.out', 'w')


x=inpFile.readline().split()
allPrefix=[]
while x!=["."]:
  for i in range(len(x)):
    allPrefix.append(x[i])
  x=inpFile.readline().split()
#print(allPrefix)
numberPrefix=len(allPrefix)

realWord=[]
prefixLen=[]

x=inpFile.readline()
while x!="":
  curr=list(x)
  for i in range(len(curr)):
    if curr[i]!="\n":
      realWord.append(curr[i])
      prefixLen.append(-1)
  x=inpFile.readline()
#print(realWord)
allLetters=len(realWord)

for i in range(numberPrefix):
  allPrefix[i]=list(allPrefix[i])
lensOfArr=[]
allPrefix=sorted(allPrefix,key=len)
for i in range(numberPrefix):
  lensOfArr.append(len(allPrefix[i]))
#print(allPrefix)
needed=[True]*numberPrefix
for i in range(numberPrefix):
  visitedPrefix=[False]*(lensOfArr[i]+1)
  #print(allPrefix[i])
  visitedPrefix[0]=True
  for j in range(lensOfArr[i]):

    
    if visitedPrefix[j]:
      
      for k in range(i):
        
        idx=j+lensOfArr[k]
        #print(idx)
        if idx<=lensOfArr[i] and not visitedPrefix[idx] and matchesPattern(i, j, k):
            visitedPrefix[idx]=True
            
            #print(idx)
        #elif i==1 and not matchesPattern(i,j,k):
          #print("not matches" + str(idx))
            
  if visitedPrefix[lensOfArr[i]] and lensOfArr[i]!=1:
    #print("Not Needed\n")
    needed[i]=False
#print(needed)
#for i in range(numberPrefix):
  #if not needed[i]:
    #print(i)

for i in range(numberPrefix-1,-1,-1):
  if not needed[i]:
    del allPrefix[i]
numberPrefix=len(allPrefix)
#print(allPrefix)
print(allPrefix)

visited=[False]*(allLetters+1)
visited[0]=True
lensOfArr=[]
for i in range(numberPrefix):
  lensOfArr.append(len(allPrefix[i]))
#print(lensOfArr)
for i in range(allLetters+1):
  if visited[i]:
    for j in range(numberPrefix):
      if i+lensOfArr[j]<=allLetters and not visited[i+lensOfArr[j]]:
        if matches(i,j):
          visited[i+lensOfArr[j]]=True

answer=0
for i in range (allLetters,-1,-1):
  if visited[i]:
    answer=i
    break

outFile.write(str(answer)+"\n")
outFile.close()
