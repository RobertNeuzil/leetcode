import random

def generateone(strlen):
	alphabet = "abcdefghijklmnopqrstuvwxyz "
	res = ""
	for i in range(strlen):
		res = res + alphabet[random.randrange(len(alphabet))]
	return res

def score(goal, teststring):
	numsame = 0
	for i in range(len(goal)):
		if goal[i] == teststring[i]:
			numsame = numsame + 1
	return numsame / len(goal)

def main():
	goalstring = 'methinks it'
	newstring = generateone(11)
	best = 0
	count = 0
	newscore = score(goalstring, newstring)
	while newscore < 1:
		if newscore > best:
			#print (newscore, newstring)
			best = newscore
		newstring = generateone(11)
		newscore = score(goalstring, newstring)
		count += 1
		if count % 100000 == 0:
			print (newscore, newstring, count)
main()