list_to_filter = list(i for i in input('Enter your list').split())
fuck_list = ['fuck']


def my_filter(func, iterable):
    """
     This function uses other functions to iterate collections and filtered unnecessary data
     :param func: Function, will be used for iterating in specific term
     :param iterable: Collection, which will be iterated
     :type func: func
     :type iterable: str, list, tuple
     :return: List, iterated with set function
     :rtype: list
     """
    result_list = []
    for i in iterable:
        if func(i):
            result_list.append(i)
    return result_list


result_list = list(my_filter(lambda i: i not in fuck_list, list_to_filter))
print(result_list)