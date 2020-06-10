"""
Problem 4: Learning by Example [Brian Dean, 2014]

Farmer John has been reading all about the exciting field of machine
learning, where one can learn interesting and sometimes unexpected
patterns by analyzing large data (he has even started calling one of
the fields on his farm the "field of machine learning"!).  FJ decides
to use data about his existing cow herd to build an automatic
classifier that can guess whether a cow will have spots or not.

Unfortunately, FJ hasn't been very good at keeping track of data about
his cows.  For each of his N cows (1 <= N <= 50,000), all he knows is
the weight of the cow, and whether the cow has spots.  Each of his
cows has a distinct weight.  Given this data, he builds what is called
a "nearest neighbor classifier".  To guess whether a new cow C will
have spots or not, FJ first finds the cow C' in his herd with weight
closest to that of C.  If C' has spots, then FJ guesses that C will
also have spots; if C' has no spots, FJ guesses the same for C.  If
there is not one unique nearest neighbor C' but rather a tie between
two of FJ's cows, then FJ guesses that C will have spots if one or
both these nearest neighbors has spots.

FJ wants to test his new automatic spot predictor on a group of new
cows that are just arriving at his farm.  After weighing these cows,
he sees that the new shipment of cows contains a cow of every integer
weight between A and B (inclusive).  Please determine how many of
these cows will be classified as having spots, using FJ's new
classifier.  Note that the classifier only makes decisions using data
from FJ's N existing cows, not any of the new cows.  Also note that
since A and B can both be quite large, your program will not likely
run fast enough if it loops from A to B counting by ones.

INPUT: (file learning.in) 

The first line of the input contains three integers N, A, and B
(1 <= A <= B <= 1,000,000,000).

The next N lines each describe a single cow.  Each line contains
either S W, indicating a spotted cow of weight W, or NS W, indicating
a non-spotted cow of weight W.  Weights are all integers in the range
1 ... 1,000,000,000. 

SAMPLE INPUT:

3 1 10
S 10
NS 4
S 1

OUTPUT: (file learning.out)

A single integer giving the number of incoming cows that FJ's
algorithm will classify as having spots.  In the example shown
here, the incoming cows of weights 1, 2, 7, 8, 9, and 10 
will all be classified as having spots.

SAMPLE OUTPUT:

6
"""

temp=input().split()

numberLines=int(temp[0])

leftSide=int(temp[1])

rightSide=int(temp[2])

allKnown=[]

for i in range(numberLines):
  temp=input().split()
  currArr=[int(temp[1])]
  if temp[0]=="S":
    currArr.append(1)
  else:
    currArr.append(0)
  allKnown.append(currArr)
#print(allKnown)
allKnown.sort()
#print(allKnown)
answer=0
for i in range(numberLines-1):
  LHS=allKnown[i][0]
  RHS=allKnown[i+1][0]
  middle=int((LHS+RHS)/2)
  if allKnown[i][1]==1:
    a=max(leftSide,LHS+1)
    b=min(rightSide,middle)
    if b>=a:
      answer+=(b-a+1)
  if allKnown[i+1][1]==1:
    a=max(leftSide,middle+1)
    b=min(rightSide,RHS)
    if b>=a:
      answer+=(b-a+1)
  if allKnown[i+1][1]==1 and allKnown[i][1]==0 and (LHS%2==RHS%2) and leftSide<=middle and middle<=rightSide:
    #print(i)
    answer+=1
#print(answer)
if allKnown[0][1]==1 and allKnown[0][0]>=leftSide:
  answer+=(allKnown[0][0]-leftSide+1)
  #print(allKnown[0][0])
  #print(leftSide)
if allKnown[numberLines-1][1]==1 and allKnown[numberLines-1][0]<rightSide:
  answer+=(rightSide-allKnown[numberLines-1][0]+1)
  #print(rightSide)
  #print(allKnown[numberLines-1])
 
print(answer)
