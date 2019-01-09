import random
def guess():
	target = random.randrange(1, 101)
	user_guess = int(input("Please enter an integer between 1 and 100:\n"))

	while user_guess != target:
		if target == user_guess:
			print ("You got the number correct!")
			break
		if target > user_guess:
			user_guess = int(input("My number is higher than your guess. Try again: \n"))
		if target < user_guess:
			user_guess = int(input("My number is lower than your guess. Try again:  \n"))
	else:
		print (f"Congratulations! {user_guess} was correct.")

guess()