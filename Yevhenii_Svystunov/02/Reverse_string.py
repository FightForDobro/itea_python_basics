user_input = input('Enter string: ')

string_len = len(user_input)
reverse_string = ''
counter = 0

while counter < string_len:

    counter += 1
    reverse_string += user_input[-counter]
    
print(reverse_string)
