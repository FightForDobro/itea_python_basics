from random import randint

my_list = [randint(0,9) for i in range(10)]
print(my_list)


most_common = None
q_most_common = 0

for item in my_list:
    q = my_list.count(item)
    if q > q_most_common:
        q_most_common = q
        most_common = item

print(most_common)
