#same as before, but with some bastard
#star grid

with open('input2.txt') as f:
    input = f.read()

lines = input.strip().split('\n')

#test
#lines = ['ULL','RRDDD','LURDL','UUUUD']

position = [0,2]
keypad_size = [0,2,4,2,0]

def mover(input,position):
	if(input=='L' and position[0]!=(2-keypad_size[position[1]]/2)):
		position[0] -=1
	if(input=='R' and position[0]!=(2+keypad_size[position[1]]/2)):
		position[0] +=1
	if(input=='U' and position[1]!=(2-keypad_size[position[0]]/2)):
		position[1] -=1
	if(input=='D' and position[1]!=(2+keypad_size[position[0]]/2)):
		position[1] +=1
	return(position)

for i in lines:
	for j in range(0,len(i)):
		position = mover(i[j],position)
		#print(i[j],position)
	print(position)