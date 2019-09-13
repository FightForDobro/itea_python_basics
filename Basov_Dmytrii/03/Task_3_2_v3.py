def custom_map(func, *arguments):
    """
    This is the 2nd version of custom map function. It can handle with multiple input arguments.
    :param func: Any input function.
    :param arguments: iterable collections, where the 1st is the smallest.
    :type func: class 'function'
    :type arguments: type depends on input collection(string, list, tuple, etc)
    :return: The function returns list of result items
    :rtype: return type 'list'
    """
    args_amount = len(arguments)
    print(args_amount)                      # Not necessary to execute. Just for checking out

# Exception condition

    if args_amount == 0:
        print("No arguments")
        return func()

# Body of function

    result = []                             # Initial empty resulting list

    for i in range(len(arguments[0])):      # Iterate on the 1st argument
        arr_j = []                          # Initial list for items with the same indexes in different arguments

        for j in range(args_amount):        # Iterate on input argument indexes
            arr = arguments[j]
            arr_j.append(arr[i])            # Add in list each i item every j argument

        print('\nInput values to be handled by function', arr_j)   # Not necessary to execute. Just for checking out

        x = func(*arr_j)                    # Action on every item
        result.append(x)                    # Filling of resulting list
        print('Your result is: ', result)
    return result


# Checking out with integer lists

my_list = [1, 2, 3, 4]
my_list_2 = [2, 4, 5, 8, 9]
result_int = custom_map(lambda x, y: float(x + y), my_list, my_list_2)
print(result_int)

# Checking out with string

my_str = input('\nThe 1st string argument: ')
my_str_2 = input('\nThe 2nd string argument: ')
result_str = custom_map(lambda s1, s2: s1 + s2, my_str, my_str_2)
