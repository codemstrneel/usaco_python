"""
Bessie the cow, always a fan of shiny objects, has taken up a hobby of mining diamonds in her spare time! She has collected N diamonds (N≤50,000) of varying sizes, and she wants to arrange some of them in a pair of display cases in the barn.
Since Bessie wants the diamonds in each of the two cases to be relatively similar in size, she decides that she will not include two diamonds in the same case if their sizes differ by more than K (two diamonds can be displayed together in the same case if their sizes differ by exactly K). Given K, please help Bessie determine the maximum number of diamonds she can display in both cases together.

INPUT FORMAT (file diamond.in):
The first line of the input file contains N and K (0≤K≤1,000,000,000). The next N lines each contain an integer giving the size of one of the diamonds. All sizes will be positive and will not exceed 1,000,000,000.
OUTPUT FORMAT (file diamond.out):
Output a single positive integer, telling the maximum number of diamonds that Bessie can showcase in total in both the cases.
SAMPLE INPUT:
7 3
10
5
1
12
9
5
14
SAMPLE OUTPUT:
5
"""
import copy 
import bisect
temp=input().split()

N=int(temp[0])
K=int(temp[1])
arr=[]
for i in range(N):
  arr.append(int(input()))
#print(arr)
arr.sort()
maxNum=0


#print(arr)
claw1=0
ranges1=[0,0]
for i in range(N):

  LHS=i
  RHS=bisect.bisect(arr,arr[i]+K,lo=i,hi=N)
  if RHS-LHS>claw1:
    claw1=RHS-LHS
    ranges1=[LHS,RHS]
#print(claw1)
#print(ranges1)

for i in range(ranges1[1]-1,ranges1[0]-1,-1):
  del arr[i]
#print(arr)

claw2=0
ranges2=[0,0]
N=len(arr)
for i in range(N):
  LHS=i
  RHS=bisect.bisect(arr,arr[i]+K,lo=i,hi=N)
  if RHS-LHS>claw2:
    claw2=RHS-LHS

maxNum=claw1+claw2
print(maxNum)

