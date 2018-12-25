data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target = 128
target2 = 4

def is_target_in_list(data, target):
	for c in data:
		if c == target:
			return True
	return False

#print(is_target_in_list(data, target))
#print(is_target_in_list(data, target2))

def binary_search(data, target):
	if len(data) < 1:
		return None
	low = 0
	high = len(data) - 1

	while low <= high:
		mid = (low + high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return False

#print (binary_search(data, target))
#print (binary_search(data, target2))

def binary_recursive(data, target, low, high):
	if low > high:
		return False
	else:
		mid = (low + high) // 2
	if target == data[mid]:
		return True
	elif target < data[mid]:
		return binary_recursive(data, target, low, mid-1)
	else:
		return binary_recursive(data, target, mid + 1, high)

print (binary_recursive(data, target, 0, len(data) - 1))
print (binary_recursive(data, target2, 0, len(data) - 1))