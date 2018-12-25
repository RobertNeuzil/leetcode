my_num = [1, 2, 3, 4, 5, 6, 7, 9, 11, 15, 19, 22, 26]
target = 6



def binary_recursive(my_num, target, high, low):
	while high >= low:
		mid = (high + low) // 2
		if my_num[mid] == target:
			return True
		if target < my_num[mid]:
			return binary_recursive(my_num, target, mid + 1, low)
		else:
			return binary_recursive(my_num, target, high, mid + 1)
	
	return False



print (

binary_recursive(my_num, target, len(my_num) -1, 0)
)