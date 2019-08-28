print('This program reverses user-entered string')

user_str = input('enter string: ')
user_str_len = len(user_str)

string_new = []

for i in range(user_str_len):
    
    string_new_symbol = user_str[user_str_len - i -1]
    string_new.append(string_new_symbol)
    print(string_new[i], end='')

print('\nTHE END')
