sorted_list = [-2, -1, 1, 3, 5, 17, 19, 21, 23, 25]
target = 48


def find_the_sum(target, sorted_list, low, high):
	
	while low < high:
		if sorted_list[low] + sorted_list[high] == target:
			return True
		if target < sorted_list[low] + sorted_list[high]:
			return find_the_sum(target, sorted_list, 0, high - 1)
		if target > sorted_list[low] + sorted_list[high]:
			return find_the_sum(target, sorted_list, low + 1, high)
	return False

print(find_the_sum(18, sorted_list, 0, len(sorted_list) - 1))