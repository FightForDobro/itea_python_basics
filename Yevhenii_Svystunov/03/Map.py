def custom_map(user_func, user_array):

    """ Returns collection changed by user function.
    
    
        Parameters:
            user_func - is the function which will change each element of source collection
            user_array - is the source array (list or string)
        
        Returns:
            new_list - is the resulting list with changed elements of source collection
        
      
    """  

    new_list = []
    
    for i in user_array:    
        
        x = user_func(i)
        new_list.append(x)

    return new_list    
