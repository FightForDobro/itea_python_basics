def custom_map(function, iterable):
    """
    This function uses other functions to iterate collections
    :param function: Function, will be used for iterating
    :param iterable: Collection, which will be iterated
    :type function: func
    :type iterable: str, list, tuple
    :return: List, iterated with set function
    :rtype: list
    """
    map_list = []

    for i in iterable:
        map_list.append(function(i))

    return map_list



# Uncomment for checking this function
'''
integer_list = [1, 2, 3,]
string_list = ['1', '2', '3']
own_list = [4, 81, 144]

first_result = custom_map(str, integer_list)
print(first_result)

second_result = custom_map(int, string_list)
print(second_result)

third_result = custom_map(lambda x: x ** 0.5, own_list)
print(third_result)
'''