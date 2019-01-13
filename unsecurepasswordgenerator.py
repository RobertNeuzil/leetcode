import random

def generate_password(characterlength):
	potential_character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?><:"|'
	
	random_words = [' television', ' cat', ' car', ' message', ' L O S T', 'newspaper', 'fridge', 
	'walkietalkie', 'umbrella', 'coat hanger', 'washing machine', 
	'currency', 'alabama', 'free firewood', 'eminem', 'soy farm', 'laptop', 'messaging service', 'car wash' ]
	
	empty_str = ''
	
	for i in range(characterlength):
		empty_str = empty_str + potential_character[random.randrange(len(potential_character))] 
	new_pass = empty_str + random_words[random.randrange(len(random_words))]
	return new_pass + "\n"

file = open("randompass.txt", "a")

for n in range(1, 201):
	file.write(generate_password(28),)
file.close()