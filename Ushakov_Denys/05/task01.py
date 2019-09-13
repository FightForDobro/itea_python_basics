# --------------------------------------
# Task 5.1 Exception ValueError Catcher
# By Ushakov Denys
# Version 0.1 2019.08.30
# --------------------------------------


def simple_num_adding(f_num, s_num):
    """
    Function adds two numbers
    :param f_num: int
    :param s_num: int
    :return: result of adding
    :rtype: int
    """

    return f_num + s_num


try:

    f_num = int(input('First number ---> '))
    s_num = int(input('Second number ---> '))
    result = str(simple_num_adding(f_num, s_num))

except ValueError:

    print('-------ERROR-------')
    print('Please enter number')
    print('-------------------')


if __name__ == '__main__':

    print(f'{f_num} + {s_num} = {result}')


