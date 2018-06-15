import random

surname_list = []

with open('last_names.txt','r') as names:
	for line in names:
		surname_list.append(line.split(None, 1)[0])

num_surnames = len(surname_list)
generated_name = 'Mr. ' + surname_list[random.randint(0, num_surnames - 1)]

print(generated_name)


