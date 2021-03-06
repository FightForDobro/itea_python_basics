def custom_map(s_func, f_list):
    """
    Simple map function split collection on single elements and add it to some function
    :param f_list: Some list
    :param s_func: Some function
    :type f_list: iterable collection
    :type s_func: func
    :return: return result
    :rtype: list
    """
    result = []

    for element in f_list:
        result.append(s_func(element, ))

    return result


def power_of_two(num, power=2):
    """
    Function power of 2 number
    :param num: Some number
    :param power: Power
    :type num: int
    :type power: int
    :return: num in power
    :rtype: int
    """

    return num ** power


numbers = [1, 2, 3, 9]

some_string = 'Hello'

result = custom_map(power_of_two, numbers)  # Использовать lambda чтобы менять повер

result_lambda = custom_map(lambda x: x * 2, some_string)

print(f'Result using func: {result}\n')
print(f'Result using lambda: {result_lambda}')

