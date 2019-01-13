sorted_list = [-2, -1, 1, 3, 5, 17, 19, 21, 23, 25]
target = 8


def find_the_sum(target, sorted_list):
	low = 0
	high = len(sorted_list) - 1
	while low < high:
		if sorted_list[low] + sorted_list[high] == target:
			print (sorted_list[low], "and", sorted_list[high], "equal", target)
			return True
		if target < sorted_list[low] + sorted_list[high]:
			high = high - 1
		if target > sorted_list[low] + sorted_list[high]:
			low = low + 1
	return False

print(find_the_sum(target, sorted_list))