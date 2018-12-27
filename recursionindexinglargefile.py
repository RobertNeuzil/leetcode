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
            print (f"{target} is part of the list")
            return True
        if binary_list[middle] < target:
            return binary_recursive(binary_list, target, high, low + 1)
        if binary_list[middle] > target:
            return binary_recursive(binary_list, target, mid - 1, low)
    print (f"{target} is not an element in the list")
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
            print (f"{two_sum_list[high]} and {two_sum_list[low]} add up to {two_sum_target} ")
            return True
        if two_sum_target < two_sum_list[high] + two_sum_list[low]:
            return find_two_sum(two_sum_target, two_sum_list, high - 1, low)
        if two_sum_target > two_sum_list[high] + two_sum_list[low]:
            return find_two_sum(two_sum_target, two_sum_list, high, low + 1)
    print ("None of the items in the list can be added together to reach the target value")
    return False

find_two_sum(12, two_sum_list, len(two_sum_list) - 1, 0)


