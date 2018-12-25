
str_1 = 'robertNeuzil'
str_2 = 'RobertNeuzil'
str_3 = 'ROBERTNEuziL'

base = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", 
"K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
"W", "X", "Y", "Z"]

def find_upper(string, listof):
	string = list(string)

	for c in string:
		if c in listof:
			print (c)
	return None

find_upper(str_3, base)
