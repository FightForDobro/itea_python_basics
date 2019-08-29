'''
Task 3.3 Custom filter

Implement custom_filter function, which will behave like the original Python filter() function.
Added by medviediev 
'''

"""
This function executes input functions with iterable values.
:param func: Input function
:type func: Function
:param iterable: List of elements which will be fed to the input of the function
:type iterable: List
:return: The list that contains repeatable values ​​processed by a function and whose result is True
:rtype: List
"""

def custom_filter(func, iterable):

    a = [string for string in iterable if func(string)]
    return a

"""
 Input functions for example
"""
def has_o(string):
    return 'o' in string.lower()

b = ['One', 'two', 'three']
c = ['qwert', 'three', '34235']

f1 = custom_filter(has_o, b)
f2 = custom_filter(has_o, c)

print(f1)
print(f2)
