from functools import lru_cache


def binary_search(my_list, target, low, high):

    while low <= high:
        mid = (low + high) // 2

        if target == my_list[mid]:
            return True
        if target < my_list[mid]:
            return binary_search(my_list, target, low, mid - 1)
        if target > my_list[mid]:
            return binary_search(my_list, target, mid + 1, high)
    return False

two_sum_list = [1, 2, 5, 9, 11, 1000000]
target = 20

def find_two_sum(two_sum_list, target, high, low):
    while low <= high:
        

        if two_sum_list[high] + two_sum_list[low] == target:
            print (two_sum_list[high], "and", two_sum_list[low], f"are equal to {target}")
            return True
        if two_sum_list[high] + two_sum_list[low] < target:
            return find_two_sum(two_sum_list, target, high, low + 1)
        if two_sum_list[high] + two_sum_list[low] > target:
            return find_two_sum(two_sum_list, target, high - 1, low)
    print ("The elements of the list do not add up to the target")
    return False


@lru_cache(maxsize = 11111)
def f(n):

    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)

for x in range (1, 101):
    print(x, "::::", f(x))
