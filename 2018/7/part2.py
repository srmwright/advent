import re
import numpy as np
import string
import collections

## Input
with open('test1.txt') as f:
    input = f.read()

lines = input.strip().split('\n')

pairs = list([])

for i in range(0,len(lines)):
	pairs.append(re.findall(r"p ([A-Z]*)",lines[i]))

alpha_dict = {}

hold_time = 0
alpha_list = list(string.ascii_uppercase)[0:6]
# hold_time = 60
# alpha_list = list(string.ascii_uppercase)
times = list(range(hold_time,hold_time + len(alpha_list)))

for letter in alpha_list:
	alpha_dict[letter] = []

for i in range(0,len(lines)):
 	alpha_dict[pairs[i][1]].append(pairs[i][0])

print(alpha_dict)

n = len(alpha_list)
n_workers = 2
worker_letter = ['']*n_workers
worker_timeleft = [0]*n_workers

time = 0
while n > 0:
	a = len(still_left)
	i = 0
	while i < a:
		letter = still_left[i]
		#print(letter)
		i = i + 1
		if len(alpha_dict[letter]) == 0:
			for k in range(0,len(worker_letter)):
				if(worker_letter==''):
					worker_letter[k] = letter
					worker_timeleft[k] = times[i]
				if worker_timeleft[k] == 0:
			alpha_dict.pop(letter)
			still_left.remove(letter)
			ansString += letter
			print(letter)
			print(ansString)
			n = n - 1
			for letter2 in still_left:
				if letter in alpha_dict[letter2]:
					alpha_dict[letter2].remove(letter)
			a = a - 1
			i = 0 

# class myLetter:

# 	def __init__(self, letter):
# 		self.letter = letter
# 		self.before = list([])
# 		self.after = list([])

# 	def prereq(self, next_letter):
# 		self.before.append(next_letter)

# 	def depends_on(self, last_letter):
# 		self.after.append(last_letter)

# ansString = ''
# still_left = alpha_list
# while n > 0:
# 	a = len(still_left)
# 	i = 0
# 	while i < a:
# 		letter = still_left[i]
# 		#print(letter)
# 		i = i + 1
# 		if len(alpha_dict[letter]) == 0:
# 			alpha_dict.pop(letter)
# 			still_left.remove(letter)
# 			ansString += letter
# 			print(letter)
# 			print(ansString)
# 			n = n - 1
# 			for letter2 in still_left:
# 				if letter in alpha_dict[letter2]:
# 					alpha_dict[letter2].remove(letter)
# 			a = a - 1
# 			i = 0
# 		#IBJTUWGFKDNVEYHQAOMPCRLSZX

# print(ansString)