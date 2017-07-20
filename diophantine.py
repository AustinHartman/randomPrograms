six = 0
nine = 0
twenty = 0
print("Availible in 6, 9, or 20 packs.")
print("Test different combinations to see if they add up.")
originalAmount = int(input("How many do you want to buy?\n"))
amount = originalAmount

while amount >= 20:
    amount = amount - 20
    twenty += 1

while amount >= 9:
    amount = amount - 9
    nine += 1

while amount >= 6:
    amount = amount - 6
    six += 1

print("Twenty:", twenty, "\nNine:", nine, "\nSix:", six)
print("You wanted to by " + str(originalAmount) + ", But you could not buy this many because of sizes:", amount)

