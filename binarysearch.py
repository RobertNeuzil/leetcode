data = [1, 2, 4, 8, 9, 11, 14, 19, 22, 23, 24, 25, 27, 1223, 1990192]
target = 2


# linear search
def linear_search(data, target):
	for i in range(len(data)):
		if data[i] == target:
			return True

	return False



#print (linear_search(data, target))

#iterative binary search
def binary_search(data, target):
	low = 0
	high = len(data) -1

	while low <= high:
		mid = (low + high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			high = mid -1
		else:
			low = mid + 1
	return False

print ( binary_search(data, target) )