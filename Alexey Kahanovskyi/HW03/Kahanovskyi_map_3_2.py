def alex_map(a, b):

    """ This function performs actions of a given function on each element of the collection and returns a new collection
        :param_a: a given function
        :param_b: agiven collection
        :type_a: function
        :type_b: list
        :return: new list with changes made by the specified function(param_a)
        :rtype: list """

    result = a

    return(result)


def function_mult_by_2():

    """ This function for multiplication function by 2
        :return: new list multiply by 2
        :rtype: list """

    my_list_2 = [i*2 for i in my_list]

    return(my_list_2)


from random import randint

my_list = [randint(0,9) for i in range(4)]

res = alex_map(function_mult_by_2() , my_list)

print(' my_list : ' , my_list)
print(' result : ' , res)
