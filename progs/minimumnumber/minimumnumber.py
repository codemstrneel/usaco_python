"""
Bessie forgot her password. But she can remember some of the 
characters. The length of the password is L (1 <= L <= 30), 
composed of 0's and 1's. She knows that the password can be 
split into one or more numbers (not necessarily unique) from a 
list composed of N (1 <= N <= 20) unique numbers. A numbers is 
defined as a sequence of at most 20 0's and 1's. She also remembers 
certain letters from her password along with their positions.

Consider the following example. Bessie knows that her password 
looks like "?01?11101?1100?" ('?' represents a letter she cannot 
remember), and her list has the following numbers:

01100
110
11
101
11001
01

She cannot remember at most 10 digits. The two possible passwords 
for Bessie to have are "101011101111001" and "101111101111001". 
Passwords can be decomposed as follows:

101 01 110 11 110 01
101 01 110 11 11001

101 11 110 11 110 01
101 11 110 11 11001

Given the list, and the digits that Bessie remembers, please find 
her password. If more than one password is valid, find the smallest 
number that works.

PROBLEM NAME: minnum

INPUT FORMAT:

* Line 1: Two space-separated integers: L and N

* Line 2: A string of length L

* Lines 3..N+2: Line i+2 contains the ith number in the list

SAMPLE INPUT:

15 6
?01?11101?1100?
01100
110
11
101
11001
01

OUTPUT FORMAT:

* Line 1: The smallest password that fits. If there is no
          solution, the output should be "NO SOLUTION".

SAMPLE OUTPUT:

101011101111001
"""
def listToString(s):  

    str1 = ""    
    for ele in s:  
        str1 += ele    
    return str1 
import copy

def match(arrIdx,currIdx):
  global numberArr
  global allNumbers
  for i in range(len(numberArr[arrIdx])):
    if allNumbers[currIdx+i]!="?" and allNumbers[currIdx+i]!=numberArr[arrIdx][i]:
      return False
  return True

allArr=[]
temp=input().split()

length=int(temp[0])

numbers=int(temp[1])

allNumbers=list(input())

numberArr=[]
for i in range(numbers):
  numberArr.append(list(input()))
#print(numberArr)
#print(numberArr)

dp=[" "]*(1001)
#print(dp)
for i in range(length-1,-1,-1):

  for j in range(numbers):
    k=i+len(numberArr[j])
    if k<=length and  (k==length or dp[k]!=" ") and match (j,i):
      x=[]
      if k==length:
        x=numberArr[j]
      else:
        x=numberArr[j]+dp[k]
      #print(x)
      #print(str(dp[i])+str(123))
      #print(k)
      if (dp[i]==" "):
        #print(x)
        dp[i]=x
      
      elif dp[i]>x:
        dp[i]=x


#print(dp[0])
answer=listToString(dp[0])
if answer!=" ":
  print(str(answer))
  
else:
  print("NO SOLUTION")
