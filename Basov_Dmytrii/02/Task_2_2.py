input_string = input('Enter something: ')
index_s = len(input_string) - 1      # finding the last value of index in list
revers_word = ''        # Initial string

for i in input_string:
    revers_word += (input_string[index_s])
    index_s -= 1

print(revers_word)
