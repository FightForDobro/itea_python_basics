def my_map(func, iterable):
    """Function which applies this function to each element of the list, returning a list of results.
    :param func: function that will be applied to each element from the iterable object
    :param iterable: iterable object
    :type func: function
    :type iterable: list
    :return: returns the processed list
    :rtype: list
    """

    for i in iterable:
        yield func(i)  # I just google it i mean 'yield' because if i
        # choose 'return' it works only with one element from list


my_list = [i * 3 for i in range(1, 10)]
print(my_list)


def do_power(number, power=2):
    number **= power
    return number





result = list(my_map(do_power, my_list))

print(result)