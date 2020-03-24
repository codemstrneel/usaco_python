"""
ID: neelkolhe
TASK: moobuzz
"""


import math

inpFile=open('moobuzz.in','r')
outFile=open('moobuzz.out','w')


numberSaid=int(inpFile.readline())



multiple=(15*numberSaid)/8

if numberSaid%8!=0:
  mult15sless=math.floor(multiple/15)
  mult15sless=mult15sless*15

  mult15smore=math.ceil(multiple/15)
  mult15smore=mult15smore*15
  answer=0
  for i in range(mult15sless+1,mult15smore):
    x=i
    x=x-math.floor(i/3.0)
    x=x-math.floor(i/5.0)
    x=x+math.floor(i/15.0)
    if x==numberSaid:
      answer=i
      break

  outFile.write(str(answer)+"\n")
  outFile.close()
else:
  mult15sless=multiple/15-1
  mult15smore=multiple/15
  mult15sless=15*mult15sless
  mult15smore=mult15smore*15
  mult15sless=int(mult15sless)
  mult15smore=int(mult15smore)
  for i in range(mult15sless+1,mult15smore):
    x=i
    x=x-math.floor(i/3.0)
    x=x-math.floor(i/5.0)
    x=x+math.floor(i/15.0)
    if x==numberSaid:
      answer=i
      break

  outFile.write(str(answer)+"\n")
  outFile.close()
  
