# How many passwords are valid?


def read_input():
	f = open('input.txt','r')
	file = [row for row in f.read().split('\n')]
	return file


def valid_password(input):
	"""Checks for valid passwords in ana input list.
	Input:
		list: min-max char: password
	Output:
		list: password
	"""
	return True	

if __name__=="__main__":
	input = read_input()
	print(input)

	valid_list = valid_password(input)
	print(valid_list)

