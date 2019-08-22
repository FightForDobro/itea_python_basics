def custom_filter(f_list, s_func):
    """
    Simple filter function filters list by another function
    :param f_list: Some list
    :param s_func: Some function
    :return: return s_func
    """

    for element in f_list:
        if s_func(element):
            return s_func



def even_number_finder(num):
    """
    Function decide even number or not
    :param num: Some number
    :return: result of function
    """

    if num % 2 == 0:

        return result_list.append(num)


result_list = []
custom_filter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], even_number_finder)

print(result_list)
