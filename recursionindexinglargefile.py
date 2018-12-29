from functools import lru_cache

my_list = [1, 2, 4, 8, 9, 10,  11, 14, 19, 22]
target = 11
def binary_search(my_list, target, high, low):


    while low <= high:
        mid = (high + low) // 2

        if target == my_list[mid]:
            return True
        elif target < my_list[mid]:
            return binary_search(my_list, target, mid - 1, low)
        elif target > my_list[mid]:
            return binary_search(my_list, target, high, mid + 1)
    return False

my_string = "sjdkaljdaklsjdaklsfjdlksjdaklsfjlkasfjslkfjdlksdajdskl"

def length_string(string):

    if string == "":
        return 0
    else:
        return length_string(string[1:]) + 1



def is_palindrome(string):
    string = string.lower()
    
    if len(string) <= 1:
        return False
    reversed_string = string[::-1]

    if string == reversed_string:
        return True

    return False


@lru_cache(maxsize = 100)
def f(n):

    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n - 2)

for x in range (1, 50):
    print (f(x))