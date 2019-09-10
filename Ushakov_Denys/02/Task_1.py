# Create string from user input
new_string = input('Enter something --> ').lower()

# Calculates o's even if letter o is capital
o = [i for i in new_string if i == 'o']

# Calculates x's even if letter o is capital
x = [i for i in new_string if i == 'x']

# True condition
if len(o) == len(x):

    print(new_string)
    print('True')

# False condition
elif o != x:

    print(new_string)
    print('False')