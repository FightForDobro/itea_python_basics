print('This program shows first number in integer array, entered odd amount of times')

string = input('enter string of integer chars: ')

while string.isdigit() != True:
    
    print('only integer digits are allowed\n')
    string = input('enter string of integer chars: ')

string_len = len(string)
symbol_occurence = []

for i in range(string_len):
    
    string_char = string[i]
    symbol_occurence.append(string.count(string_char))

print(symbol_occurence)

for j in range(string_len):

    if symbol_occurence[j] % 2 != 0:

        print(string[j]);
        break

print('\nTHE END')

    
    
