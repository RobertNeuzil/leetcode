from functools import lru_cache

"""
perform a binary search of a list
"""

binary_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#target = 13


def binary(binary_list, target):
    for x in binary_list:
        if x == target:
            return True
    return False


def binary_recursive(binary_list, target, high, low):
    while low <= high:
        middle = (low + high) // 2

        if binary_list[middle] == target:
            print(f"{target} is part of the list")
            return True
        if binary_list[middle] < target:
            return binary_recursive(binary_list, target, high, low + 1)
        if binary_list[middle] > target:
            return binary_recursive(binary_list, target, mid - 1, low)
    print(f"{target} is not an element in the list")
    return False

#binary_recursive(binary_list, 2222222222222222, len(binary_list) - 1, 0)


string = "robertNeuzil"


def find_upper(string):
    index = 0
    while index <= len(string):
        for x in string:
            if x[index].isupper():
                return x
        else:
            index += 1
    return False


two_sum_list = [3, 4, 9, 11, 13]
two_sum_target = 12


def find_two_sum(two_sum_target, two_sum_list, high, low):
    while low <= high:
        if two_sum_list[high] + two_sum_list[low] == two_sum_target:
            print(
                f"{two_sum_list[high]} and {two_sum_list[low]} add up to {two_sum_target} ")
            return True
        if two_sum_target < two_sum_list[high] + two_sum_list[low]:
            return find_two_sum(two_sum_target, two_sum_list, high - 1, low)
        if two_sum_target > two_sum_list[high] + two_sum_list[low]:
            return find_two_sum(two_sum_target, two_sum_list, high, low + 1)
    print("None of the items in the list can be added together to reach the target value")
    return False

#find_two_sum(12, two_sum_list, len(two_sum_list) - 1, 0)


string_two_two = "A Toyota! Race fast, safe car! A Toyota!"

string_two_three = """ The last two episodes of 'How I met Your Mother' should have been the final season. While the 
plot of the first twenty episodes should have been one episode """


def is_palindrome(string):
    string = string.lower()
    string = string.replace(" ", "")
    string = string.replace("!", "")
    string = string.replace(",", "")

    if string == string[::-1]:
        return True
    return False

# print(is_palindrome(string_two_two))
# print(is_palindrome(string_two_three))


string_with_unkown_length = """jakslfjsdlkfjslkdfjskldfjlkesj
flkerjflksfjklsfjkslfjskljfskljasijwei
ofjifheriofjioefjerfjioefr"""

# I'm pretty sure this algorithim is entirely useless for
# optimzing time or space complexity
# nonetheless, here it is


def length_of_string(string):
    if string == "":
        return 0

    return length_of_string(string[1::]) + 1

# print(length_of_string(string_with_unkown_length))


cap_letter_string = "skdjlksjdsdjfksljfdlkfjsldkfjdkKKKKKKKKKKLMNOOPOS"


def find_upper_recursive(string, index=0):
    if string[index].isupper():
        return string[index]
    if index == len(string) - 1:
        return "None Found"
    return find_upper_recursive(string, index + 1)


# print(find_upper_recursive(cap_letter_string))


not_unique = "unique"
unique = "bear"


def all_unique(string):
    set_string = set(string)
    list_string = list(string)
    if len(set_string) == len(list_string):
        return True

    return False

# print(all_unique(not_unique))


def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0:
            print("fizzbuzz")

        if x % 5 == 0:
            print("fizz")

        else:
            print(x)
# fizzbuzz()

@lru_cache(maxsize = 1000)
def fibonacci_cache(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)







# YouTube Video: https://www.youtube.com/watch?v=0gkWZNE1H4Y&list=PL5tcWHG-UPH1kjiE-Fqt1xCSkcwyfn2Jb
"""
Given an array of sorted integers. We need to find the closest value to the 
given number.
Array may contain duplicate values and negative numbers.
Examples:
    Input : arr[] = {1, 2, 4, 5, 6, 6, 8, 9}
    Target number = 11
    Output : 9
    9 is closest to 11 in given array
    Input :arr[] = {2, 5, 6, 7, 8, 8, 9};
    Target number = 4
    Output : 5
"""

A = [1, 2, 4, 5, 6, 6, 8, 9]
A = [2, 5, 6, 7, 8, 8, 9]


def find_closest_num(A, target):
    min_diff = float("inf")
    low = 0
    high = len(A) - 1
    closest_num = None

    # Edge cases for empty list of list
    # with only one element:
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]

    while low <= high:
        mid = (low + high)//2

        # Ensure you do not read beyond the bounds
        # of the list.
        if mid+1 < len(A):
            min_diff_right = abs(A[mid + 1] - target)
        if mid > 0:
            min_diff_left = abs(A[mid - 1] - target)

        # Check if the absolute value between left
        # and right elements are smaller than any
        # seen prior.
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = A[mid - 1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = A[mid + 1]

        # Move the mid-point appropriately as is done
        # via binary search.
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        # If the element itself is the target, the closest
        # number to it is itself. Return the number.
        else:
            return A[mid]
    return closest_num


y = find_closest_num(A, 4)
print(y)