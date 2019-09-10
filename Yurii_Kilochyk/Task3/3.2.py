
# Task 3.2 Custom map

"""
This function executes input functions with iterable values.
:param func: input function
:type func: function
:param iterable: list of elements which will be fed to the input of the function
:type iterable: list
:return: return is a list that contains iterable values processed by the function
:rtype: list
"""

def my_map(func, iterable):
    return [func(i) for i in iterable] 

"""
 Input functions for example
"""
def upper(string):
    return string.upper()

def sqr(number):
    return number * 2

my_iter = ['one', 'two', 'three']
my_number = [1, 2, 3]

s_map = my_map(upper, my_iter)
n_map = my_map(sqr, my_number)

print(s_map)
print(n_map)


