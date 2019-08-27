def custom_filter(s_func, f_list):
    """
    Simple filter function filters collection by another function
    :param f_list: Some list
    :param s_func: Some function
    :type f_list: iterable
    :type s_func: func
    :return: return result of function
    :rtype: list
    """
    result_in_func = []

    for element in f_list:

        if s_func(element):

            result_in_func.append(element)

    return result_in_func


def even_number_finder(num):
    """
    Function decide even number or not
    :param num: Some number
    :type num: int
    :return: result of function
    :rtype: int
    """

    if num % 2 == 0:

        return num


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
some_string = 'hello'

result = custom_filter(even_number_finder, numbers)

result_lambda = custom_filter(lambda x: x == 'l', some_string)

print(f'Result using func: {result}\n')
print(f'Result using lambda: {result_lambda}')
