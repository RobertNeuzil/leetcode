data = [1, 2, 4, 8, 9, 11, 13, 14, 15, 18, 19, 22, 25, 26, 28]
target = 11
target2 = 12


def iterative_search(target, data):
	for c in data:
		if c == target:
			return True
	return False



def binary_search(target, data):
	high = len(data) - 1
	low = 0

	while low <= high:
		mid = (low + high) // 2
		if data[mid] == target:
			return True
		elif target < data[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return False

def recursive_search(target, data, low, high):
	if low > high:
		return False
	else:
		mid = (low + high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			return recursive_search(target, data, low, mid -1)
		else:
			return recursive_search(target, data, mid + 1, high)






#print(iterative_search(target, data))
#print(iterative_search(target2, data))

#print(binary_search(target, data))
#print(binary_search(target2, data))

print(recursive_search(target, data, 0, len(data) - 1))