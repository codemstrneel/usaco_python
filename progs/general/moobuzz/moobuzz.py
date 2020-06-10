"""
Farmer John's cows have recently become fans of playing a simple number game called "FizzBuzz". The rules of the game are simple: standing in a circle, the cows sequentially count upward from one, each cow saying a single number when it is her turn. If a cow ever reaches a multiple of 3, however, she should say "Fizz" instead of that number. If a cow reaches a multiple of 5, she should say "Buzz" instead of that number. If a cow reaches a multiple of 15, she should say "FizzBuzz" instead of that number. A transcript of the first part of a game is therefore:
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16

Having a slightly more limited vocabulary, the version of FizzBuzz played by the cows involves saying "Moo" instead of Fizz, Buzz, and FizzBuzz. The beginning of the cow version of the game is therefore

1, 2, Moo, 4, Moo, Moo, 7, 8, Moo, Moo, 11, Moo, 13, 14, Moo, 16

Given N (1≤N≤109), please determine the Nth number spoken in this game.

SCORING
Test cases 2-5 satisfy N≤106.
INPUT FORMAT (file moobuzz.in):
The input consists of a single integer, N.
OUTPUT FORMAT (file moobuzz.out):
Please print out the Nth number spoken during the game.
SAMPLE INPUT:
4
SAMPLE OUTPUT:
7
The 4th number spoken is 7. The first 4 numbers spoken are 1, 2, 4, 7, since we skip over any time a cow says "Moo".

Problem credits: Brian Dean
"""
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
  
