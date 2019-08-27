text = list(input(' Enter a text for reverse : '))

reverse_text = []

for i in range(len(text)):

   reverse_element = text[len(text) - 1 -i]
   reverse_text.append(reverse_element)

print(reverse_text)
