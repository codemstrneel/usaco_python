"""
Farmer John has just arranged his N haybales (1≤N≤100,000) at various points along the one-dimensional road running across his farm. To make sure they are spaced out appropriately, please help him answer Q queries (1≤Q≤100,000), each asking for the number of haybales within a specific interval along the road.
INPUT FORMAT (file haybales.in):
The first line contains N and Q.
The next line contains N distinct integers, each in the range 0…1,000,000,000, indicating that there is a haybale at each of those locations.

Each of the next Q lines contains two integers A and B (0≤A≤B≤1,000,000,000) giving a query for the number of haybales between A and B, inclusive.

OUTPUT FORMAT (file haybales.out):
You should write Q lines of output. For each query, output the number of haybales in its respective interval.
SAMPLE INPUT:
4 6
3 2 7 5
2 3
2 4
2 5
2 7
4 6
8 10
SAMPLE OUTPUT:
2
2
3
4
1
0
Problem credits: Nick Wu
"""

"""
ID: neelkolhe
TASK: haybales
"""


def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l) // 2
  
        # If element is present at the middle itself 
        if arr[mid] <= x and mid+1<len(arr) and arr[mid+1]>x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        elif mid==len(arr)-1:
          return mid
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1


inpFile=open('haybales.in','r')
outFile=open('haybales.out','w')

temp=inpFile.readline().split()

numberBales=int(temp[0])

numberLines=int(temp[1])

locations=inpFile.readline().split()

for i in range(numberBales):
  locations[i]=int(locations[i])

locations.sort()

#print(locations)

queries=[]
for i in range(numberLines):
  tempArr=inpFile.readline().split()
  for j in range(2):
    tempArr[j]=int(tempArr[j])
  queries.append(tempArr)

#print(queries)
answers=[]
for i in  range(numberLines):
  answers.append(binarySearch(locations,0,numberBales-1,queries[i][1])-binarySearch(locations,0,numberBales-1,queries[i][0]-1))

print(answers)

