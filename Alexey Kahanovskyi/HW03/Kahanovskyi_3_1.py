def subtraction_list(a , b):

    """ This function to sabtract two lists
      :param_1: the first given list
      :param_2: the second given list
      :type_1: list
      :type_2: list
      :return: new list consisting of elements of the first given list(param_1)
      :rtype: list """

    c = [i for i in list_a if i not in list_b]

    return(c)


from random import randint

list_a = [randint(0,9) for i in range(5)]
list_b = [randint(0,9) for i in range(5)]


print(' list_a : ' , list_a)
print(' list_b : ' , list_b)

result = subtraction_list(list_a , list_b)

print(' result : ' , result)