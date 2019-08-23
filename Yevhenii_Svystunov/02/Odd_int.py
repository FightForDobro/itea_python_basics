my_list = [3, 2, 1, 3, 2, 3, 1, 1]
new_list = []

print(my_list)

for i in my_list:

    counter = 0
    
    for j in my_list:
    
        if i == j:
            counter =+ 1
        
    if counter % 2:
        new_list.append(i)
        
print(new_list[0])