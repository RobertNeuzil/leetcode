from functools import lru_cache

@lru_cache(maxsize = 200)
def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

two_sum_list = [1, 9, 22, 500, 10000000, 100000000000000000]
two_sum_target = 31

def two_sum(two_sum_list, two_sum_target, low, high):
    while low <= high:

        if two_sum_target == two_sum_list[low] + two_sum_list[high]:
            return True
        if two_sum_target < two_sum_list[low] + two_sum_list[high]:
            return two_sum(two_sum_list, two_sum_target, low, high - 1)
        if two_sum_target > two_sum_list[low] + two_sum_list[high]:
            return two_sum(two_sum_list, two_sum_target, low + 1, high)

    return False

binary_list = range(1, 101)
binary_target = 14

def binary_search(binary_list, binary_target, low, high):
    while low <= high:
        mid = low + high
    
        if binary_target == binary_list[mid]:
            return True
        if binary_target < binary_list[mid]:
            return binary_search(binary_list, binary_target, low, mid - 1)
        if binary_target > binary_list[mid]:
            return binary_search(binary_list, binary_target, mid + 1, high)

    return False

def fizzbuzz():

    for x in range(1, 1001):
        if x % 25 == 0:
            print ( x,  "Fizzbuzz")

        if x % 5 == 0 and x % 25 != 0:
            print (x , "Fizz")
        if x % 5 != 0:
            print (x)

fizzbuzz()