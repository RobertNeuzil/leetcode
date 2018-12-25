from functools import lru_cache

fibonacci_cache = {}

def fibonacci(n):
	if n in fibonacci_cache:
		return fibonacci_cache[n]
	
	if n == 1:
		value = 1
	if n == 2:
		value = 1
	elif n > 2:
		value = fibonacci(n-1) + fibonacci(n-2)

	fibonacci_cache[n] = value
	return value




@lru_cache(maxsize = None)
def fibonacci_two(n):
	if n == 1:
		return 1
	if n == 2:
		return 2
	elif n > 2:
		return fibonacci_two(n -1) + fibonacci_two(n -2)

for n in range(1, 101):
	print (n, ":", fibonacci_two(n))


#for n in range(1, 1001):
	#print (n, ":", fibonacci(n))