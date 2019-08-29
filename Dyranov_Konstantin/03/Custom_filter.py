def my_filter(func, x):
    """
       :This function check line length
       :param x: Input string
       :type 0: str
       :return: True or False
       :rtype: str
    """
    for i in x:

       if len(x) > 79:
           return True
       else:
           return False


