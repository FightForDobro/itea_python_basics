def custom_map (function, parametrs):
    """
    This function applies the function to the entire list of items.
    :param a: function
    :param b: list
    :type function: function
    :type parametrs: an object
    :return: object after applying the function
    :rtype: list
    """

    result = []

    for i in parametrs:
        result.append(function(i))

    return result

