#  I did the first part as is was writen in the task 3.1
def array_diff_one_way(f_arr, s_arr):
    """
    This function filter list's one way
    (Remove number from f_arr which are present in s_arr)
    :param f_arr: First list
    :param s_arr: Second list
    :type f_arr: list, int
    :type s_arr: list, int
    :return: Filtered list which contains exclusive numbers
    :rtype: list
    """

    arr_filtered = filter(lambda x: x not in s_arr and f_arr, f_arr or s_arr)

    arr = list(arr_filtered)

    # Removes duplicates
    arr_all_duplicate_filter = []
    for i in arr:
        if i not in arr_all_duplicate_filter:
            arr_all_duplicate_filter.append(i)

    return arr_all_duplicate_filter


# As for this one, it was done by following your directions during the lesson
def array_diff_both_way(f_arr, s_arr):
    """
    This function filter list's both ways
    (Add numbers to new list which are not repeated in first list and not in the second)
    :param f_arr: First list
    :param s_arr: Second list
    :type f_arr: list, int
    :type s_arr: list, int
    :return: Filtered list which contains exclusive numbers
    :rtype: list
    """

    f_arr_filtered = list(filter(lambda x: x not in s_arr, f_arr))
    s_arr_filtered = list(filter(lambda x: x not in f_arr, s_arr))

    arr_all = f_arr_filtered + s_arr_filtered

    # Removes duplicates
    arr_all_duplicate_filter = []
    for i in arr_all:
        if i not in arr_all_duplicate_filter:
            arr_all_duplicate_filter.append(i)

    return arr_all_duplicate_filter


# Main menu
print('1.One way like in task on github')
print('2.Both way like im heard on lesson')
print('3.Exit')

button = int(input('Choose version --> '))

first_arr = []
second_arr = []

if button == 1:

    print('If you finish enter -0 in first arr')

    # Creates list from user input
    while True:

        first_arr.append(input('Enter number for first arr --> '))

        if '-0' in first_arr:
            first_arr.remove('-0')
            break

        second_arr.append(input('Enter number for second --> '))

    array = array_diff_one_way(first_arr, second_arr)

    print(array)

elif button == 2:

    print('If you finish enter -0 in first arr')

    # Creates list from user input
    while True:

        first_arr.append(input('Enter number for first arr --> '))

        if '-0' in first_arr:
            first_arr.remove('-0')
            break

        second_arr.append(input('Enter number for second arr --> '))

    array = array_diff_both_way(first_arr, second_arr)

    print(array)

elif button == 3:
    exit('Finish')

else:
    print('Enter correct version')
