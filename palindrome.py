str_1 = "ra             DaR"
str_2 = "madam"
str_3 = "The cow is looking for breakfast"


def is_palindrome(string):
	string = string.lower()
	string = string.replace(" ", "")
	reversed_str = string[::-1]

	if reversed_str == string:
		return True

	return False


print(is_palindrome(str_3))