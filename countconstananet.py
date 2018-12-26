vowels = "aeiou"

input_str1 = "abc de"
input_str2 = "EeEeE"


def count_iterative(string, vowels):
    string = string.lower()
    count = 0
    for x in string:
        if x in vowels:
            count += 1
    return count


def count_recursive(string):
    if string == "":
        return 0
    if string[0].lower() not in vowels:
        return 1 + count_recursive(string[1:])
    else:
        return count_recursive(string[1:])



print(count_iterative(input_str1, vowels))
print(count_iterative(input_str2, vowels))


print ( count_recursive(input_str1) )