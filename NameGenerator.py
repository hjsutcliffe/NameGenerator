import random

#TODO: Clean up way names are displayed
#TODO: Add men's first names
#TODO: Add women's first names
#TODO: Add user input functionality

surname_list = []

def num_lines(file_name):
	with open(file_name) as file:
		for i, line in enumerate(file):
			pass
		return i + 1;

num_surnames = num_lines('last_names.txt');
name_index = random.randint(0, num_surnames - 1)
generated_name = 'Mr. '

with open('last_names.txt','r') as names:
	for i, line in enumerate(names):
		if i == name_index:
			generated_name += line.split(None, 1)[0]

print(generated_name)


