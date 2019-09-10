# Task 3.1 Array difference

def difference(a_list, b_list):
    """
    The function, which subtracts one list from another and returns the result
    :param a_list: The first list which was inserted by user
    :param b_list: The second list which was inserted by user
    :type a_list: list
    :type b_list: list
    :return: The list with numbers which are different
    :rtype: list
    """

    dif_list = [i for i in a_list + b_list if i not in b_list or i not in a_list]

    return dif_list


def creating_the_list(x_list_string):
    """
    The function, which convert inserted strings to the list
    :param x_list_string: The inserted string
    :type x_list_string: str
    :return: The converted string for str to list
    :rtype: list
    """

    x_list = list(map(lambda x: int(x), x_list_string))

    return x_list


first_list = input('Input first list:')
second_list = input('Input second list:')

a_list = creating_the_list(first_list)
b_list = creating_the_list(second_list)

global_dif_list = difference(a_list, b_list)

if global_dif_list != []:
    print('The difference is: \n', global_dif_list)

else:
    print('There is no difference.')