def sum_two_numbers():
    """ This function asked the user to enter two numbers and then sums them up, if the numbers are not int, print on display an exception text
        :param:
        :type:
        :return: Return the sum of two numbers
        :rtype: int
    """
    number1 = input("Enter first number \n")
    number2 = input("Enter second number \n")

    try:
        sum = ((int(number1) + int(number2)))
        return sum

    except ValueError or UnboundLocalError:
        print("Number must be integer ")


if __name__ == "__main__":
    with open("file.txt", "w") as f:
        f.write(f"{str(sum_two_numbers())}\n")
