string_1 = "RobertNeuzil"
string_2 = "robertNeuzil"
string_3 = "RobertNeuzil"

def find_first_upper(string):
	string_up = string.upper()

	for c in string:
		if c in string_up:
			return c
	return False

def find_upper_recursive(string, index = 0):
	if string[index].isupper():
		return string[index]
	if index == len(string) - 1:
		return "None Found"
	return find_upper_recursive(string, index + 1)
	

print(find_upper_recursive(string_1))