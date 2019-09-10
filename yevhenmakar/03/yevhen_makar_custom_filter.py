def custom_filter(function, iterable):
    """
    This function uses other functions to iterate collections and filtered unnecessary data
    :param function: Function, will be used for iterating in specific term
    :param iterable: Collection, which will be iterated
    :type function: func
    :type iterable: str, list, tuple
    :return: List, iterated with set function
    :rtype: list
    """
    map_list = []

    for i in iterable:
        if function(i):
            map_list.append(i)

    return map_list


# Uncomment for checking this function
'''
first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
second_list = ['1', 'a', '2', 'b', '3', 'c']
third_list = [7, 3, 2, 8, 9, 6, 5, 1, 0]

first_result = custom_filter(lambda x: x % 2, first_list)
print(first_result)

second_result = custom_filter(lambda x: str.isdigit(x), second_list)
print(second_result)

third_result = custom_filter(lambda x: x > 5, third_list)
print(third_result)
'''