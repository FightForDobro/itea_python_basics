# Home Work
# Vsevolod Kryvosheiev

# Task 3.3 Custom filter
# # Implement custom_filter function, which will behave like the original Python filter() function.


def custom_filter(user_filter, arg):
    """ Tis function create new list from souse list filtered elements

    :param user_filter: filter condition
    :param arg: list user arguments
    :type user_filter: function
    :type arg: list
    :return: list of filtered arguments
    :rtype: list
    """

    return [i for i in arg if user_filter(i)]


# example
list_for_filter = [1, 2, 3, 4, 5]
print(custom_filter(lambda x : x % 2 == 0, list_for_filter))
