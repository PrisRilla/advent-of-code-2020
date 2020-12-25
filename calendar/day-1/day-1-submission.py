# Part 1
## Find the two entries that sum to 2020; what do you get if you multiply them together?
import math


def read_report():
	file = open("expense_report_input.txt", "r")
	nums = [int(x) for x in file.read().split('\n') if x!='']
	print(nums)
	return nums

def find_relevant_numbers(nums):
	"""Return list of relevant numbers that sum to 2020."""
	ls = []
	d = {}
	for n in nums:
		if n not in d:
			d[n] = 2020-n
	for k,v in d.items():
		if v in nums:
			if k and v not in ls:
				ls.extend([k,v])
	print(ls)
	return ls		


if __name__=="__main__":
	nums = read_report()
	candidates = find_relevant_numbers(nums)
	prod = math.prod(candidates)
	print (prod) 
