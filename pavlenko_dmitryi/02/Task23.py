list = [1, 2, 3, 1, 3, 2, 1]
result = 0

for i in list:

    counter = 0

    for j in list:

        if i == j:

            counter += 1

    if counter % 2 != 0:

        result = j


print (result)