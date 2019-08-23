# Home Work 4
# Vsevolod Kryvosheiev
# Task 2.2 - Reverse String

user_string = input('Enterg your string: ')

reverce_string  = ''

# used reverse read string (-1 to -q-ty simbol)
for i in range(-1, - len(user_string) - 1, -1):
     reverce_string += user_string[i]

print(reverce_string)
