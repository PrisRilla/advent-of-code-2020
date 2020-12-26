# How many passwords are valid?
# Part 1: min-max occurrences
# Part 2: positional value


def read_input():
	f = open('input.txt','r')
	file = [tuple(row.replace(':','').replace('-'," ").split(" ")) for row in f.read().split('\n') if len(row)>0]
	return file


def valid_password_max_min(entry):
	"""Check if is a valid password for tuple.
	Based on min/max occurrences of a character.

	Input:
		tuple: min, max, letter, password
	Output:
		str: password
	"""
	min_count = int(entry[0])
	max_count = int(entry[1])
	letter = entry[2]
	password = entry[3]
	counter = 0
	
	for char in password:
		if char == letter:
			counter+=1

	if counter >= min_count and counter <= max_count:
		return password
	else:
		return None


def count_valid_passwords_max_min(input):
	"""Count number of valid passwords for input list.
	Based on min/max occurrences of character.
	
	Input:
		list: tuples (min, max, letter, password)
	Output:
		int: number of valid passwords
	"""
	ls = []
	for entry in input:
		if valid_password_max_min(entry) is not None:
			ls.append(valid_password_max_min(entry))

	return len(ls)


def valid_password_positional(entry):
	"""Check if valid password for a tuple.
	Based on position of characters.

	Input:
		tuple: position 1, position 2, letter, password
	Output:
		str: password
	"""
	pos1 = int(entry[0])-1
	pos2 = int(entry[1])-1
	letter = entry[2]
	password = entry[3]

	if password[pos1]==letter or password[pos2]==letter:
		if password[pos1]==letter and password[pos2]==letter:
			return None
		return password
	return None


def count_valid_passwords_positional(input):
	"""Count number of valid passwords for input list.
	Based on position of characters.

	Input:
		list: tuples (position 1, position 2, letter, password)
	Output:
		int: number of valid passwords
	"""
	count = 0
	for entry in input:
		if valid_password_positional(entry) is not None:
			count+=1
	
	return count


if __name__=="__main__":
	input = read_input()
	
	# Part 1
	valid_max_min = valid_password_max_min(input[-3])
	# print(valid)
	number_valid = count_valid_passwords_max_min(input)
	# print(number_valid)


	# Part 2
	for i in input[:5]:
		print(valid_password_positional(i))
	
	print( count_valid_passwords_positional(input))
