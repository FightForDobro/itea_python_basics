def custom_filter(user_func, user_array):

    """ Returns collection changed by user function only if user function returns True on each iteration.
    
    
        Parameters:
            user_func - is the function which will change each element of source collection
            user_array - is the source array (list or string)
        
        Returns:
            new_list - is the resulting list with some elements of source collection. If relult of condition in user function
            is True, then we write element of source list to this list and so on
        
      
    """  

    new_list = []
    
    for i in user_array:    
        
        x = user_func(i)
        if x:
            new_list.append(i)

    return new_list    
