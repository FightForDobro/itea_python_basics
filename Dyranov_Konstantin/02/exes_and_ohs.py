string_input = input("Enter word: ")

#Create filter for symbol
X_symbol = ["x", "X"]
O_symbol = ["o", "O"]

#Find symbol in string_input
X_finder = [s for s in string_input if s in X_symbol]
O_finder = [s for s in string_input if s in O_symbol]

#Result: symbol == symbol or not symbol in string_input
if len(X_finder) == len(O_finder) or not X_finder and not O_finder:
    print(True)
else:
    print(False)
