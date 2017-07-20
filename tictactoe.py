game = ['0','0','0','0','0','0','0','0','0']

print('-------------')
print('|', game[0], '|', game[1], '|', game[2], '|')
print('|', game[3], '|', game[4], '|', game[5], '|')
print('|', game[6], '|', game[7], '|', game[8], '|')
print('-------------')

turn = 'x'
column = input("Which column?")
row = input("Which row?")

if (row == 1 and column == 1 and (game[0] == '0')):
    game[0] == turn
if (row == 1 and column == 2 and (game[1] == '0')):
    game[1] == turn
if (row == 1 and column == 3 and (game[2] == '0')):
    game[2] == 'x'
if (row == 2 and column == 1 and (game[3] == '0')):
    game[3] == 'x'
if (row == 2 and column == 2 and (game[4] == '0')):
    game[4] == turn
if (row == 2 and column == 3 and (game[5] == '0')):
    game[5] == turn
if (row == 3 and column == 1 and (game[6] == '0')):
    game[6] == turn
if (row == 3 and column == 2 and (game[7] == '0')):
    game[7] == turn
if (row == 3 and column == 3 and (game[8] == '0')):
    game[8] == turn

print('-------------')
print('|', game[0], '|', game[1], '|', game[2], '|')
print('|', game[3], '|', game[4], '|', game[5], '|')
print('|', game[6], '|', game[7], '|', game[8], '|')
print('-------------')