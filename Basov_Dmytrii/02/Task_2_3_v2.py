user_input = input('Enter a list: ')
unique_list = []            # List of unique numbers
frequency_list = []         # List with frequency of numbers

while not user_input.isdigit():             # Check out of correct input
    user_input = input('Enter only numbers, please! ')

input_list = list(user_input)

for x in input_list:
    if x not in unique_list:
        unique_list.append(x)

for i in unique_list:
    counter = 0             # Initial frequency number of item from unique list

    for j in input_list:

        if j == i:
            counter += 1    # If number from input list is equal to unique number list

    frequency_list.append(counter)

# odd_list - list with numbers, which appear an odd number of times
odd_list = [unique_list[i] for i in range(len(frequency_list)) if frequency_list[i] % 2]

print('User input list:', input_list)
print('List of unique numbers:', unique_list)
print('Frequency list of unique numbers:', frequency_list)
print('This numbers appear an odd number of times:', odd_list)
