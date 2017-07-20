#Convert decimal to binary with a recursive function
def decimalToBinary(x):

    if x > 1:
        decimalToBinary(x//2)
    print(x % 2, end = '')


def callback():
    repeat = input("\nRun again?\n")
    if repeat == 'yes':
        number = int(input("What is your number?\n"))
        decimalToBinary(number)
    else:
        quit(0)

#number = int(input("What is your number?\n"))
#decimalToBinary(number)
#callback()



