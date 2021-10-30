# which rooms are real?

import re
import string
from operator import itemgetter

with open('input4.txt') as f:
    input = f.readlines()

alphabet = list(string.ascii_lowercase)

def letter_counter(input_string):
	occurrences = []
	for letter in alphabet:
		occurrences.append(input_string.count(letter))
	z = zip(alphabet,occurrences)
	z2 = sorted(z, key=itemgetter(1), reverse=True)
	checksum = ''
	for i in range(0,5):
		checksum = checksum + z2[i][0]
	return(checksum)

sum = 0

for i in range(0,len(input)):
 	letters = re.findall("[a-z-]+",input[i])
 	sector_id = int(re.findall("[0-9]+",input[i])[0])
 	#print(letter_counter(letters[0]))
 	#print(letters[1])
 	if letters[1] == letter_counter(letters[0]):
 		sum += sector_id

print(sum)
