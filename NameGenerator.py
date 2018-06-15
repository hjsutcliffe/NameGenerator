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

def generate_index(file_name):
	count = num_lines(file_name);
	index = random.randint(0, count - 1)
	return index

def generate_name(file_name, index):
	name = ''
	with open(file_name) as names:
		for i, line in enumerate(names):
			if i == index:
				name += line.split(None, 1)[0]
	return name

first_index = generate_index('male_names.txt')
last_index = generate_index('last_names.txt')

fullname = generate_name('male_names.txt', first_index) 
fullname += ' ' + generate_name('last_names.txt', last_index)

print(fullname)


