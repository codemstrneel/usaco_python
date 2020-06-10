"""
Runaround numbers are integers with unique digits, none of which is zero (e.g., 81362) that also have an interesting property, exemplified by this demonstration:

If you start at the left digit (8 in our number) and count that number of digits to the right (wrapping back to the first digit when no digits on the right are available), you’ll end up at a new digit (a number which does not end up at a new digit is not a Runaround Number). Consider: 8 1 3 6 2 which cycles through eight digits: 1 3 6 2 8 1 3 6 so the next digit is 6.
Repeat this cycle (this time for the six counts designed by the ‘6’) and you should end on a new digit: 2 8 1 3 6 2, namely 2.
Repeat again (two digits this time): 8 1
Continue again (one digit this time): 3
One more time: 6 2 8 and you have ended up back where you started, after touching each digit once. If you don’t end up back where you started after touching each digit once, your number is not a Runaround number.
Given a number M (that has anywhere from 1 through 9 digits), find and print the next runaround number higher than M, which will always fit into an unsigned long integer for the given test data.

PROGRAM NAME: runround
INPUT FORMAT
A single line with a single integer, M

SAMPLE INPUT (file runround.in)
81361
Copy
OUTPUT FORMAT
A single line containing the next runaround number higher than the input value, M.

SAMPLE OUTPUT (file runround.out)
81362
"""

"""
ID: neel1
TASK: runround
LANG: PYTHON3
"""

inpFile = open('runround.in', 'r')
outFile = open('runround.out', 'w')
import sys 
  
INT_MAX = sys.maxsize; 
  
# Function to count distinct 
# digits in a number 
def countDistinct(n): 
  
    # To count the occurrence of digits 
    # in number from 0 to 9 
    arr = [0] * 10; 
    count = 0; 
  
    # Iterate over the digits of the number 
    # Flag those digits as found in the array 
    while (n != 0): 
        r = int(n % 10); 
        arr[r] = 1; 
        n //= 10; 
      
    # Traverse the array arr and count the 
    # distinct digits in the array 
    for i in range(10): 
        if (arr[i] != 0): 
            count += 1; 
      
    return count; 
  
# Function to return the total number 
# of digits in the number 
def countDigit(n): 
    c = 0; 
  
    # Iterate over the digits of the number 
    while (n != 0): 
        r = n % 10; 
        c+=1; 
        n //= 10; 
      
    return c; 
  
# Function to return the next 
# number with distinct digits 
def nextNumberDistinctDigit(n): 
    while (n < INT_MAX): 
  
        # Count the distinct digits in N + 1 
        distinct_digits = countDistinct(n + 1); 
  
        # Count the total number of digits in N + 1 
        total_digits = countDigit(n + 1); 
  
        if (distinct_digits == total_digits): 
  
            # Return the next consecutive number 
            return n + 1; 
        else: 
  
            # Increment Number by 1 
            n += 1; 
      
    return -1; 
  

def checkRunRound(numArr):
    global lenNumArr
    currIdx = 0
    boolNumArr = [False] * lenNumArr
    for i in range(lenNumArr):
        if boolNumArr[(currIdx + numArr[currIdx]) % lenNumArr] == True:
            return False
        else:
            boolNumArr[(currIdx + numArr[currIdx]) % lenNumArr] = True
        currIdx = (currIdx + numArr[currIdx]) % lenNumArr
        if i == lenNumArr - 1:
            if currIdx == 0:
                return True

    return False


def checkDiffNum(numArr):
    global lenNumArr
    boolArr = [False] * 10
    for i in range(lenNumArr):
        if numArr[i] == lenNumArr:
            return False
        if numArr[i]==0:
          return False
        if boolArr[numArr[i]] == True:
            #print(numArr[i])
            return False
        else:
            boolArr[numArr[i]] = True
    return True


currNum = int(inpFile.readline()) + 1

while True:
    numArr = [int(d) for d in str(currNum)]
    lenNumArr = len(numArr)
    if checkDiffNum(numArr):
        if checkRunRound(numArr):
            break
    currNum =nextNumberDistinctDigit(currNum)

outFile.write(str(currNum) + "\n")
outFile.close()

