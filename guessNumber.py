import random
from sys import exit
def guessNumber():
    low = int(input("What is the low value?"))
    high = int(input("What is the high value?"))
    print("This is a guessing game the number is", low, "to", high)
    guess = int(input("What is your guess?\n"))
    number = random.randint(low, high)
    while guess != number:
        if guess > number:
            print("Too high.")
            guess = int(input(""))
        else:
            print("Too low.")
            guess = int(input(""))

    if guess == number:
        finish = input("That is the correct number. Play again: y / n\n")

    if finish == "y":
        guessNumber()
    else:
        exit(0)

guessNumber()


