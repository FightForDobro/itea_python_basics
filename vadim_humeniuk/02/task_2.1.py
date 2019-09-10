user_input = input('Enter any char\'s: ')

user_input.lower()

counter_x = 0
counter_o = 0

for i in user_input:

    if i in ['x']:
        counter_x += 1

    if i in ['o']:
        counter_o += 1

print(counter_x == counter_o)
