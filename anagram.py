
str_1 = "practice makes perfect"
str_2 = "perfect makes practice"
str_3 = "A car goes for a long time"
str_4 = "The cat can't stop eating bacon"


def anagram(str_1, str_2):
	str_1 = str_1.replace(" ", "")
	str_2 = str_2.replace(" ", "")

	if len(str_1) != len(str_2):
		return False
	
	str_1 = str_1.upper()
	str_2 = str_2.upper()

	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	dict_1 = dict.fromkeys(list(alphabet), 0)
	dict_2 = dict.fromkeys(list(alphabet), 0)

	for i in range(len(str_1)):
		dict_1[str_1[i]] += 1
		dict_2[str_2[i]] += 1

	return dict_1 == dict_2

print(anagram(str_1, str_2))
print(anagram(str_3, str_4))