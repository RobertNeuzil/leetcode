import random


def generate_password(characterlength):
	potential_character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?><:"|'
	random_word = 'television'
	empty_str = ''
	for i in range(characterlength):
		empty_str = empty_str + potential_character[random.randrange(len(potential_character))] 
	new_pass = empty_str + random_word
	return new_pass

print (generate_password(28))