'''

Check to see if a string has unique characters

'''

str_1 = "bear"
str_2 = "radar"


def unique(one):
	one = list(one)
	two = set(one)

	if len(one) == len(two):
		return True
	else:
		return False


print (unique(str_1))
print(unique(str_2))

	

