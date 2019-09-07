# Task 2.1 - Exes and Ohs

input_list = list(input('Input any text:\n'))

number_of_x, number_of_o = 0, 0

for i in input_list:
    
    if i == 'x' or i == 'X':
        number_of_x += 1
        
    if i == 'o' or i == 'O':
        number_of_o += 1

if number_of_x == number_of_o:
    print('Number is equal')

else:
    print('Number is NOT equal')

