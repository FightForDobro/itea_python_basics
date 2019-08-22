def custom_map(f_list, s_func):
    """
    Simple map function split list on single elements and add it to some function
    :param f_list: Some list
    :param s_func: Some function
    :return: return s_func
    """

    for element in f_list:
        s_func(element, )

    return s_func


def power_of_two(num, power=2):
    """
    Function power of 2 number
    :param num: Some number
    :param power: Power
    :return:
    """

    result = num * power

    return result_list.append(result)


result_list = []

custom_map([1, 2, 3, 9], power_of_two)

print(result_list)
