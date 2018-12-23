
# YouTube Video: https://www.youtube.com/watch?v=gCin6Qz-eJQ
# Given an array of integers, return the two numbers such that they add up to
# a specific target. You may assume that each input would have exactly one
# solution, and you may not use the same element twice.

A = [2, 1, -2, 4, 7, 11]
target = 13


def brute_force(A, target):
	for i in range(len(A)):
		for j in range(i + 1, len(A)):
			if A[i] + A[j] == target:
				print (f'The elements {A[i]} and {A[j]} add up to {target}')

brute_force(A, target)