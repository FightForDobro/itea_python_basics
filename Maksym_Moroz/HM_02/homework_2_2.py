words = str(input("Enter smth... \n"))

counter = 1
counter2 = 0
list_one = []
new_str = ""

for i in words:

    list_one.append(words[len(words)-counter])

    counter += 1

for i in list_one:

    new_str += i

print(new_str)
