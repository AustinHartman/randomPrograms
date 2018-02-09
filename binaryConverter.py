# Convert decimal to binary with a recursive function
def decimal_to_binary(x):

    if x > 1:
        decimal_to_binary(x//2)
    print(x % 2, end='')


def callback():
    repeat = input("\nRun again?\n")
    if repeat == 'yes':
        number = int(input("What is your number?\n"))
        decimal_to_binary(number)
    else:
        quit(0)

callback()




