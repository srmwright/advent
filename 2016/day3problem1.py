# which triangles are impossible?

with open('input3.txt') as f:
    lines = f.readlines()

def isProper(sides):
	sides = sorted(sides)
	if(sides[0]+sides[1] > sides[2]):
		return(1)
	else:
		return(0)

counter = 0

for i in range(0,len(lines)):
	lines[i] = map(str.strip, filter(None, lines[i].split("  ")))
	lines[i] = [int(k) for k in lines[i]]
	counter += isProper(lines[i])

print(len(lines))
print(counter)
