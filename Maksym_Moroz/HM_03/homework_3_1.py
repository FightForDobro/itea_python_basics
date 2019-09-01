def array_diff(list1, list2):
    """ This function  subtracts one list from another and returns the result. It remove all values (all of its occurrences) from list1, which are present in list2
        :param list1: It list from which second list is subtracted
        :param list2: It second list which is subtracted from the first list
        :type list1: list
        :type list2: list
        :return: A new list with deleted values (all its occurrences) from list1, which are present in list2.
        :rtype: list
    """
    counter = 0
    while True:

        new_list = [i for i in list1 if i != list2[0 + counter]]
        counter += 1
        list1 = new_list
        if counter == len(list2):
            break
    return new_list

a = array_diff([2, 3, 4, 5, 6, 4, 4], [2, 3, 4])
print(a)
