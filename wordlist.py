wordlist = ["cat", "dog", "rabbit"]
letterlist = []

for aword in wordlist:
	for aletter in aword:
		if aletter not in letterlist:
			letterlist.append(aletter)
		else:
			pass
print (letterlist)