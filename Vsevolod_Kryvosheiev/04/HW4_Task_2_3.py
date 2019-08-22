# Home Work 4
# Vsevolod Kryvosheiev

# Task 2.3 - Find the odd int
# Given an array, find the int that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.

checed_list = [2, 2, 3, 2, 3, 2, 2]

for i in checed_list:

    sum_ellement = 0

    for j in checed_list:

        if j == i:
            sum_ellement += 1

    if sum_ellement % 2:

        print(" Odd quatity simbol: ", i, 'q-ty', sum_ellement)
        break
