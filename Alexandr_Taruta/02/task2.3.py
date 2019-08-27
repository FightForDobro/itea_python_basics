numbers_list = [int(number) for number in input('Enter list of numbers ').split()]

for number in range(0, len(numbers_list)):
    counter = 0

    for number_1 in range(0, len(numbers_list)):
        if numbers_list[number] == numbers_list[number_1]:
            counter += 1
if counter % 2 != 0:
    print(numbers_list[number])
