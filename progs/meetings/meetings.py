"""
ID: neelkolhe
TASK: meetings
"""


inpFile=open('meetings.in','r')
outFile=open('meetings.out','w')

arr=inpFile.readline().split()
numberCows=int(arr[0])

barn=int(arr[1])

cowArray=[]
totalWeight=0
posCows=[]
negCows=[]
locations=[]
for i in range(numberCows):
  x=inpFile.readline().split()
  x[0]=int(x[0])
  x[1]=int(x[1])
  x[2]=int(x[2])
  cowArray.append(x)
  totalWeight+=x[0]
  locations.append([x[1],x[2],x[0]])

times=[]
for i in range(numberCows):
  if locations[i][1]==1:
    times.append([barn-locations[i][0],1,locations[i][2]])
  else:
    times.append([locations[i][0],-1,locations[i][2]])

times.sort()
currWeight=0
print(totalWeight)
print(times)

for i in range(numberCows):
  currWeight+=locations[i][2]
  if currWeight>=(totalWeight/2):
    timeNeeded=times[i][0]
    break

print(timeNeeded)

posLocations=[]
negLocations=[]

for i in range(numberCows):
  if locations[i][1]>0:
    posLocations.append(locations[i][0])
  else:
    negLocations.append(locations[i][0])

numberMeetings=0
for i in range(len(posLocations)):
  for j in range (len(negLocations)):
    print(posLocations[i])
    print(negLocations[j])
    if negLocations[j]>posLocations[i]:
      if negLocations[i]-posLocations[i]<=(2*timeNeeded):
        numberMeetings+=1

outFile.write(str(numberMeetings)+"\n")
outFile.close()
