def sum_function(first_input, second_input):
    """
    This function sums two numbers or displays an error when entering text.
    :param first_input: first input
    :param second_input: second input
    :type first_input: int
    :type second_input   int
    :return: amount of inputs
    :rtype:  int
    """
    try:
        first_number = int(first_input)
        second_number = int(second_input)


    except ValueError:
        return print("You made a mistake while entering")

    else:
        sum_of_numbers = first_number + second_number
        return sum_of_numbers


first_input = input("Enter first number: ")
second_input = input("Enter second number: ")
sum_input = sum_function(first_input, second_input)
print(sum_input)

with open("test.txt", 'w') as f:
    f.write(str(sum_input)+ "\n")

