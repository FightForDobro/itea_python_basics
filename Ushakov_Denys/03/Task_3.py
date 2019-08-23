def custom_map(f_list, s_func):  # добавить масив сюда в которйо будет записывать резулятат выполения
    """
    Simple map function split list on single elements and add it to some function
    :param f_list: Some list
    :param s_func: Some function
    :return: return result
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
    :return: num in power
    """

    return num * power


result = custom_map([1, 2, 3, 9], power_of_two)  # Использовать lambda чтобы менять повер

print(result)

