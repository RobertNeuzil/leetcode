def logic_and (a, b):
	if a == 1 and b == 1:
		return 1
	else:
		return 0

def logic_or (a, b):
	if a == 1 or b == 1:
		return 1
	else:
		return False

def logic_not (a):
	if a == 1:
		return False
	if a == 0:
		return True

def logic_nand(a, b):
	if a == 1 and b == 1:
		return False
	else:
		return True

print(logic_and(1, 0))