from random import randint

print('Welcome to the game 21!')

limit = 21
my_points = 0

main_answer = input('Do you want to play? (y/n): ')

while main_answer == 'y':

    points = randint(2,11)
    my_points += points
    if my_points == limit:
        print('Your points:' , my_points, 'You win!!!')
        break
    elif my_points > limit:
        print('Sorry, but you gave more than 21. You lose!')
        break
    else:
        print('Your points:' , my_points)
        add_answer = input('Do you want to take a card? (y/n): ')
        if add_answer == 'y':
            continue
        else:
            print('It was a nice try. Goodbye!')
            break
            
if main_answer == 'n':
    print('Maybe another time')
        
        


