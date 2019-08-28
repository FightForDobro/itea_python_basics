def custom_map(func, input_list):
    """
    This is custom map function. It makes a predefined action on each item of input sequence.
    :param func: Any input function, that could be applied to collection.
    :param input_list: iterable collection
    :type func: class 'function'
    :type input_list: type depends on input collection(string, list, tuple, etc)
    :return: This function returns list of result items
    :rtype: return type 'list'
    """
    result = []
    for i in range(len(input_list)):

        result.append(func(input_list[i]))

    return result


# Checking out with string

user_input = input('Enter any collection: ')
test = custom_map(lambda x: x * 5, user_input)
print(test)

# Checking out with integer

integer_list = [1, 2, 3, 4, 5]
test_2 = custom_map(lambda x: x * x, integer_list)
print(integer_list)
print(test_2)

# Checking out with tuple

user_tuple = ([1, 2], [3, 4])
test_3 = custom_map(lambda x: x * 2, user_tuple)
print(user_tuple)
print(test_3)
