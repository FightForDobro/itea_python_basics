try:
    number_1 = int(input("Enter number_1: "))
    number_2 = int(input("Enter number_2: "))

except ValueError:
    numbers_summ = "One of input numbers not int"

else:
    numbers_summ = number_1 + number_2

print(numbers_summ)