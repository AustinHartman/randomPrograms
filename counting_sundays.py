year = 1900
sundays = 0
day = 7

first_day = [1, 32, 60, 91, 121, 152, 182,
             213, 244, 274, 305, 335]

first_day_ly = [1, 32, 61, 92, 122, 153,
                183, 214, 245, 275, 306,
                336]


def is_ly(y):
    if y % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return False
    else:
        return True


while day <= 36525:
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        for d in first_day:
            if d == day:
                sundays += 1
                break
    else:
        for d in first_day_ly:
            if d == day:
                sundays += 1
                break

    if day > (first_day[-1] and first_day_ly[-1]):
        for pos in range(0, len(first_day)):
            if is_ly(year + 1):
                first_day[pos] += 366
                first_day_ly[pos] += 366
            else:
                first_day[pos] += 365
                first_day_ly[pos] += 365
        year += 1
    day += 7


print(sundays)
print(day, year)


