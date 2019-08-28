def list_difference(array_x, array_y):
    """
    This function compares values of two lists and return list of unique items from the 1st one.
    :param array_x: user collection 1
    :param array_y: user collection 2
    :type array_x: type depends on input collection(string, list, tuple, etc)
    :type array_y: type depends on input collection(string, list, tuple, etc)
    :return: Function returns list of unique items the 1st collection
    :rtype: return type 'list'
    """
    result_list = []
    for i in array_x:

        if i not in array_y:
            result_list.append(i)

    return result_list


# Checking out

a = list(input('Enter something: '))
b = list(input('Enter something: '))

result = list_difference(a, b)
print(result)
