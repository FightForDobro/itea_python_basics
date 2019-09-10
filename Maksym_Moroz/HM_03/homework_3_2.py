def function(x):
    """ This function add number 4 to the argument using concatenation.
        :param x: It is argument to which the number 4 is added
        :type x: str
        :return: Return a string with the added number 4 using concatenation
        :rtype: str
    """
    x = x + "4"
    return x

def map1(function, list):
    """ This function make adds to each element in the list a value that is set using another function
        :param function: This function sets a value that adds to each item in the list
        :param list: It list to which value is added
        :type function: str
        :type list: list
        :return: A new list with added function value
        :rtype: list
    """

    new_list = [function(i) for i in list]
    return new_list


print(map1(function, "abcdf"))
