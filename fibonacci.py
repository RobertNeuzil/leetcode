fib_cache = { }


def fibonacci(n):
	#if element in cache, don't recalculate
	if n in fib_cache:
		return fib_cache[n]
	
	if n == 1 or n == 2:
		value = 1
	if n > 2:
		value = fibonacci(n-1) + fibonacci(n - 2)
	
	fib_cache[n] = value
	return value

for n in range(1, 101):
	print (n, ":", fibonacci(n) )


