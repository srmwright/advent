import time
from datetime import datetime
import re
import numpy as np
import pandas as pd
import string

## Input
with open('input.txt') as f:
    input = f.read()

lines = input.strip().split('\n')

## Is this a reacting pair?
def isPair(a,b):
	if (a == b.lower() and b == a.upper()) or (b == a.lower() and a == b.upper()):
		return True
	else:
		return False

#print(isPair('a','A'))
#print(isPair('a','a'))

#Input string and counters
myString = lines[0]
i = 0
b = len(myString)

# React the string
while i < b-1:
	if isPair(myString[i],myString[i+1]): #if pair
		myString = myString[:i] + myString[(i+2):] #remove characters
		i = i - 1 #move index back to check
		b = b - 2 #adjust for new length of string
	else:
		i = i + 1 #else move forward
	if i < 0: #don't get stuck at index -1!
		i = 0
	#print(myString)
	# if i%100 == 0 or b%100 == 0:
	# 	print(i,b)
print(len(myString)) #answer