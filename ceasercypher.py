def ceaser_cypher(cleartext):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	cleartext = cleartext.upper()
	cyphertext = ''
	for xox in cleartext:
		if xox in alphabet:
			xox_pos = alphabet.find(xox)
			new_pos = (xox_pos + 13) % 26
			cyphertext += alphabet[new_pos]
	
		else:
			cyphertext += xox
	return cyphertext
ceaser = ceaser_cypher("helloworld")
print (ceaser)