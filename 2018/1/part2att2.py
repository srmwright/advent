### Idea - calculate differences between all cumulative frequncies in the list
### Look for gaps that are multiples of the sums
### Use this fact to find the first recurrence

import numpy as np
import math

### Input file into lines
with open('input.txt') as f:
    input = f.read()

lines = input.strip().split('\n')
theSum = 0
start = 0
frequencies = list([])
#loop over the list, build the cumulative frequencies
for i in range(0, len(lines)):
		start += int(lines[i])
		if(start in frequencies):
			answer.append(start)
			break
		frequencies.append(start)
theSum = start

freq_np = np.array(frequencies) #feed cum. frequencies in numpy array

freq_mat = freq_np[:,np.newaxis] - freq_np #create a difference matrix between the vector and itself
#print(freq_mat%theSum==0*freq_mat)
i, j = np.where(freq_mat%theSum==0) #find all pairs where the gaps are multiples of the sum of the list

#input parameters for loops - this would all be unnecessary if I could do vectors
i_vals = []
j_vals = []
floors = []
for i1 in range(0,len(i)):
		if i[i1] > j[i1]:
			i_vals.append(i[i1]) #keep track of second value
			j_vals.append(j[i1]) #keep track of first value THIS IS THE ONE WE WANT
			floors.append(math.floor(freq_mat[i[i1], j[i1]]/theSum)) #calculate number of loops required

index = 0
abs_floor = 0
loops = 0
for i in range(0,len(floors)):
	if floors[i]==min(np.abs(floors)):
		abs_floor = floors[i]
		index = j_vals[i] - 1
		loops = i
		break
answer = frequencies[index] + abs_floor*theSum #calculate the actual frequency at the loop point
print(answer)

# test = np.tril(freq_mat%theSum==0,1,0)
# print(test)
#print(np.floor(freq_mat,theSum) if freq_mat%theSum==0 else 0)

#print(np.floor(np.tril(freq_mat)/theSum))
