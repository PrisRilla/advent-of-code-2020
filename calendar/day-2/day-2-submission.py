# How many passwords are valid?


def read_input():
	f = open('input.txt','r')
	file = [tuple(row.replace(':','').replace('-'," ").split(" ")) for row in f.read().split('\n') if len(row)>0]
	return file


def valid_password(entry):
	"""Checks if is a valid password for tuple.
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


def count_valid_passwords(input):
	"""Count number of valid passwords for input list
	Input:
		list: tuples (min, max, letter, password)
	Output:
		int: number of valid passwords
	"""
	ls = []
	for entry in input:
		if valid_password(entry) is not None:
			ls.append(valid_password(entry))

	return len(ls)


if __name__=="__main__":
	input = read_input()

	valid = valid_password(input[-3])
	# print(valid)

	number_valid = count_valid_passwords(input)
	print(number_valid)
