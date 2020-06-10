"""
Problem 7: The Grand Farm-off [Haitao Mao, 2009]

Farmer John owns 3*N (1 <= N <= 500,000) cows surprisingly numbered
0..3*N-1, each of which has some associated integer weight W_i (1 <=
W_i <= d). He is entering the Grand Farm-off, a farming competition
where he shows off his cows to the greater agricultural community.

This competition allows him to enter a group of N cows. He has given
each of his cows a utility rating U_i (1 <= U_i <= h), which
represents the usefulness he thinks that a particular cow will have
in the competition, and he wants his selection of cows to have the
maximal sum of utility.

There might be multiple sets of N cows that attain the maximum
utility sum. FJ is afraid the competition may impose a total weight
limit on the cows in the competition, so a secondary priority is
to bring lighter weight competition cows.

Help FJ find a set of N cows with minimum possible total weight
among the sets of N cows that maximize the utility, and print the
remainder when this total weight is divided by M (10,000,000 <= M
<= 1,000,000,000).

Note: to make the input phase faster, FJ has derived polynomials
which will generate the weights and utility values for each cow.
For each cow 0 <= i < 3*N,

       W_i = (a*i^5+b*i^2+c) mod d
 and   U_i = (e*i^5+f*i^3+g) mod h

with reasonable ranges for the coefficients (0 <= a <= 1,000,000,000;
0 <= b <= 1,000,000,000; 0 <= c <= 1,000,000,000; 0 <= e <=
1,000,000,000; 0 <= f <= 1,000,000,000; 0 <= g <= 1,000,000,000;
10,000,000 <= d <= 1,000,000,000; 10,000,000 <= h <= 1,000,000,000).

The formulae do sometimes generate duplicate numbers; your algorithm
should handle this properly.

PROBLEM NAME: farmoff

INPUT FORMAT:

* Line 1: Ten space-separated integers: N, a, b, c, d, e, f, g, h, and
        M

SAMPLE INPUT (file farmoff.in):

2 0 1 5 55555555 0 1 0 55555555 55555555

INPUT DETAILS:

The functions generate weights of 5, 6, 9, 14, 21, and 30 along
with utilities of 0, 1, 8, 27, 64, and 125.

OUTPUT FORMAT:

* Line 1: A single integer representing the lowest sum of the weights
        of the N cows with the highest net utility.

SAMPLE OUTPUT (file farmoff.out):

51

OUTPUT DETAILS:

The two cows with the highest utility are cow 5 and 6, and their combined
weight is 21+30=51.
"""


x=input().split()

N=int(x[0])

a=int(x[1])
b=int(x[2])
c=int(x[3])
d=int(x[4])
e=int(x[5])
f=int(x[6])
g=int(x[7])
h=int(x[8])
M=int(x[9])
allArr=[]
for i in range(3*N):
  weightNumber=(((a%d)*(i**5))+((b%d)*(i**2))+c)%d
  utilNum=(e*(i**5)+f*(i**3)+g)% h
  allArr.append([utilNum,weightNumber])

allArr.sort(reverse=True)

allNumbers=[]
i=0
while i<3*N:
  currNum=allArr[i][0]
  currArr=[]
  while i<3*N and allArr[i][0]==currNum:
    currArr.append(allArr[i])
    i+=1
  allNumbers.append(currArr)

#print(allNumbers)
for i in range(len(allNumbers)):
  x=allNumbers[i]
  currArr=[]
  
  for j in range(len(x)-1,-1,-1):

    currArr.append(x[j])

  allNumbers[i]=currArr
i=0
x=0
totalWeight=0
prevNum=0
while i<N:
  prevNum=i
  currIdx=0
  currArr=allNumbers[x]

  while i<N and i<len(allNumbers[x])+prevNum:
    totalWeight+=allNumbers[x][currIdx][1]
    i+=1
    currIdx+=1
  
  x+=1

print(totalWeight%M)




