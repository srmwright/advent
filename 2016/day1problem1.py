with open('input1.txt') as f:
    input = f.read()

inst = input.strip().split(', ')

#part 1 - how far away do you end up?

#up, right, down, left
position = [0,0,0,0]
orientation = 0

for i in range(0,len(inst)):
	if(inst[i][0] == 'R'):
		orientation += 1
	elif(inst[i][0] == 'L'):
		orientation -= 1
	idx = orientation % 4
	position[idx] += int(inst[i][1:])

distance = abs(position[0] - position[2]) + abs(position[1] - position[3])
print(distance)

#part 2 - how far away is the first place you end up twice?

#up/down, right/left
position = [0,0,0,0]
orientation = 0

for i in range(0,len(inst)):
	if(inst[i][0] == 'R'):
		orientation += 1
	elif(inst[i][0] == 'L'):
		orientation -= 1
	idx = orientation % 4
	steps = inst[i][1:]
	for j in range(0,steps):
		if(idx <= 1):
			position[idx] += 1
		else:
			position[idx-2] -= 1
		for k in range(0,len(history)):
			if(position==history[k]):
				print("I've been here before!", abs(position[0]) + abs(position[1]))
				break
		history.push_back(position)

distance = abs(position[0] - position[2]) + abs(position[1] - position[3])
print(distance)
