text = input(' Enter a text : ')

list_text = text.split(' ')
dont_analayze = ['a', 'an', 'to', 'is', 'are', 'was', 'were', 'will', 'would', 'could', 'and', 'or', 'if' , 'he', 'she', 'it', 'this', 'my']

new_text = [i for i in list_text if i not in dont_analayze]

mc = dict((x, new_text.count(x)) for x in set(new_text))
unique_d = dict((x, new_text.count(x)) for x in set(new_text) if new_text.count(x) == 1)

percent = dict((x, (new_text.count(x) / len(new_text)* 100)) for x in set(new_text))

mc_d = list(mc.items())

for i in range(len(mc_d)):

    mc_d.sort(key=lambda i: i[1])

    if i == len(mc_d) - 1 or i == len(mc_d) - 2 or i == len(mc_d) - 3:

        print(' Keywords ' , mc_d[i])

print(' unique words ' , unique_d)
print(' Words quantity : ' , len(set(list_text)))
print(' Frequency' , percent)
