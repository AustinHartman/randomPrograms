# Program calculates the amount of change required in min coins

money = float(input("What amount of money do you want the minimum coins to be calulated for: "))

coin_vals = [0.25, 0.1, 0.05, 0.1]
coins = 0

while money > 0:
    print(coins)
    for coin in coin_vals:
        if coin <= money:
            money -= coin
            coins += 1
            break


print(coins)