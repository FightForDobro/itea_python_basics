# Task 3.2 Custom map


def any_function(x):
    """
    The function powered the inserted number
    :param x: The integer which will be powered
    :type x: int
    :return: The powered integer
    :rtype: int
    """
    return x ** x   # here we can hardcode any function


def custom_map(some_func, iterator_list):
    """
    The function will process each element of the list with inserted function (some_func)
    :param some_func: The function which will be executed
    :param iterator_list: The values which will be processed by the function
    :type some_func: function
    :type iterator_list: list
    :return: The list processed by the function
    :rtype: list
    """

    local_iterator = [int(i) for i in iterator_list]
    func_map = [some_func(i) for i in local_iterator]

    return func_map


values = input('Input the values:')

print(custom_map(any_function, values))