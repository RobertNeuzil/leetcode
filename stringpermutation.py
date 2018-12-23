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


def is_it_valid(one, two):
    one = one.replace(' ', '')  # get rid of spaces
    two = two.replace(' ', '')  # get rid of spaces
    # or don't get rid of spaces and treat extra spaces as not valid:
    # in that case, skip line 18 & 19 and they will be evaluated to false at line 25
    if len(one) != len(two):
        return False
    for c in one:
        if c in two:
            two = two.replace(c, "")
    if len(two) == 0:
        return True
    else:
        return False


print(is_it_valid(string_one, string_two))
print(is_it_valid(string_five, string_six))
