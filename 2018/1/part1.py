### Input file into lines
with open('input.txt') as f:
    input = f.read()

lines = input.strip().split('\n')

answer = 0 #starting frequency

#loop over the list, adding as appropriate
for i in range(0, len(lines)):
	answer += int(lines[i])

print(answer)