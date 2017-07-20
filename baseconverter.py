def num_base_convert(num, base):
    power = 1
    converted_number = ''
    multiplier = 0
    if base < 2:
        return print("Not happening")
    while base ** power < num:
        power += 1
        print(power)
    while num > 0:
        if base ** power <= num:
            multiplier = int(num / (base ** power))
            num -= multiplier * base ** power
            converted_number += str(multiplier)
            power -= 1
        else:
            if len(converted_number) > 0:
                converted_number += '0'
            power -= 1
    print(converted_number)

def run():
    repeat = input("\nRun base converter?\n")
    if repeat == 'yes':
        n = int(input("What is your number?\n"))
        b = int(input("What is the base you want to convert to?\n"))
        num_base_convert(n, b)
        run()
    else:
        quit(0)

run()
