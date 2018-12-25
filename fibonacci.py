cache_dict = {}

def fibonacci(n):

	if n in cache_dict:
		return cache_dict[n]

	if n == 1 or n == 2:
		value = 1
	else:
		value = fibonacci(n-1) + fibonacci(n-2)
	cache_dict[n] = value
	return value

for x in range(1, 101):
	print (x, ":", fibonacci(x))

