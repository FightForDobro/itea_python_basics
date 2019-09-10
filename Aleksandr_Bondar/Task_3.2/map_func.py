

def cmap(func,iterable):
    """
This function works like standard map function, with only difference that it
returns list instead of map object
:param func: function what need to be applied to iterable
:param iterable: iterable data, which need to be processed by function
:type func: function, known to interpreter
:type iterable: any iterable object
:return: list of iterable's items, processed by function
:rtype: list
"""
    
    result = []
    for i in iterable:
        result.append(func(i))
    return result

# For testing:

a = input('enter something: ')
print(cmap(lambda x: x*2, a))



