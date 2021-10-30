import re
import numpy as np

with open('input.txt') as f:
    input = f.read()

lines = input.strip().split('\n')

#Initialise input lists
claims = list([])
x_init = list([])
y_init = list([])
x_size = list([])
y_size = list([])

#REGEX?
p = re.compile(r'\d+')
for i in range(0, len(lines)):
	numbers = p.findall(lines[i])
	claims.append(int(numbers[0]))
	x_init.append(int(numbers[1]))
	y_init.append(int(numbers[2]))
	x_size.append(int(numbers[3]))
	y_size.append(int(numbers[4]))

#Get the ending index of each piece of fabric
x_fin = tuple(map(sum, zip(x_init, x_size)))
y_fin = tuple(map(sum, zip(y_init, y_size)))

#Create a matrix
fabric = np.zeros((max(x_fin),max(y_fin)))
fabric2 = np.zeros((max(x_fin),max(y_fin)))

#Count how often each piece is cut
for i in range(0, len(lines)):
	fabric[x_init[i]:x_fin[i],y_init[i]:y_fin[i]] += 1
	fabric2[x_init[i]:x_fin[i],y_init[i]:y_fin[i]] += claims[i]

#Flatten arrays for convenience
fabric_f = (fabric==1).flatten()*1
fabric2_f = fabric2.flatten()

#Send everything that overlap to zero
fabric_counter = [ x*y for x,y in zip(fabric_f, fabric2_f)]

sizes = [x*y for x,y in zip(x_size, y_size)] #calculate cut sizes
counts = [0]*len(lines)

#Count cases where no overlap
for i in range(0, len(fabric_counter)):
	if(fabric_counter[i] > 0):
		counts[int(fabric_counter[i])-1] += 1

#If number of cases equals size, give answer
x = np.where(np.equal(sizes, counts))
print(claims[int(x[0])])
