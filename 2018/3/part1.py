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
	x_init.append(int(numbers[1]))
	y_init.append(int(numbers[2]))
	x_size.append(int(numbers[3]))
	y_size.append(int(numbers[4]))

#Get the ending index of each piece of fabric
x_fin = tuple(map(sum, zip(x_init, x_size)))
y_fin = tuple(map(sum, zip(y_init, y_size)))

#Create a matrix
fabric = np.zeros((max(x_fin),max(y_fin)))

#Count how often each piece is cut
for i in range(0, len(lines)):
	fabric[x_init[i]:x_fin[i],y_init[i]:y_fin[i]] += 1 

#Print the answer
print(sum(sum(fabric>1)))