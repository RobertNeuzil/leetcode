from functools import lru_cache

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
target = 4

def binary_recursive(my_list, target, high, low):
    while low <= high:
        mid = (high + low) // 2

        if target == my_list[mid]:
            print (f'{target} is an element in {my_list}')
            return True
        if target < my_list[mid]:
            return binary_recursive(my_list, target, mid - 1, low)
        if target > my_list[mid]:
            return binary_recursive(my_list, target, high, mid + 1)
    print (f'{target} is not an element in {my_list}')
    return False



string_with_upper = "robertNeuzil"

def find_upper(string, index = 0):
    if string[index].isupper():
        return string[index]
    if string[index] == len(string) - 1:
        return "none found"
    else:
        return find_upper(string, index + 1)


@lru_cache(maxsize = 300)
def f(n):

    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)

for p in range(1, 101):
    print (f(p))