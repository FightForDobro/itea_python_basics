random_list = list(input('Enter please numbers: '))

counter = 0

for i in random_list:

    counter = 0

    for j in random_list:

        if i == j:
            counter += 1

    if counter % 2:
        print('This number is appear odd times: ', i)
        break