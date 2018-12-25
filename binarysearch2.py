data = [1, 2, 3, 4, 5, 6, 7, 8 , 9]
target = 2

def recursive_binary(data, target, low, high):
	if low > high:
		return False
	else:
		mid = (low + high) // 2
		if data[mid] == target:
			return True
		
		elif target < data[mid]:
			return (recursive_binary(data, target, low, mid - 1))
		else:
			return (recursive_binary(data, target, mid + 1, high))


print(recursive_binary(data, 1110, 0, len(data) - 1))