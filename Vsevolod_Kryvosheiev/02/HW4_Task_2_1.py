# Home Work 4
# Vsevolod Kryvosheiev
# Task 2.1 - Exes and Ohs
# Check to see if a string has the same amount of 'x's and 'o's. The string can contain any char.

checked_char = input('Enter your char: ')

count_o = 0
count_x = 0

for i in checked_char:

    if i in ['o', 'O']:
        count_o += 1

    if i in ['x', 'X']:
        count_x +=1

print(count_x == count_o)
