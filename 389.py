'''

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.


Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.

'''

s = "abcd"
t = "abcdefghi"

s_list = [x for x in s]
t_list = [y for y in t]
difference = (set(s_list) & set(t_list))


for c in t_list:
	if c not in difference:
		print (c)






