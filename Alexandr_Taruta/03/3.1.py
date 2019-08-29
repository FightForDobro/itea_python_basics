first_list = [i for i in input('Enter numbers you would like to add in the first list: ').split()]
second_list = [i for i in input('Enter numbers you would like to add in the second list :').split()]


def list_of_unique_items(first_list, second_list):
    """ This function returns unique values from two lists
     :param first_list: First list which sets be user
     :param second_list: Second list which sets by user
     :type first_list: list
     :type second_list: list
     :return: Returns new list with unique values
     :rtype: list """

    counter = 0
    new_list_v1 = []
    new_list_v2 = []
    for value in first_list:
        for value_1 in second_list:
            if value not in second_list:
                new_list_v1.append(value)

    for value_1 in second_list:
        for value in first_list:
            if value_1 not in first_list:
                new_list_v1.append(value_1)
    for i in new_list_v1:
        if i not in new_list_v2:
            new_list_v2.append(i)

    return new_list_v2




new_list = list_of_unique_items(first_list, second_list)
print(new_list)
