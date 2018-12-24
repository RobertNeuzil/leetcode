'''
A permutation == is a reording of a string that includes all the letters of the original string,
even if they are not in the same order.
input: "television"
output : "eltevision", "noisivelet"     are both valid.
output : "televis" is not valid
write a function to decide whether one string is a valid permutation of the other
'''

string_one = 'television'
string_two = 'televisino'
string_three = 'the cow jumps over the moon'
string_four = 'the         moon jumps o v e r theco     w'
string_five = "It was a long and windy road"
string_six = "I went to mcdonald's and got a hamburger and a kid's toy"


def check_perm(one, two):
    one = one.lower()
    two = two.lower()
    one = one.replace(" ", "")
    two = two.replace(" ", "")

    if len(one) != len(two):
        return False    

    for x in one:
        if x in two:
            two = two.replace(x, "")

    if len(two) == 0:
        return True
    else:
        return False

print (check_perm(string_three, string_four))
print (check_perm(string_five, string_six))