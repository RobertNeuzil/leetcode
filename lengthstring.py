# write a function to find the length of a string, without use the standard len()


string_1 = "Hello and goooo                     dbye."

def find_length(string):
	count = 0
	for x in string:
		count += 1
	return count



def find_length_no_space(string):
	count = 0
	string = string.replace(" ", "")
	for x in string:
		count += 1
	return count







print(find_length(string_1))
print(find_length_no_space(string_1))