# are each of the character in your string repeats?
# asked another way, does the same letter appear twice in your string?


string1 = "tile"
string2 = "radar"

def is_it_unique(string):
	set_of = set(string) # the set will be unordered, so we can not match every element to every element
	list_of = list(string) # in the list

	if len(set_of) == len(list_of): # However, we do not need to know what the indivudual elements are. The set will
	# discard any repeating letters. So to simply know the length of the list(which, allows repeats) against the length of
	# the set(which doesn't) will tell us all we need to know about whether the set found any repeating elements
		print ("Yes, every element is unique")
	else:
		print ("No, every element is not unique")
