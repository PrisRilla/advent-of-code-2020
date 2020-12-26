# Part 1: Find the two entries that sum to 2020; what do you get if you multiply them together?
# Part 2: What is the product of the three entries that sum to 2020?
import math


def read_report():
	file = open("expense_report_input.txt", "r")
	nums = [int(x) for x in file.read().split('\n') if x!='' and int(x) < 2020]
	return nums


def find_2_relevant_numbers(nums, target):
	"""Return list of 2 relevant numbers that sum to 2020."""
	ls = []
	d = {}
	for n in nums:
		if n not in d:
			d[n] = target-n
	for k,v in d.items():
		if v in nums:
			if k and v not in ls:
				ls.extend([k,v])
	return ls		


def find_3_relevant_numbers(nums, target):
	"""Return list of 3 relevant numbers that sum to 2020."""
	ls = []
	nums.sort()

	for i in range(0, len(nums)):
		j = i+1
		k = len(nums)-1
		remaining_sum = target - nums[i]

		while j < k and i < len(nums)-3:
			if nums[j] + nums[k]==remaining_sum:
				ls.extend([nums[i],nums[j], nums[k]])
				return ls
			elif nums[j] + nums[k] < remaining_sum:
				j+=1
			elif nums[j] + nums[k] > remaining_sum:
				k-=1
	return False



if __name__=="__main__":
	nums = read_report()
	
	# Part 1
	pair_sum = find_2_relevant_numbers(nums,2020)
	print(pair_sum)
	pair_prod = math.prod(pair_sum)
	print (pair_prod)

	# Part 2
	triple_sum = find_3_relevant_numbers(nums,2020) 
	print(triple_sum)
	triple_prod = math.prod(triple_sum)
	print(triple_prod)
