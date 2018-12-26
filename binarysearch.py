el_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def binary_search(target, el_list):
	for x in el_list:
		if x == target:
			return True
	return False


def binary_better(target, el_list):
	high = len(el_list) - 1
	low = 0
	while low <= high:
		mid = (low + high ) // 2

		if el_list[mid] == target:
			return True
		elif target < el_list[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return False



def binary_recursive(data, target, high, low):
	if low > high:
		return False
	else:
		mid = (high + low) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			return binary_recursive(data, target, mid - 1, low)
		else:
			return binary_recursive(data, target, high, mid + 1)
	return False


print(binary_recursive(el_list, 7, len(el_list) -1 , 0))
