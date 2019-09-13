your_string = input('Enter something: ')
count_x = 0
count_o = 0

for i in your_string:

    if i == 'x' or i == 'X':
        count_x += 1

    if i == 'o' or i == 'O':
        count_o += 1

if count_o == count_x:
    print(True)

else:
    print(False)
