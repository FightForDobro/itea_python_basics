user_input = input("Enter text: ")
new_list = []
counter = 1
inverted_text = ""

for i in user_input:

    new_list.append(user_input[len(user_input) - counter])
    counter = counter + 1

for i in new_list:

    inverted_text += i

print(inverted_text)
