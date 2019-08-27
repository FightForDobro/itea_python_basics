def exception_same(a, b):
    """
    This function removes the same values ​​from lists
    :param a: First list
    :param b: Second list
    :type a: list, int
    :type b: list, int
    :return: list items that are not duplicated
    :rtype: list

    """

    for i in a:

            for j in b:

                if  j == i:

                    new_list.remove(i)
                    new_list.remove(i)


list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [4, 5, 6, 7]
new_list = list_a + list_b

exception_same(list_a, list_b)
print (new_list)