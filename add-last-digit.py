#!/usr/bin/python

print("ENTER TWO NUMBERS TO ADD LAST TWO DIGITS")
print("----------------------------------------")
print("ENTER FIRST NUMBER")
a=int(input()) #1stnumber 
print("ENTER SECOND NUMBER")
b=int(input()) #2ndnumber 
c = a%10
d = b%10
print("ANSWER IS")
print(c+d)
