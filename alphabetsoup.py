

def alphabetsoup(string):
	li = sorted(list(string))
	newstring = ''
	for x in li:
		newstring += x

	return newstring

word = input('please enter a string:')
print (alphabetsoup(word))