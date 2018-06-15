import random

def num_lines(file_name):
    """Return the number of lines in a file"""
    with open(file_name) as file:
        for i, line in enumerate(file):
            pass
        return i + 1

def generate_index(file_name):
    """Return a random line number from a file"""
    count = num_lines(file_name)
    index = random.randint(0, count - 1)
    return index

def generate_name(file_name, index):
    """Return the name at line number index from a file"""
    name = ''
    with open(file_name) as names:
        for i, line in enumerate(names):
            if i == index:
                name += line.split(None, 1)[0]
    return name

def get_gender():
    """Return the user's choice of gender"""
    gender = input('Which kind of name would you like? Enter m for male or f for female ')
    while True:
        try:
            return {'m': 'male', 'f': 'female'}[gender]
        except KeyError:
            print("Please enter 1 for male or 2 for female")

def main():
    last_index = generate_index('last_names.txt')
    gender = get_gender()
    if gender == 'male':
        first_index = generate_index('male_names.txt')
        fullname = generate_name('male_names.txt', first_index)
    else:
        first_index = generate_index('female_names.txt')
        fullname = generate_name('female_names.txt', first_index)

    fullname += ' ' + generate_name('last_names.txt', last_index)
    print(fullname.title())


main()
