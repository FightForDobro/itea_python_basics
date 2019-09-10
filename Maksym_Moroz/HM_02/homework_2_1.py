words = input("Enter smth... \n")

list_x = [i for i in words if i == "X" or i == "x"]
list_o = [i for i in words if i == "O" or i == "o"]

if len(list_o) == len(list_x):

    print("YEP")

else:

    print("Count x != count o")
