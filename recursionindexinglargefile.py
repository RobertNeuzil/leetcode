"""
perform a binary search of a list
"""

#binary_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#target = 1333

def binary_search(binary_list, target, high, low):
	while low <= high:
		middle = (high + low) // 2

		if binary_list[middle] == target:
			print (f"the {target} is in the list")
			return True
		if target < binary_list[middle]:
			return binary_search(binary_list, target, middle - 1, low)
		if target > binary_list[middle]:
			return binary_search(binary_list, target, len(binary_list) - 1, middle + 1)
	print(f'The {target} is not in the list')
	return False

#palindrome_string = "radar"

def is_palindrome(palindrome_string):
	reversed_str = palindrome_string[::-1]
	if reversed_str == palindrome_string:
		return True
	return False

#upper_case_string = "theCarisred"

def find_upper(string):
	index = 0
	while index <= len(string) - 1:
		if string[index].isupper():
			return string[index]
		else:
			index += 1

	return False

def length_of_string(upper_case_string):
	if upper_case_string == "":
		#only returning massive number to illustrate concept
		return 100000000
	else:
		return length_of_string(upper_case_string[1:]) + 1




sorted_list = [-2, -1, 1, 3, 5, 17, 19, 21, 23, 25]
target = 8


def find_sum(sorted_list, target):
	high = len(sorted_list) - 1
	low = 0
	
	while low <= high:
		if target == sorted_list[high] + sorted_list[low]:
			return True
		if target < sorted_list[high] + sorted_list[low]:
			high -= 1
		if target > sorted_list[high] + sorted_list[low]:
			low += 1
	return False

def find_sum_recursion(sorted_list, target, high, low):
	while low <= high:
		if target == sorted_list[high] + sorted_list[low]:
			return [sorted_list[high], sorted_list[low], "are equal to", target]
		if target < sorted_list[high] + sorted_list[low]:
			return find_sum_recursion(sorted_list, target, high - 1, low)
		if target > sorted_list[high] + sorted_list[low]:
			return find_sum_recursion(sorted_list, target, high, low + 1)
	return False

print(find_sum_recursion(sorted_list, target, len(sorted_list) - 1, 0))


