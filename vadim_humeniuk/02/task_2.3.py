number_list = [2, 4, 6, 1, 3, 5, 6, 4, 2, 5, 3, 1, 6]   # last number in list is odd number

for i in number_list:

    counter = 0

    for q in number_list:

        if q == i:

            counter += 1

    if counter % 2:
        print('Odd number is ', i)
        break
