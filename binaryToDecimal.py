def binaryToDecimal(x):
	rev = str(x)[::-1]
	power = 0
	integer = 0
	while power < len(rev):
		if int(rev[power]) == 1:
			integer += 2**power
		power += 1
	print(integer)
num = input("What is your number?\n")
binaryToDecimal(num)

