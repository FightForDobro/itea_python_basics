def list_vs_list(first_list, second_list):
    """
        This function removes the same symbol from two lists
        :param first_list: First list
        :param second_list: Second list
        :type first_list: list
        :type second_list: list
        :return: summ of unique symbol of two lists
        :rtype: list
    """

    # find unique symbol in first list
    diff_first_list = [i for i in first_list if i not in second_list]

    # find unique symbol in second list
    diff_second_list = [i for i in second_list if i not in first_list]

    # semm of unique
    return diff_first_list + diff_second_list


# input first list symbol
first_list = list(input('Enter symbols: '))

# input second list symbol
second_list = list(input('Enter symbols: '))

# call the function and pass 2 parameters
print(list_vs_list(first_list, second_list))

