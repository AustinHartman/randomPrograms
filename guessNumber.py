import random
from sys import exit
def guessNumber():
    print("This is a guessing game the number is 0 to 25")
    guess = int(input("What is your guess?\n"))
    number = random.randint(0,25)
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


