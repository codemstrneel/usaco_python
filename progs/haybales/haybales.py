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

