import time
from datetime import datetime
import re
import numpy as np
import pandas as pd

with open('input.txt') as f:
    input = f.read()

lines = input.strip().split('\n')

datetimes = list([])
dates = list([])
minutes = list([])
text = list([])

for i in range(0, len(lines)):
	datetimes.append(datetime.strptime(str(re.findall(r'\[([^]]*)\]', lines[i])[0]), '%Y-%m-%d %H:%M'))
	minutes.append(datetimes[i].minute)
	dates.append(datetimes[i].date())
	text.append(re.findall(r"\[.*\](.*)", lines[i])[0].strip())
	#Input the text for the action

#Create data frame
df = pd.DataFrame({
	'datetime': datetimes,
	'minutes': minutes,
	'date': dates,
	'action': text
	})
#Sort the data frame
df = df.sort_values(['datetime'])
df['guard_number'] = df['action'].apply(lambda x: re.findall(r".*#(\d*).*", x)[0] if x[0]=="G" else 0)
df['time_asleep'] = df['minutes'] - df['minutes'].shift(1)
#Group by guard
df['guard_number'] = df['guard_number'].replace(to_replace=0, method='ffill')
df_wakeup = df.loc[df['action']=='wakes up']
df_wakeup['time_asleep'] = df_wakeup['time_asleep'].apply(lambda x: int(x))
df_wakeup = df_wakeup.groupby(['guard_number'])['time_asleep'].sum().reset_index()
df_wakeup = df_wakeup.sort_values(['time_asleep'], ascending = False).reset_index()

guard_no = df_wakeup['guard_number'][0]
print(df_wakeup.head())
print(guard_no)
#Most popular sleeping minute
df_sleepy = df.loc[df['guard_number']==guard_no]
df_sleepy = df_sleepy[df_sleepy['action']=='wakes up'].reset_index()
df_sleepy['time_asleep'] = df_sleepy['time_asleep'].apply(lambda x: int(x))

print(df_sleepy.head())
minute_counter = [0]*60
for i in range(0, len(df_sleepy)):
	for j in range(int((df_sleepy['minutes'][i] - int(df_sleepy['time_asleep'][i]))),df_sleepy['minutes'][i]):
		minute_counter[j] += 1

max_mins = int(np.argmax(minute_counter))
print(max_mins)
print(guard_no)

print(max_mins*int(guard_no))

### Same problem globally
top_guard = 0
max_minute = 0
max_counter = 0
guard_list = set(df['guard_number'])

def max_min_per_guard(df2):
	minute_counter = [0]*60
	for i in range(0, len(df2)):
		for j in range(int((df2['minutes'][i] - int(df2['time_asleep'][i]))),df2['minutes'][i]):
			minute_counter[j] += 1
	max_mins = int(np.argmax(minute_counter))
	return [max_mins,max(minute_counter)]

print(guard_list)

for guard in guard_list:
	#print(df)
	#print(int(guard))
	df_guard = df[df['action']=='wakes up'].reset_index()
	df_guard = df_guard.loc[df_guard['guard_number']==guard].reset_index()
	df_guard['time_asleep'] = df_guard['time_asleep'].apply(lambda x: int(x))
	#print(df_guard.head())
	maxmins = max_min_per_guard(df_guard)
	if(maxmins[1] > max_counter):
		max_minute = maxmins[0]
		max_counter = maxmins[1]
		top_guard = guard
	print(max_minute,max_counter,top_guard)

print("Top guard is",top_guard)
print("Max minute is",max_minute)
print("Count was",max_counter)
print("Answer is",int(top_guard)*int(max_minute))

