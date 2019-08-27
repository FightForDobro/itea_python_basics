input_sentence = input('Enter the letters')

x_counter = 0
o_counter = 0
for symbol in input_sentence.lower():
    if symbol != 'x' and symbol != 'o':
        continue
    if symbol == 'x':
        x_counter += 1
    if symbol == 'o':
        o_counter += 1
if x_counter == o_counter and x_counter != 0 != o_counter:
    print(True)
elif x_counter != o_counter:
    print(False)
else:
    print(True)




