#Create list
new_list = int(input("Enter numbers: "))
new_list = str(new_list)
output = ""
for i in new_list:
    output = i + output

new_list = [int(x) for x in str(output)]

#Find each numbers in list
find_one = [i for i in new_list if i == 1 in new_list]
find_two = [i for i in new_list if i == 2 in new_list]
find_three = [i for i in new_list if i == 3 in new_list]

#compare numbers
if len(find_one) > len(find_two) and len(find_one) > len(find_three):
    print(1)
elif len(find_two) > len(find_one) and len(find_two) > len(find_three):
    print(2)
elif len(find_three) > len(find_one) and len(three) > len(find_two):
    print(3)
else:
    print("No odd int")