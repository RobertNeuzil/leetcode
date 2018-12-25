a = [-2, 1, 2, 4, 7, 11]
target = 13

def two_sum_brute_force(a, target):
	for i in range(len(a) - 1):
		for j in range(i + 1, len(a)):
			if a[i] + a[j] == target:
				return a[i], a[j]

	return False


def two_sum_hash_table(a, target):
	ht = dict()
	for i in range(len(a)):
		if a[i] in ht:
			print(ht[a[i]], a[i])
			return True

		else:
			ht[target - a[i]] = a[i]

def two_sum(a, target):
	i = 0
	j = len(a) - 1

	while i <= j:
		if a[i] + a[j] == target:
			print (a[i], a[j])
			return True
		elif a[i] + a[j] < target:
			i += 1
		else:
			j -= 1
	return False


two_sum(a, target)