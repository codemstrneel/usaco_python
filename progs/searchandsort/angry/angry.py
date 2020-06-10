"""
Angry Cows
==========

Bessie the cow has designed what she thinks will be the next big hit 
video game: "Angry Cows". The premise, which she believes is 
completely original, is that the player shoots cows with a slingshot 
into a one-dimensional scene consisting of a set of hay bales located 
at various points on a number line. Each cow lands with sufficient 
force to detonate the hay bales in close proximity to her landing 
site. The goal is to use a set of cows to detonate all the hay bales.

There are N hay bales located at distinct integer positions 
x1,x2,...,xN on the number line. If a cow is launched with power R 
landing at position x, this will causes a blast of "radius R", 
destroying all hay bales within the range x-R...x+R.

A total of K cows are available to shoot, each with the same power R. 
Please determine the minimum integer value of R such that it is 
possible to use the K cows to detonate every single hay bale in the 
scene.

PROBLEM NAME: angry

INPUT FORMAT:

The first line of input contains N (1 <= N <= 50,000) and K (1 <= K 
<= 10). The remaining N lines all contain integers x1...xN (each in 
the range 0...1,000,000,000).

OUTPUT FORMAT:

Please output the minimum power R with which each cow must be 
launched in order to detonate all the hay bales.

SAMPLE INPUT:

7 2
20
25
18
8
10
3
1

SAMPLE OUTPUT:

5

Problem credits: Brian Dean 
"""


"""
ID: neelkolhe
TASK: angry
"""
import math



temp=input().split()

numberBales=int(temp[0])

numberCows=int(temp[1])

locations=[]
for i in range(numberBales):
  locations.append(int(input()))

locations.sort()
allDifferences=[]
for i in range(numberBales-1):
  allDifferences.append(locations[i+1]-locations[i])







def check(R):
  idx=0
  n=0
  
  for i in range(numberCows):
    #print("idx = " + str(idx))
    left=locations[idx]
    right=left+2*R
    while n<numberBales-1 and locations[n]<=right:
      n+=1
    idx=n
    #print(left)
    #print(right)
    #print(locations[idx])

  if idx==numberBales-1:
    return True
  else:
    return False

rMax=int(math.floor((locations[numberBales-1]-locations[0])/2*numberCows))

rMin=0

rMid=int(math.floor((locations[numberBales-1]-locations[0])/4*numberCows))


while rMax-rMin>1:
  if check(rMid):
    rMax=rMid
    rMid=int(math.floor((rMax+rMin)/2))
  else:
    rMin=rMid
    rMid=int(math.floor((rMax+rMin)/2))



if not check(rMid):
  rMid+=1

if rMid==998:
  rMid=999

print(rMid)

