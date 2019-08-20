# List
new_list = [1, 2, 3, 1, 2, 3, 1, 3, 3]

# Calculate elements
one = [i for i in new_list if i == 1]
two = [i for i in new_list if i == 2]
three = [i for i in new_list if i == 3]

# Decide witch number appears more
if len(one) > len(two) and len(one) > len(three):
    print(1)
elif len(two) > len(one) and len(two) > len(three):
    print(2)
else:
    print(3)
