def array_diff(x, y):

    """ Returns difference between two lists.
    
    
        Parameters:
            x - is the first list
            y - is the second list
        
        Returns:
            diff_list - is the resulting list in which we deleted all values from
            the first list, which are present in the list b
        
      
    """  
    
    diff_list = []

    for i in x:    
        match_counter = 0
        
        for j in y:        
            if i == j:
                match_counter += 1
                
        if match_counter == 0:
            diff_list.append(i)
                
    return diff_list


list_a = [1, 2, 2, 4, 3, 45, 2]
list_b = [2, 3]

return_list = array_diff(list_a, list_b)

print(return_list)




