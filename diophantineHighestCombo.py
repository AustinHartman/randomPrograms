print("This program will search to see what the max combination of burgers")
print("buy in 6, 9, or 20 packs that will be less than the upper limit.")
maxLimitOriginal = int(input("What is the upper limit?\n"))
maxLimit = maxLimitOriginal

while maxLimit >= 20:
    maxLimit = maxLimit - 20

while maxLimit >= 9:
    maxLimit = maxLimit - 9

while maxLimit >= 6:
    maxLimit = maxLimit - 6

if maxLimit == 0:
    print("The max limit of " + str(maxLimitOriginal) + " burgers is purchasable \nwith pack sizes of 20, 6, and 9.")
else:
    mostBurgers = maxLimitOriginal - maxLimit
    print("At most, you can buy " + str(mostBurgers) + " burgers")