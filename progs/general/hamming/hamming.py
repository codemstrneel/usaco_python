"""
ID: neel1
LANG: PYTHON3
TASK: hamming
"""

def hammingDistance(n1, n2) : 
  
    x = n1 ^ n2  
    setBits = 0
  
    while (x > 0) : 
        setBits += x & 1
        x >>= 1
      
    return setBits

inpFile=open('hamming.in','r')
outFile=open('hamming.out','w')

temp=inpFile.readline().split()

numberWords=int(temp[0])
bitLen=int(temp[1])
minDis=int(temp[2])

allWords=[0]
counter=1

maxLen=2**bitLen
for i in range(1,maxLen):
  currCounter=0
  for j in range(counter):
    if hammingDistance(i,allWords[j])>=minDis:
      currCounter+=1
  if currCounter==counter:
    allWords.append(i)
    counter+=1

  if counter==numberWords:
    break

print(allWords)
currLine=0
for i in range(numberWords):
  if currLine<9:
    if i !=numberWords-1:
      outFile.write(str(allWords[i])+" ")
    else:
      outFile.write(str(allWords[i])+"\n")
    currLine+=1
  elif currLine==9:
    outFile.write(str(allWords[i])+"\n")
    currLine=0

outFile.close()
