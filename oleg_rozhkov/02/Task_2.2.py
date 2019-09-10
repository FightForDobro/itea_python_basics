# Task 2.2 - Reverse String

input_list = list(input('Input any text:\n'))

# backward_list = input_list[::-1] # easiest way

# strange -> why it doesn't work
# backward_list = [i for i in range(len(input_list)-1, -1, -1)]

backward_list = []

for i in range(len(input_list)-1, -1, -1):

    backward_list.append(input_list[i])

backward_string = ''

for i in backward_list:

    backward_string += i
    
print(backward_string)

