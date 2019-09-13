# --------------------------------------
# Task 5.2 Read file and modify values
# By Ushakov Denys
# Version 0.1 2019.08.31
# --------------------------------------

import task01

# Block of reading file
try:

    with open('task1.txt', 'a') as f:

        f.write(task01.result)
        f.write('\n')

except FileNotFoundError:

    print('\nFile doesn\'t exist')
    print('Creating new file')
    print('........')
    with open('task1.txt', 'w') as f:

        f.write(task01.result)
        f.write('\n')

    print('Restart program')


else:

    with open('task1.txt', 'r') as f:

        text = f.read()
# -------------------------------------------

# Block of prints---------------------------
print('\n--------------------')
print('Simple reading file:')
print(text, end='')
print('--------------------\n')

# Iterate over file
print('Iterate over file:')
counter = 0
for line in text.split('\n'):

    print(line)
    counter += 1
# ----------------------------

# Add result to list without \n
list_of_text = text.splitlines()
int_list = []

for i in list_of_text:

    int_list.append(int(i))
# -------------------------------

# Call function and print
print('------------------------')
print('List form lines')
print(list(int_list))
print('------------------------')
# -------------------------------------------------
