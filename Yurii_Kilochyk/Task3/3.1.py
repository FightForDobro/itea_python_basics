'''
Task 3.1 Array difference

Implement a difference function, which subtracts one list from another and returns the result.

It should remove all values (all of its occurrences) from list a, which are present in list b.

Examples:

call: array_diff([1, 2], [1])
return: [2]

call: array_diff([1, 2, 2, 2, 3], [2])
return: [1,3]
Added by medviediev
'''

"""
This function removes all values (all of its occurrences) from list a, which are present in list b.
:param list_a: List, from which list_b elements will be removed
:type list_a: List
:param list_b: The list of values which will be removed from list_a
:type list_b: List
:return: Return is list which contains unique to list_a elements
:rtype: List
"""
 
def array_difference(list_a, list_b):

    c = []
    
    for i in list_a:

        if i not in list_b:
            c.append(i)

    return c

a = [2, 4, 3, 5, 8]
b = [1, 2, 2, 2, 3, 7]

d = array_difference(a, b)

print('Array difference: ', d)
           
     
         
