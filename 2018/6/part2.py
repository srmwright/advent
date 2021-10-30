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

safe = 0 #count number of safe places
safe_def = 10000 #sum of taxicab distance to be safe
for i in range(0,size_of_grid[0]): #loop over grid
	for j in range(0, size_of_grid[1]):
		tot_distance = 0
		for k in range(0,len(coords)): #sum total distance
			tot_distance += taxicab(coords[k],list([j,i]))
		if tot_distance < safe_def: #if safe, increment
			safe += 1

print(safe) #answer
