"""
This code finds the int that appears an odd number of times in an array. There will always be only one integer that appears an odd number of times.
"""

# a = [4, 9, 1, 1, 2, 3, 2, 4, 8, 9, 9, 4, 4, 9, 3, 8, 7]

a = []
e = input('Do you want to add a number to list: y/n\n')

if e == 'y':

    while e == 'y':

        d = int(input('Enter a number: '))
        a.append(d)
        e = input('Do you want to add a number to list: y/n\n')

print(a)
c = []

for i in a:

    count = 0

    for j in a:

        if j == i:
            count += 1

    c.append(count)

print(c)
d = len(c)

for k in range(d):

    if c[k] % 2:
        print('\n', a[k])
        break


