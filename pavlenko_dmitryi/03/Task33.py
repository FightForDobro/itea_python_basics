def custom_filter (function, param):
    """
      This function will filter items from the list that match the conditions.
      :param a: function
      :param b: list
      :type function: function
      :type parametrs: an object
      :return: list of elements that meet the specified function parameters
      :rtype: list
      """

    result = []

    for i in param:

       if function(i):

         result.append(i)

        return result