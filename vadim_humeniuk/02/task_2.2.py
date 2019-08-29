while True:

    user_input = input('Enter a sentence to reverse it: ')

    reverse_string = ''

    for i in user_input:
        reverse_string = i + reverse_string

    print(reverse_string)

    print('Do you want reverse another sentence? ')

    user_answer = input()

    if user_answer in ('yes', 'y'):
        continue

    elif user_answer in ('no', 'n'):
        break
