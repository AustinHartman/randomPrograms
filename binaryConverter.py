#Convert decimal to binary with a recursive function
def decimalToBinary(x):

   if x > 1:
       decimalToBinary(x//2)
   print(x % 2, end = "")

number = int(input("What is your number?"))
decimalToBinary(number)