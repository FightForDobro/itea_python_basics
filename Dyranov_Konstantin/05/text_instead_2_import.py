import text_instead_2


result = text_instead_2.summ_numbers(input("Enter Number_1: "), input("Ebter Number_2: "))# add any numbers
print(result)

with open("file.txt", 'a') as f:
    f.write(str(result) + '\n')

with open("file.txt", 'r') as f_1:
    first_print = f_1.readlines()
    for_first_print = [line.rstrip() for line in first_print]# remove line breaks
    print(for_first_print)

filename = "file.txt"

for line in first_print:
    print(line.rstrip())# Second print
