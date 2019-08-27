normal_string = list(input('Enter please a string: \n'))

reversed_string = ''

list_index = len(normal_string)

while list_index >= 1:

    list_index -= 1
    reversed_string += normal_string[i]

print(reversed_string)