import time
from datetime import datetime
import re
import numpy as np
import string
import collections

## Input
with open('input.txt') as f:
    input = f.read()

lines = input.strip().split('\n')

x_coords = list([])
y_coords = list([])
coords = list([])

for i in range(0, len(lines)):
	x_coords.append(int(lines[i].strip().split(', ')[0]))
	y_coords.append(int(lines[i].strip().split(', ')[1]))
	coords.append(list([x_coords[i],y_coords[i]]))

#Size of grid with extension at plus end
## NB - probably should only set extension to size/2 (I think that's adequate)
start_of_grid = list([min(x_coords),min(y_coords)])
size_of_grid = list([max(x_coords)+200,max(y_coords)+200])

#Taxicab function
def taxicab(c0, c1):
	return abs(c1[1] - c0[1]) + abs(c1[0] - c0[0])

#print(taxicab(coords[2],coords[0]))

## For each point on grid, calculate distance to every node
## Store index of closest node, taxicab distance
## If a tie, set closest node to -1

# Define matrices for distances and indices
the_grid_taxi = np.zeros(size_of_grid)
the_grid_index = np.zeros(size_of_grid)

# Get set of nodes at the edge (infinite areas)
infinite_nodes = set()

#Populate the matrices
for i in range(0,size_of_grid[0]):
	for j in range(0, size_of_grid[1]):
		min_node = -1
		min_distance = 10000000000
		for k in range(0,len(coords)):
			distance = taxicab(coords[k],list([j,i]))
			the_grid_taxi[i,j] = distance
			if distance == min_distance: #if tie, set to -1
				min_node = -1
			elif distance < min_distance: #else set to new closest
				min_node = k
				min_distance = distance
		the_grid_index[i,j] = min_node
		#if on edge, add to infinite node list
		if (i==0 or j==0 or i==size_of_grid[0]-1 or j==size_of_grid[1]-1):
			infinite_nodes.add(min_node)

#Flatten and count the nearest nodes
tgi = the_grid_index.flatten()
areas = collections.Counter(tgi).values()
#print(areas)
#Get rid of counts of infinite nodes
for index in sorted(infinite_nodes, reverse=True):
    del areas[index]
print(max(areas)) #Answer


## If infinite, will have a "nearest" on the outer boundary...