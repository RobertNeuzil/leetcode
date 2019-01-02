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

def length_of_string(string):
    if string == "":
        return 0
    return length_of_string(string[1::]) + 1

def is_palindrome(string):
    string = string.lower()
    string = string.replace(" ", "")

    reversed_str = string[::-1]

    if reversed_str == string:
        return True
    else:
        return False

two_sum_list = [1,2,3,4,5,6,11]
target_sum = 13


def find_two_sum(two_sum_list, target_sum, high = len(two_sum_list) - 1, low = 0):
    while low <= high:
        
        if target_sum == two_sum_list[low] + two_sum_list[high]:
            return True

        if target_sum < two_sum_list[low] + two_sum_list[high]:
            return find_two_sum(two_sum_list, target_sum, high - 1)
        if target_sum > two_sum_list[low] + two_sum_list[high]:
            return find_two_sum(two_sum_list, target_sum, high, low + 1)
        
    
    return False

print(find_two_sum(two_sum_list, target_sum, len(two_sum_list) - 1, 0))

