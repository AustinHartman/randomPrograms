def expDigitSum(x):
    sum = 0
    num = 2 ** x
    digits = []
    digits += str(num)
    for digit in digits:
        sum += int(digit)
    print("Here are all of the individual digits of 2 to the",x,"power:",digits)
    print(sum)

number = int(input("What is your number?\n"))
expDigitSum(number)

