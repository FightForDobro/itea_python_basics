"""
This code reverses a string.
"""

a = input('Enter your word:\n')

b = len(a)
c = []

while b:

    b -= 1
    c.append(a[b])

# print(c)
d = ''.join(c)
print(d)

