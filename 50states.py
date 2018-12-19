'''
In a list of all 50 states, randomly choose a state, 500 times
and write the state to a text file



'''

list_of_fifty = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]



def state_generator(states):
	import random
	number = 500
	f = open('states.txt', 'a')
	for x in range(number):
		state = random.choice(list_of_fifty)
		f.write(state + '\n')
	f.close()
  		

state_generator(list_of_fifty)