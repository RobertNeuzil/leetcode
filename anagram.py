
str_1 = "practice makes perfect"
str_2 = "perfect makes practice"
str_3 = "A car goes for a long time"
str_4 = "The cat can't stop eating bacon"


def anagram(str_1, str_2):
	str_1 = str_1.replace( " ", "" )
	str_2 = str_2.replace(" ", "")

	if len(str_1) != len(str_2):
		return False

	for c in str_1:
		if c in str_2:
			return True
	return False


print(anagram(str_1, str_2))
print(anagram(str_3, str_4))