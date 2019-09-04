def summary_function(number_1, number_2, filename='result_file'):
    """
    Custom function calculate sum of two numbers
    :param number_1: inputted number
    :param number_2: inputted number
    :param filename: name of target file to save the result; 'result_file' - default name
    :type number_1: int
    :type number_2: int
    :type filename: str
    :return: The function returns sum of number
    :rtype: return type 'int'
    """
    try:
        int_num_1 = int(number_1)
        int_num_2 = int(number_2)

    except ValueError:
        return print('INPUT VALUE ERROR, PEACE OF SH*T!!!')

    summary = int_num_1 + int_num_2

    with open(f'{filename}.txt', 'a+') as file:
        file.writelines(f'{summary}')

    return summary
