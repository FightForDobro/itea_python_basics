def array_differentiation(first_list, second_list):

    """
    This function differentiate two lists and make one another with unique symbols
    :param first_list: First list whose symbols will be added to unique list if they are not presented in second list
    :param second_list: Second list whose symbols will be added to unique list if they are not presented in first list
    :type first_list: list
    :type second_list: list
    :return: Will be returned list with unique symbols
    :rtype: list
    """

    unique_list = []

    for i in first_list:

        if i not in second_list:
            unique_list.append(i)

    for j in second_list:

        if j not in first_list:
            unique_list.append(j)

    return unique_list


#Uncomment for checking this function
# first_example_list = list(input('Enter symbols: '))
# second_example_list = list(input('Enter symbols: '))
#
# result = array_differentiation(first_example_list, second_example_list)
#
# print(result)