user_input = input("Enter text: ")
counter_x = 0
counter_o = 0

for i in user_input:
    if i == 'o' or i == 'O':
      counter_o = counter_o + 1

    elif i == 'x' or i == 'X':
        counter_x = counter_x + 1
    else:
        continue

if counter_o == counter_x:
    print ("True")
else:
    print ("False")
