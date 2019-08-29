old_list = ['1', '2', '3', '4', '5', '6', '7']
new_list = []

def my_map(x):
    """
        :function translates str to int
        :param old_list: First list
        :param new_list: new_listt
        :type old_list: list
        :type new_list: list
        :return: list 
        :rtype: list
    """
    for item in old_list:
        new_list.append(int(item))


my_map(old_list)

print(new_list)

#True map func
old_list = ['1', '2', '3', '4', '5', '6', '7']
new_list = list(map(int, old_list))
print(new_list)
