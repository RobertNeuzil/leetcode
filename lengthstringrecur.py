
def find_length(string):
	count = 0
	for x in string:
		count += 1
	return count


# We're slicing the str at 1, not 0.
# so, in the string "HelloWorld"
# the first recursion is "elloWorld"
# then "lloWorld" etc etc etc
# counting every recursion


def find_recursive(string):
	if string == "":
		return 0
	return find_recursive(string[1:]) + 1

"""
1: "DJKSD"
2: "JKSD"
3: "JKSD"
4: "SD"
5: "D"
100: ""

"""

print(find_recursive("sjkdljsaf"))