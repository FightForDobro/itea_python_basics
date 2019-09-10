input_sentence = input('Enter something you want to revers:')

list_reversed = []
for symbol in range(len(input_sentence)):
    list_reversed.insert(0, input_sentence[symbol])
    reversed_str = ''.join(list_reversed)
print(list_reversed)
print(reversed_str)
