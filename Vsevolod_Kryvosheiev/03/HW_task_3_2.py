# Home Work
# Vsevolod Kryvosheiev

# Task 3.2 Implement custom_map function, which will behave like the original Python map() function.


def custom_map(function, arg):
    """This function returned new list created from user list and function

    :param function: user function for new list
    :param arg: source list
    :type function: function
    :type arg: list
    :return: new list from user list and function for it
    :rtype: list
    """

    return [function(x) for x in arg]


# example
list_for_ = [1, 'r', 2.0]
print(custom_map(str, list_for_))
