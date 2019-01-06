import random
def generateone(strlen):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	res = ""
	for i in range(strlen):
		res = res + alphabet[random.randrange(26)]
	return res

def score(goal, teststring):
	numsame = 0
	for i in range(len(goal)):
		if goal[i] == teststring[i]:
			numsame = numsame + 1
	return numsame / len(goal)

def main():

	goalstring = 'catt'
	newstring = generateone(4)
	best = 0
	newscore = score(goalstring, newstring)
	while newscore < 1:
		if newscore >= best:
			print (newscore, newstring)
			best = newscore
		newstring = generateone(4)
		newscore = score(goalstring, newstring)
	if newscore == 1:
		print (newstring)
main()
