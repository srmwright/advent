import collections

## Read file
with open('input.txt') as f:
    input = f.read()

lines = input.strip().split('\n')
twos = 0
threes = 0

for i in range(0, len(lines)):
	a = collections.Counter(str(lines[i])).values()
	print(a)
	two = sum(x == 2 for x in a) #count number of tuples
	three = sum(x == 3 for x in a) #count number of triples
	if two > 0: #iterate
		twos += 1
	if three > 0:
		threes += 1

print("Answer is", twos*threes) #print answer


