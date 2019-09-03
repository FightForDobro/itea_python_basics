from homework_5_1 import sum_two_numbers

counter = 0

while counter <= 3:

    with open("file.txt", "a") as l:
        l.write(f"{str(sum_two_numbers())}\n")
    counter += 1


with open("file.txt") as f:

    all_file = f.read()

print(all_file)

new_str = ""

for i in all_file:
        new_str += i

print(new_str)

with open("file.txt") as f2:
    all_file_list = f2.readlines()

for i in all_file_list:
    print(i)
