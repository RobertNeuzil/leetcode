def recursive_binary_search(data, target, high, low):
	while low <= high:
		middle = (low + high) // 2

		if target == data[middle]:
			print (target)
			return True
		if target > data[middle]:
			return recursive_binary_search(data, target, high, middle + 1)
		if target < data[middle]:
			return recursive_binary_search(data, target, middle - 1, low)
	return False



def binary(data, target):
	low = 0
	high = len(data) - 1

	while low <= high:

		mid = (high + low) // 2

		if data[mid] == target:
			print (target, "at", "index", ":", mid)
			return True
		if target < data[mid]:
			high = mid - 1
		if target > data[mid]:
			low = mid + 1
	print ("Target does not exist in list")
	return False







data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 27

binary(data, target)