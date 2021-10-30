import numpy as np

### Input file into lines
with open('test5.txt') as f:
    input = f.read()

lines = input.strip().split('\n')

theSum = 0 #starting frequency
start = 0 #starting frequency

frequencies = list([start])
answer = []

#loop and check for recurrence
for i in range(0, len(lines)):
		start += int(lines[i])
		if(start in frequencies):
			answer.append(start)
			break
		frequencies.append(start)
theSum = start
frequencies1 = frequencies.copy() #copy is very important here
print(frequencies)
print(theSum)

#write function to check for recurrence
def checker(frequencies, frequencies1):
		for j in range(0,len(frequencies1)-1):
			if(frequencies[(len(frequencies1)-1)*i+j] in (frequencies[0:(len(frequencies1)-1)*i+j])):
				return(frequencies[(len(frequencies1)-1)*i+j]) #if match, return frequency


#write loop that appends multiples and runs the check
for i in range(1,1000):
		frequencies.extend([x+(theSum*i) for x in frequencies1[1:len(frequencies1)]])
		print(frequencies)
		answer = checker(frequencies,frequencies1)
		if(answer):
			break
print("answer is",answer)

### This takes far too long...use the sum of everything from part 1...

# def looper(lines, start, answer, frequencies):
# #loop over the list, adding as appropriate
# 	for i in range(0, len(lines)):
# 		start += int(lines[i])
# 		if(start in frequencies):
# 			answer.append(start)
# 			break
# 		frequencies.append(start)
# 	return(start)

# while len(answer)==0:
# 	start = looper(lines, start, answer, frequencies)
# 	print('loop')
# print(frequencies)
# print(answer)