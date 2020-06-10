"""
A certain book’s prefaces are numbered in upper case Roman numerals. Traditional Roman numeral values use a single letter to represent a certain subset of decimal numbers. Here is the standard set:

I   1
V   5
X  10
L   50
C  100
D  500
M  1000
Copy
As many as three of the same marks that represent 10n may be placed consecutively to form other numbers:

III is 3
CCC is 300
Marks that have the value 5x10n are never used consecutively.

Generally (with the exception of the next rule), marks are connected together and written in descending order to form even more numbers:

CCLXVIII = 100+100+50+10+5+1+1+1 = 268
Sometimes, a mark that represents 10^n is placed before a mark of one of the two next higher values (I before V or X; X before L or C; etc.). In this case, the value of the smaller mark is SUBTRACTED from the mark it precedes:

IV = 4
IX = 9
XL = 40
This compound mark forms a unit and may not be combined to make another compound mark (e.g., IXL is wrong for 39; XXXIX is correct).

Compound marks like XD, IC, and XM are not legal, since the smaller mark is too much smaller than the larger one. For XD (wrong for 490), one would use CDXC; for IC (wrong for 99), one would use XCIX; for XM (wrong for 990), one would use CMXC. 90 is expressed XC and not LXL, since L followed by X connotes that successive marks are X or smaller (probably, anyway).

Given N (1 <= N < 3,500), the number of pages in the preface of a book, calculate and print the number of I’s, V’s, etc. (in order from lowest to highest) required to typeset all the page numbers (in Roman numerals) from 1 through N. Do not print letters that do not appear in the page numbers specified.

If N = 5, then the page numbers are: I, II, III, IV, V. The total number of I’s is 7 and the total number of V’s is 2.

PROGRAM NAME: preface
INPUT FORMAT
A single line containing the integer N.

SAMPLE INPUT (file preface.in)
5
Copy
OUTPUT FORMAT
The output lines specify, in ascending order of Roman numeral letters, the letter, a single space, and the number of times that letter appears on preface page numbers. Stop printing letter totals after printing the highest value letter used to form preface numbers in the specified set.
"""


"""
ID: neel1
LANG: PYTHON3
TASK: preface
"""
import copy
inpFile = open('preface.in', 'r')
outFile = open('preface.out', 'w')
def convert(num):
  val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
  ]
  syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
         ]
  roman_num = ''
  i = 0
  while  num > 0:
            for j in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
  return roman_num

maxNum=int(inpFile.readline())

totalIs=[0]*3501

totalVs=[0]*3501

totalXs=[0]*3501

totalLs=[0]*3501

totalCs=[0]*3501

totalDs=[0]*3501

totalMs=[0]*3501

for i in range(1,3501):
  totalIs[i]=copy.copy(totalIs[i-1])

  totalVs[i]=totalVs[i-1]
  totalXs[i]=totalXs[i-1]
  totalLs[i]=totalLs[i-1]
  totalCs[i]=totalCs[i-1]
  totalDs[i]=totalDs[i-1]
  totalMs[i]=totalMs[i-1]

  currNum=convert(i)
  numArr=list(currNum)
  
  for j in range(len(numArr)):
    if numArr[j]=="I":
      totalIs[i]+=1
    elif numArr[j]=="V":
      totalVs[i]+=1
    elif numArr[j]=="X":
      totalXs[i]+=1
    elif numArr[j]=="L":
      totalLs[i]+=1
    elif numArr[j]=="C":
      totalCs[i]+=1
    elif numArr[j]=="D":
      totalDs[i]+=1
    elif numArr[j]=="M":
      totalMs[i]+=1

if totalIs[maxNum]>0:
  outFile.write("I " + str(totalIs[maxNum])+"\n")
if totalVs[maxNum]>0:
  outFile.write("V " + str(totalVs[maxNum])+"\n")
if totalXs[maxNum]>0:
  outFile.write("X " + str(totalXs[maxNum])+"\n")
if totalLs[maxNum]>0:
  outFile.write("L " + str(totalLs[maxNum])+"\n")
if totalCs[maxNum]>0:
  outFile.write("C " + str(totalCs[maxNum])+"\n")
if totalDs[maxNum]>0:
  outFile.write("D " + str(totalDs[maxNum])+"\n")
if totalMs[maxNum]>0:
  outFile.write("M " + str(totalMs[maxNum])+"\n")
outFile.close()
