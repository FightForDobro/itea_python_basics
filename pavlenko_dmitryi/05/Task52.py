import Task51

sum_input = Task51.sum_function(Task51.first_input, Task51.second_input)

for i in range(2):

    with open("test.txt", "a") as f:

        f.write(str(sum_input)+ "\n")

with open("test.txt", 'r') as f:

     copy_text = f.read()

print(copy_text)

new_list = []

with open("test.txt", 'r') as f:

    copy_lines = f.read().splitlines()

    for i in  copy_lines:

        new_list.append(i)

print (new_list)

for i in new_list:
    print(i)