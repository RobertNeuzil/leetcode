import random


def generate_password(characterlength):
	potential_character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?><:"|'
	random_words = [' television', ' cat', ' car', ' message', ' L O S T' ]
	empty_str = ''
	for i in range(characterlength):
		empty_str = empty_str + potential_character[random.randrange(len(potential_character))] 
	new_pass = empty_str + random_words[random.randrange(len(random_words))]
	return new_pass

for n in range(1, 101):
	print (generate_password(28))