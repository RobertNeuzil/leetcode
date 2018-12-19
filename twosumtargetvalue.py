# YouTube Video: https://www.youtube.com/watch?v=gCin6Qz-eJQ
# Given an array of integers, return the two numbers such that they add up to
# a specific target. You may assume that each input would have exactly one
# solution, and you may not use the same element twice.

A = [-2, 1, 2, 4, 7, 11]
target = 20

"""

def two_sum_brute_force(A, target):
    for i in range(len(A)-1):  # range(0, 5) 0,1,2,3,4
        for j in range(i+1, len(A)): # range(1, 6) range(2, 6) range(3, 6) range(4, 6) range(5, 6)
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
    return False
print (two_sum_brute_force(A, target))

"""

for i in range(len(A)-1):
	for j in range(i+1, len(A)):
		print (j + 10)