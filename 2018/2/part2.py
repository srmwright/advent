import collections

## Read file
with open('input.txt') as f:
    input = f.read()

lines = input.strip().split('\n')

## Read over all pairs of lines
for i in range(0, len(lines)):
	for j in range(i, len(lines)):

		# Return true/false for every pairwise character comparison
		a = [x==y for (x,y) in zip(list(lines[i]),list(lines[j]))]
		diff = len(a) - sum(a) #Count number of differences
		if(diff == 1): #If 1
			#Find position of the same indices
			same_indices = [k for k, x in enumerate(a) if x]
			#Find the characters
			indices = list(list(lines[i])[q] for q in same_indices)
			#Turn back into a string
			print(''.join(indices))
			#list(lines[i])[k for k, x in enumerate(a) if x]