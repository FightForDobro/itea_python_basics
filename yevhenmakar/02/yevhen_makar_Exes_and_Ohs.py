first_string = input('Enter please string: ')


if 'x' and 'o' not in first_string:

    print('True')

else:

    count_x = 0
    count_y = 0

    for i in first_string:

        if i == 'x' or 'X':
            count_x += 1

        if i == "o" or 'O':
            count_y += 1

    if count_x == count_y:
        print('True')

    else:
        print('False')
