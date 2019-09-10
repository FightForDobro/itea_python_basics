def function(x):
    """ This function make an argument to a power 2
        :param x: It is argument argument that make to power 2
        :type x: int
        :return: Return power 2
        :rtype: int
    """
    x = x ** 0.5
    return x

def map1(function, list):
    """ This function filters the list by the value of another function
        :param function: This function sets the value by which the second argument of the function is filtered
        :param list: It's list which is filtered
        :type function: int
        :type list: list
        :return: filtered list
        :rtype: list
    """

    new_list = [i for i in list if function(i).is_integer()]
    return new_list


print(map1(function, [1, 3, 4, 5, 4, 6, 8, 16, 65, 100]))
