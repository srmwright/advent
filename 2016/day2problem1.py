with open('input2.txt') as f:
    input = f.read()

lines = input.strip().split('\n')

position = [1,1]
keypad_size = 2

def mover(input,position):
	if(input=='L' and position[0]!=0):
		position[0] -=1
	if(input=='R' and position[0]!=keypad_size):
		position[0] +=1
	if(input=='U' and position[1]!=0):
		position[1] -=1
	if(input=='D' and position[1]!=keypad_size):
		position[1] +=1
	return(position)

for i in lines:
	for j in range(0,len(i)):
		position = mover(i[j],position)
	print(position)
	print(1+position[0]+3*(position[1]))