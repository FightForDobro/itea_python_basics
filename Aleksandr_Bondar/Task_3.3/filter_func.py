

def cfilter(func,iterable):
    """
This function works like standard filter function, with only difference that it
returns list instead of filter object
:param func: function what need to be applied to iterable as a filter,
this function must return boolean result.
:param iterable: iterable data, which need to be processed by function
:type func: function with boolean result, known to interpreter
:type iterable: any iterable object
:return: list of iterable's items, for which function returns 'True'
:rtype: list
"""
    result = []

    for i in iterable:

        if func(i) == True:
            result.append(i)

    return result

# For testing:

a = input('enter something: ')
print(cfilter(str.isalpha, a))

