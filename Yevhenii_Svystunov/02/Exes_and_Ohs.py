user_input = input('Enter string: ')

counter_o = 0
counter_x = 0

if 'o' and 'x' not in user_input:

    print('True')
    
else:

    for symbol in user_input:
    
        if symbol == 'o':
            counter_o += 1
        elif symbol == 'x':
            counter_x += 1
            
    if counter_o == counter_x:
        print('True')
    else:
        print('False')