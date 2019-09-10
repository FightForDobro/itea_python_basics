def custom_filter(func, my_list):
    """
    This is custom map function. It contains a predefined function in its inner condition
    to filter items in an established sequence.
    :param func: Any input function, that returns True or False value.
    :param my_list: Any input collection
    :type func: class 'function'
    :type my_list: type depends on input collection(string, list, tuple, etc)
    :return: This function returns list of filtered values.
    :rtype: return type 'list'
    """
    y = []

    for i in range(len(my_list)):

        if func(my_list[i]):
            y.append(my_list[i])

    return y


# Checking out

user_input = input('Enter a number: ')
result = custom_filter(lambda x: x.isalpha(), user_input)
print(result)
