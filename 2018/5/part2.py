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

#Input string
myString = lines[0]

# Use part A solution as reacting function
def react(myString):
	i = 0
	b = len(myString)
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
		#if i%100 == 0 or b%100 == 0:
			#print(i,b)
	return (len(myString))

#Loop to find the shortest resulting polymer
shortest_polymer = len(myString)
for letter in list(string.ascii_lowercase):
#for letter in ['a','b','c','d']:
	input_str = myString.replace(letter.lower(),'')
	input_str = input_str.replace(letter.upper(),'')
	#print(input_str)
	a = react(input_str)
	print(letter, a, shortest_polymer)
	if a < shortest_polymer:
		shortest_polymer = a

print(shortest_polymer) #answer