import re
import numpy as np
import string
import collections

## Input
with open('test1.txt') as f:
    input = f.read()

lines = input.strip().split(' ')
tree = [int(x) for x in lines]
tree_types = ['']*len(tree)

#Keep a track of the number of children and metadata in a list
nchildren = [tree[0]]
nmeta = [tree[1]]

#Create an array to store every metadata entry
meta = []

print(len(tree))

current_index = 0
i = 2
#try a solution keeping the state of what's being passed
while i < len(tree):
	current_index += 1 #increment current_index
	nchildren.append(tree[i]) #append number of children of current child to node
	print(tree[i],i)
	i += 1
	nmeta.append(tree[i]) # append amount of metadata to tree
	print(tree[i], i)
	i += 1
	if nchildren[current_index] == 0:
		n_to_read = nmeta[current_index]
		for j in range(0, n_to_read):
			meta.append(tree[i])
			print(tree[i], i, 'ans')
			i = i + 1
		current_index = current_index - 1
		nchildren[current_index] -= 1

print(meta)

