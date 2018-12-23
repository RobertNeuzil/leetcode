'''

Check to see if a string has unique characters

'''

str_1 = "bear"
str_2 = "radar"


def check(string):
	list_string = list(string)
	set_string = set(string)
	if len(list_string) == len(set_string):
		return True
	else:
		return False


print(check(str_1))
print(check(str_2))


	

