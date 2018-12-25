def is_divisible(num, den):
	return num % den == 0


def make_is_divisible(den):

	def is_divisible(num):
		return num % den == 0

	return is_divisible

is_div_2 = make_is_divisible(2)


print(
is_div_2(3), is_div_2(4), 
is_div_2(7), is_div_2(18)
)

print (make_is_divisible(5)(155))