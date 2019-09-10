def alex_filter(a, b):

    """ This function filters the collection according to the condition specified by the function
        :param_a: a given function(filtring conditions)
        :param_b: agiven collection
        :type_a: function
        :type_b: list
        :return: new list with changes made by the specified function(param_a)
        :rtype: list """

    result = a

    return (result)


def function_chet():

    """ This function is parity check
        :return: new list (only even elements)
        :rtype: list """

    my_list_2 = [i for i in my_list if i % 2 == 0]

    return(my_list_2)


from random import randint

my_list = [randint(0,9) for i in range(6)]

result = alex_filter(function_chet() , my_list)

print(' my_list : ' , my_list)
print(' filter_result : ' , result)
