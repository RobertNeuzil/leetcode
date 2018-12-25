def F(n):
	if n == 1 or n == 2:
		return 1
	return F(n-1) + F(n-2)

for i in range(1, 11):
	print (F(i))

