def changeCalc():
    change = float(input("How much change do you have? (give two decimals)\n"))

    if change >= 100:
        hundreds = change//100
        change = change - (hundreds * 100)
        print("Hundreds:", int(hundreds))
    if change >= 50:
        fifties = change//50
        change = change - (fifties * 50)
        print("Fifties:", int(fifties))
    if change >= 20:
        twenties = change//20
        change = change - (twenties * 20)
        print("Twenties:", int(twenties))
    if change >= 10:
        tens = change//10
        change = change - (tens * 10)
        print("Tens:", int(tens))
    if change >= 5:
        fives = change//5
        change = change - (fives * 5)
        print("Fives:", int(fives))
    if change >= 1:
        ones = change//1
        change = change - (ones * 1)
        print("Ones:", int(ones))
    if change >= .25:
        quarters = change//.25
        change = change - (quarters * .25)
        print("Quarters:", int(quarters))
    if change >= .10:
        dimes = change//.10
        change = change - (dimes * .10)
        print("Dimes:", int(dimes))
    if change >= .05:
        nickels = change//.05
        change = change - (nickels * .05)
        print("Nickels:", int(nickels))
    if change >= .01:
        pennies = change//.01
        change = change - (pennies * .01)
        print("Pennies:", int(pennies))
    rerun = input("Want to run again?\n")
    if rerun == 'yes':
        changeCalc()
    else:
        exit(0)

changeCalc()
