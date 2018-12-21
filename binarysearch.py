data = [1, 2, 4, 8, 9, 11, 14, 19, 22, 23, 24, 25, 27, 1223, 1990192]
       #0  1  2  3  4  5   6   7   8    9  10  11  12   13    14
target = 2
target2 = 88888888888888888888888888888888888

# linear search
def linear_search(data, target):
	for i in range(len(data)):  # range(len(data))  range(0, 15) start will start there, stop will generate numbers UP TO but NO INCLUDING STOP
		if data[i] == target:
			return True

	return False



#print (linear_search(data, target))

#iterative binary search
def binary_search(data, target):
	low = 0
	high = len(data) -1 #len(data) is 15. But we're starting from index 0, to index 14, for a total of 15 elements. Subtract 1

	while low <= high: # will be True until there are no more elements left
		mid = (low + high) // 2  # 14 // 2 == 7
		if target == data[mid]: # if the target is equal to index 7 (the middle point, the first iteration), we're done
			return True
		elif target < data[mid]:  # if 2 < 19
			high = mid -1   # the high end of the list is is now at index 6
		else:
			low = mid + 1  # or, if not, the low end of the list is now at index 8
			# repeat this process over and over until line 25 becomes true.
	return False # or not and the number must not be an element in the list

print (binary_search(data, target))
print (binary_search(data, target2))