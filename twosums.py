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


print(find_sum(sorted_list, 8))