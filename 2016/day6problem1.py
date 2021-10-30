# break the repetition code

import collections

with open('input6.txt') as f:
    input = f.readlines()

# repetition code

word = ''
for i in range(0,len(input[0])):
	chars = []
	for line in input:
		chars.append(line[i])
	word = word + collections.Counter(chars).most_common(1)[0][0]

print(word)

# modified repetition code

word = ''
for i in range(0,len(input[0])):
	chars = []
	for line in input:
		chars.append(line[i])
		n = len(set(chars))
	word = word + collections.Counter(chars).most_common(n)[-1][0]

print(word)