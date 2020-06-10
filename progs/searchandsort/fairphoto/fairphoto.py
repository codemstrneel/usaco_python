"""
Problem 2: Fair Photography [Brian Dean, 2014]

Farmer John's N cows (1 <= N <= 100,000) are standing at various positions along 
a long one-dimensional fence.  The ith cow is standing at position x_i (an
integer in the range 0...1,000,000,000) and has breed b_i (either 'G' for
Guernsey or 'H' for Holstein).  No two cows occupy the same position.

FJ wants to take a photo of a contiguous interval of cows for the county
fair, but we wants all of his breeds to be fairly represented in the photo.
Therefore, he wants to ensure that, for whatever breeds are present in the
photo, there is an equal number of each breed (for example, a photo with
all Holsteins is ok, a photo with 27 Holsteins and 27 Guernseys is ok, but a
photo with 10 Holsteins and 9 Guernseys is not ok).  Help FJ take his fair
photo by finding the maximum size of a photo that satisfies FJ's
constraints.  The size of a photo is the difference between the maximum and
minimum positions of the cows in the photo.  It is possible that FJ could
end up taking a photo of just a single cow, in which case this photo would
have size zero.

PROBLEM NAME: fairphoto

INPUT FORMAT:

* Line 1: The integer N.

* Lines 2..1+N: Line i+1 contains x_i and b_i.

SAMPLE INPUT (file fairphoto.in):

6
4 G
10 H
7 G
16 G
1 G
3 H

INPUT DETAILS:

There are six cows with breeds (from left to right) G, H, G, G, H, G.  

OUTPUT FORMAT:

* Line 1: A single integer indicating the maximum size of a fair
        photo.

SAMPLE OUTPUT (file fairphoto.out):

7

OUTPUT DETAILS:

The largest fair photo Farmer John can take is of the middle 4 cows,
containing 2 Holsteins and 2 Guernseys.  
"""


numberCows=int(input())

arr=[]

for i in range(numberCows):
  temp=input().split()
  arr.append([int(temp[0])-1,temp[1]])

arr.sort()

allNums=[[0,0]]

#print(arr[numberCows-1])
for i in range(numberCows):
  if arr[i][1]=="H":

    allNums.append([allNums[i][0]+1,arr[i][0]])
    #print(i)
  else:
    allNums.append([allNums[i][0]-1,arr[i][0]])

del(allNums[0])

for i in range(numberCows):
  allNums[i][0]+=numberCows
#print(allNums)

allSums=[]
maxAllSums=[]
for i in range(2*numberCows+1):
  allSums.append(1000000000000)
  maxAllSums.append(0)

for i in range(numberCows):
  if i<numberCows-1 and allNums[i+1][1]<allSums[allNums[i][0]]:
    allSums[allNums[i][0]]=allNums[i+1][1]
  if allNums[i][1]>maxAllSums[allNums[i][0]]:
    maxAllSums[allNums[i][0]]=allNums[i][1]
#print(allSums)
#print(maxAllSums)

maximum=0
for i in range(len(allSums)):
  if maxAllSums[i]-allSums[i]>maximum:
    maximum=maxAllSums[i]-allSums[i]

currLetter=arr[0][1]
currStart=arr[0][0]
currEnd=arr[0][0]
for i in range(numberCows):
  if arr[i][1]==currLetter:
    currEnd=arr[i][0]
  else:
    if currEnd-currStart>maximum:
      maximum=currEnd-currStart
    currLetter=arr[i][1]
    currStart=arr[i][0]
    currEnd=arr[i][0]

  
print(maximum)
