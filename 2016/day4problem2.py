# cypher!

import re
import string
from operator import itemgetter

with open('input4.txt') as f:
    input = f.readlines()

alphabet = list(string.ascii_lowercase)

for i in range(0,len(input)):
 	letters = re.findall("[a-z-]+",input[i])[0]
 	sector_id = int(re.findall("[0-9]+",input[i])[0])
 	new_letters = ''
	for i in range(0,len(letters)):
		if(letters[i]!='-'):
			new_letters += alphabet[(alphabet.index(letters[i]) + sector_id) % 26]
		else:
			new_letters += '-'
	location = new_letters.find('north')
	if(location>=0):
		print(new_letters,sector_id)
