"""
ID: neel1
TASK: zerosum
LANG: PYTHON3
"""
import sys
sys.setrecursionlimit(20000)

import copy
def getInt(integers):
  strings = [str(integer) for integer in integers]
  a_string = "".join(strings)
  an_integer = int(a_string)
  return(an_integer)
allArr=[]
counter=0
def recurse(length):
  global numbers
  global currArr
  global allArr
  global counter
  if length==(numbers-1):

    allArr.append(copy.copy(currArr))
    #print(allArr)
    return (length)
  
  currArr.append("+")
  x=length
  length+=1
  recurse(length)
  length=x
  del(currArr[length])
  currArr.append("-")
  x=length
  length+=1
  recurse(length)
  length=x
  del(currArr[length])
  currArr.append(" ")
  x=length
  length+=1
  recurse(length)
  length=x
  del(currArr[length])
  return
  


inpFile = open('zerosum.in', 'r')
outFile = open('zerosum.out', 'w')

numbers=int(inpFile.readline())

currArr=[]
allArr=[]
recurse(0)
#print(allArr)



answers=[]
for i in range (3**(numbers-1)):
  x=allArr[i]
  prevSign="+"
  totalSum=1
  currArr=[]
  for j in range(numbers-1):
    if x[j]=="+":
      
      totalSum+=(j+2)
      if j>0 and x[j-1]==" ":
        
        if prevSign=="+":
          totalSum+=getInt(currArr)
          currArr=[]
        else:
          totalSum-=getInt(currArr)
          currArr=[]
    elif x[j]=="-":
      
      totalSum-=(j+2)
      if j>0 and x[j-1]==" ":
        
        if prevSign=="+":
          totalSum+=getInt(currArr)
          currArr=[]
        else:
          totalSum-=getInt(currArr)
          currArr=[]
    else:
      

      if j==0:
        
        currArr.append(1)
        currArr.append(2)
        totalSum-=1
      else:
        if x[j-1]!=" ":
          currArr.append(j+1)
          currArr.append(j+2)
          if x[j-1]=="+":
            prevSign="+"
            
            totalSum-=(j+1)
          
          else:
            prevSign="-"
            totalSum+=(j+1)
        else:
          currArr.append(j+2)
          
      
      if j==numbers-2:
        if prevSign=="+":
          totalSum+=getInt(currArr)
        else:
          totalSum-=getInt(currArr)
  if totalSum==0:
    answers.append(x)
        


          



answers.sort()
for i in range(len(answers)) :  
  print(answers[i])
for i in range(len(answers)):
  outFile.write(str(1))
  for j in range(numbers-1):
    outFile.write(str(answers[i][j]))
    outFile.write(str(j+2))
  outFile.write("\n")

outFile.close()




