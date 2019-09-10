print('This program shows first number in array, entered odd amount of times')

string = input('enter string: ')

string_len = len(string)
symbol_occurence = []

for i in range(string_len):
    
    string_char = string[i]
    symbol_occurence.append(string.count(string_char))

for j in range(string_len):

    if symbol_occurence[j] % 2 != 0:

        print(string[j]);
        break

print('\nTHE END')

    
    
