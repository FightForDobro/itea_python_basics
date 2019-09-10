# Task 3.3 Custom filter


def from_input_to_list(inputted_string):
    """
    The function creates a list from the string
    :param inputted_string: The string which were inputted by the user
    :type inputted_string: string
    :return: The list converted from string
    :rtype: list
    """

    created_list = [int(i) for i in inputted_string]

    return created_list


def any_function(x):
    """
    The function powered the inserted number
    :param x: The integer which will be powered
    :type x: int
    :return: The powered integer
    :rtype: int
    """
    return x ** x   # here we can hardcode any function


def custom_filter(some_func, iterator_list):
    """
    The function that copies filter function but with pre-setted condition and function
    :param some_func: The function which will be executed
    :param iterator_list: The values which will be processed by the function
    :type some_func: function
    :type iterator_list: list
    :return: The list processed by the function
    :rtype: list
    """

    local_iterator = from_input_to_list(iterator_list)
    func_map = [some_func(i) for i in local_iterator]
    true_list = [j for j in func_map if j > 100]  # here we can hardcode any condition

    return true_list


values = input('Input the values:')

print(custom_filter(any_function, values))
