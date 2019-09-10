# Task 2.3 - Find the odd int

given_list = [1, 2, 3, 1, 3, 2, 1]

for i in given_list:

    counter = 0

    for j in given_list:

        if i == j:

            counter += 1

    if counter % 2 != 0:

        print('The odd number is: \n', i)

    else:

        print('There is no odd number!')

    break
