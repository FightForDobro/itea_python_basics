import Task_5_1 as task


a = input('Enter number 1: ')
b = input('Enter number 2: ')
my_file = input('Enter a name of your file to save the result: ')

x = task.summary_function(a, b, my_file)

if x:
    print('Your last sum is: ', x)
    print('The 1st method of output!\n')

    with open(f'{my_file}.txt') as file:
        print(file.read())

    print('--------------')
    print('The 2nd method of output!\n')

    with open(f'{my_file}.txt') as file:
        for i in file:
            print(i)

    print('--------------')
    print('The 3rd method of output!\n')

    with open(f'{my_file}.txt') as file:
        for i in file:
            list_file = file.readlines()

    for j in list_file:
        print('Your result is: ', j.rstrip())
