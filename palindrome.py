input_str = "mad  am"

def is_palindrome(string):
	string = string.replace(" ", "")
	reversed_str = string[::-1]
	if string == reversed_str:
		return True
	return False


print(is_palindrome(input_str))