"""
This code checks to see if a string has the same amount of 'x's and 'o's. The string can contain any char.
"""

a = input('Enter your string:\n')

count_x = 1
count_o = 1

for i in a:
    
    if i == 'x':
        count_x += 1

    elif i == 'X':
        count_o += 1

    elif i == 'o':
        count_o += 1
        
    elif i == 'O':
        count_o += 1

if count_x / count_o != 1:
    print(False)
    
else:
    print(True)
    
