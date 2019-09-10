

def array_diff (listA,listB):
    """
This function removes all occurences of each listB's element, from listA.\n
Original listA isn't modified, meanwhile result is written to new list.\n
:param listA: list, from which listB's elements will be removed
:type listA: list
:param listB: list, which provides elements to remove from listA
:type listB: list
:return: return is list which contains unique to listA elements
:rtype: list
    """
    listC = listA.copy()

    for i in listB:
        
        if i in listC:
            
            for j in listC:
                
                if j == i:
                    listC.remove(j)

    return listC

#For testing:

listA = list(input('enter list A: '))
listB = list(input('enter list B: '))

list_diff = array_diff(listA, listB)

print('array difference is: ', list_diff)
