# what an absolute hash...

import hashlib

input = 'abbhdwsy'
indices = ['0','1','2','3','4','5','6','7']
answer = ['z']*8
breaker = False

for i in range(0,100000000):
	input_string = input + str(i)
	the_hash = hashlib.md5(input_string).hexdigest()
	if(the_hash[0:5]=='00000' and the_hash[5] in indices):
		idx = int(the_hash[5])
		if(answer[idx]=='z'):
			answer[idx] = the_hash[6]
	if('z' not in answer):
		breaker = True
	if breaker:
		break

print(''.join(answer))

# 424a0197