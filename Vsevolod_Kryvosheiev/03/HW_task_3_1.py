#
# Home Work
# Vsevolod Kryvosheiev

# Task 3.1 Array difference


def array_diff(main_list, delete_list):
    """This is a difference function, which subtracts one list from another and returns the result.
        It remove all values (all of its occurrences) from list 'main_list', which are present in list delete_list.

    :param main_list: source list of values
    :param delete_list: list of values to be removed from the source list
    :type main_list: list
    :type delete_list: list
    :return: difference list
    :rtype: list
    """

    diff_list = []

    for i in filter(lambda x: not x in delete_list, main_list):

        # delete duplicate values
        if not i in diff_list:
            diff_list.append(i)

    return diff_list


main_user_list = [1, 2, 2, 2, 3, 3, 4, 5]
remove_user_list = [1, 4]

difference_list = array_diff(main_user_list, remove_user_list)
print(difference_list)


