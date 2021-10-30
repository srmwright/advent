# which triangles are impossible?
# now when reading by column

#import numpy as np

# a better way of doing what I wanted last time...
with open('input3.txt') as f:
    #w, h = [int(x) for x in next(f).split()]
    array = [[int(x) for x in raw.strip().split()] for raw in f]

columns = zip(*array)

def isProper(sides):
	sides = sorted(sides)
	if(sides[0]+sides[1] > sides[2]):
		return(1)
	else:
		return(0)


counter = 0

for col in columns:
	for i in range(0,len(col)/3):
		sides = col[3*i:3*(i+1)]
		counter += isProper(sides)

print(counter)