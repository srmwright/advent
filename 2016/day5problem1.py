# what an absolute hash...

import hashlib

input = 'abbhdwsy'
answer = ''
breaker = False

for i in range(0,10000000):
	input_string = input + str(i)
	the_hash = hashlib.md5(input_string).hexdigest()
	if(the_hash[0:5]=='00000'):
		answer = answer + the_hash[5]
	if len(answer)==8:
		breaker = True
	if breaker:
		break

print(answer)