string_1 = "robertneuzil"

'''
The real world solution is to use the
len() func that comes installed in the
standard library. This is simply an application
of recursion vs iteration. The len() func
has been tested and perfected over and over
by talented programmers. 


'''
def iterative_str_length(string_1):
	count = 0
	for e in string_1:
		count += 1
	return count

#print(iterative_str_length(string_1))

def recursive_str_length(string_1):
	if string_1 == "":
		return 0
	return 1 + recursive_str_length(string_1[1:])


print(recursive_str_length(string_1))