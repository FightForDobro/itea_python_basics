text = input(' Enter a texet : ')

x = 0
o = 0

for counter in text:

    if counter == 'x' or counter == 'X':

        x += 1

    if counter == 'o' or counter == 'O':

        o += 1

print('amount of x = ' , x)
print('amount of o = ' , o)

if x == o:

    print(' True ')

else:

    print(' False ')








