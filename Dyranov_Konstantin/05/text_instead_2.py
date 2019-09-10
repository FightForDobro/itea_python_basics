def summ_numbers(a, b):
    """
        :function created to be able to import to another file
        :param number_1: input first number
        :param number_2: input second number
        :type number_1: int
        :type number_2: int
        :return: summ number_1 & number_2
        :rtype: int
    """

    try:
        number_1 = int(a)
        number_2 = int(b)

    except ValueError:# we expect the error "non-numeric value entered"
        numbers_summ = ""
        print("One of input number not int")

    else:
        numbers_summ = number_1 + number_2

    return numbers_summ


result_summ = summ_numbers(input("Enter number_1: "), input("Enter number_2: "))
print(result_summ)

with open("file.txt", 'a') as f:
    f.write(str(result_summ) + '\n')# write data to a file
