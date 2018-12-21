import timeit
data = list(range(100000001))
	   
target = 2
target2 = 222222222  # two, too, to

# linear search


def linear_search(data, target):
    # range(len(data))  range(0, 15) start will start there, stop will generate numbers UP TO but NOT INCLUDING STOP
    for i in range(len(data)):
        if data[i] == target:
            return True

    return False




# iterative binary search
def binary_search(data, target):
	high = len(data) - 1
	low = 0
	while low < high:
		mid = (high + low) // 2
		if data[mid] == target:
			return True
		if data[mid] > target:
			high = mid - 1
		else:
			low = mid + 1

	return False

print(linear_search(data, target2))
#print(binary_search(data, target2)) 