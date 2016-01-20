def binaryToDecimal(x):
	rev = str(x)[::-1]
	power = 0
	integer = 0
	while power < len(rev):
		if int(rev[power]) == 1:
			integer += 2**power
		power += 1
	print(integer)
	repeat = input("Run again?\n")
	if repeat == 'yes':
		num = input("What is your number?\n")
		binaryToDecimal(num)
	else:
		quit(0)
num = input("What is your number?\n")
binaryToDecimal(num)


