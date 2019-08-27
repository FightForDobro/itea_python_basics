list_one = [4, 5, 2, 9, 3, 3, 2, 4, 9, 1, 1, 5, 5]

while True:

    new_list2 = [i for i in list_one if list_one[0] == i]
    new_list = [i for i in list_one if list_one[0] != i]

    list_one = new_list

    if len(new_list2) % 2 == 1:

        print("Odd number is", new_list2[0])

        break









