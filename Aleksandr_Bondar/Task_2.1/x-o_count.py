print('The program counts amount "x" and "o" in entered string. Result is boolean\n')

string = input('enter the sting: ')

x_count = 0
o_count = 0

for i in string:

    if i == 'x' or i == 'X':
        x_count = x_count + 1
        
    elif i == 'o' or i == 'O':
        o_count = o_count + 1

    else:
        continue

print(x_count == o_count)

print('\nTHE END')


