"""
The Leprechaun
==============

Imagine Bessie's surprise as she spied a leprechaun prancing through
the north pasture. Being no one's fool, she charged at the leprechaun
at captured him with her prehensile hooves.

"One wish, bovine one. That's all I have for cows," he said.

"Riches," Bessie said dreamily. "The opportunity for riches."

Leprechauns never grant precisely the easiest form of their captor's
wishes. As the smoke cleared from the location of a loud explosion,
a shimmering donut spun slowly over the verdant green fields.

"I have made you a torus," the leprechaun cooed. "And on that torus
is an N x N matrix (1 <= N <= 200) of integers in the range
-1,000,000..1,000,000 that will determine the magnitude of your
riches. You must find the sequence of contiguous integers all in
one row, one column, or on one diagonal that yields the largest sum
from among all the possible sequences on the torus."

Bessie pondered for a moment and realized that the torus was a
device for "wrapping" the columns, rows, and diagonals of a matrix
so that one could choose contiguous elements that "wrapped around"
the side or top edge.

Bessie will share the matrix with you.  Determine the value of the
largest possible sum (which requires choosing at least one matrix
element).

By way of example, consider the 4 x 4 matrix on the left below that
has all the elements from one exemplary "wrapped" diagonal marked:

           8  6  6* 1           8  6* 6  1
          -3  4  0  5*         -3  4  0  5
           4* 2  1  9           4  2  1  9*
           1 -9* 9 -2           1 -9  9*-2

The marked diagonal of the right-hand matrix includes two nines
(the highest available number) and a six for a total of 24. This
is the best possible sum for this matrix and includes only three
of the four possible elements on its diagonal.

PROBLEM NAME: lepr

INPUT FORMAT:

* Line 1: A single integer: N

* Lines 2..N+1: Line i+1 contains N space-separated integers that
        compose row i of the matrix

SAMPLE INPUT:

4
8 6 6 1
-3 4 0 5
4 2 1 9
1 -9 9 -2

OUTPUT FORMAT:

* Line 1: A single integer that is the largest possible sum computable
        using the rules above

SAMPLE OUTPUT:

24
"""


numberLines=int(input())
allRows=[]
for i in range(numberLines):
  allRows.append(input().split())
  for j in range(numberLines):
    allRows[i][j]=int(allRows[i][j])

#print(allRows)

allRowArr=[]
for i in range(numberLines):
  currRowArr=[]
  for j in range(numberLines):
    startingPoint=j
    currArr=[]
    for k in range(numberLines):
      newPoint=(j+k)%numberLines
      if k==0:
        currArr.append(allRows[i][newPoint])
      else:
        currArr.append(allRows[i][newPoint]+currArr[k-1])
    currRowArr.append(max(currArr))
  allRowArr.append(max(currRowArr))
#print(allRowArr)    

allColArr=[]
for i in range(numberLines):
  currRowArr=[]
  for j in range(numberLines):
    startingPoint=j
    currArr=[]
    for k in range(numberLines):
      newPoint=(j+k)%numberLines
      if k==0:
        currArr.append(allRows[newPoint][i])
      else:
        currArr.append(allRows[newPoint][i]+currArr[k-1])
    currRowArr.append(max(currArr))
  allColArr.append(max(currRowArr))

#print(allColArr)

allDiagArr=[]
for i in range(numberLines):
  currRowArr=[]
  for j in range(numberLines):
    startingPoint=j
    currArr=[]
    for k in range(numberLines):
      newPoint=(j+k)%numberLines
      if k==0:
        currArr.append(allRows[(i+k)%numberLines][(j+k)%numberLines])
      else:
        currArr.append(allRows[(i+k)%numberLines][(j+k)%numberLines]+currArr[k-1])
    currRowArr.append(max(currArr))
  allDiagArr.append(max(currRowArr))

#print(allDiagArr)

newDiagArr=[]
for i in range(numberLines):
  currRowArr=[]
  for j in range(numberLines):
    startingPoint=j
    currArr=[]
    for k in range(numberLines):
      newPoint=(j+k)%numberLines
      if k==0:
        currArr.append(allRows[(i-k)%numberLines][(j+k)%numberLines])
      else:
        currArr.append(allRows[(i-k)%numberLines][(j+k)%numberLines]+currArr[k-1])
    currRowArr.append(max(currArr))
  newDiagArr.append(max(currRowArr))

#print(newDiagArr)

x1=max(allRowArr)
x2=max(allColArr)
x3=max(allDiagArr)
x4=max(newDiagArr)

print(max(x1,x2,x3,x4))
