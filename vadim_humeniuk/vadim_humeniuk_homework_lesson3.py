from random import randint

first_card = randint(2, 11) + randint(2, 11)  # player randomise
second_card = randint(2, 11) + randint(2, 11)
third_card = randint(2, 11) + randint(2, 11)

first_bot_card1 = randint(2, 11) + randint(2, 11)  # first bot randomise
first_bot_card2 = randint(2, 11) + randint(2, 11)
first_bot_card3 = randint(2, 11) + randint(2, 11)

second_bot_card1 = randint(2, 11) + randint(2, 11)  # second bot randomise
second_bot_card2 = randint(2, 11) + randint(2, 11)
second_bot_card3 = randint(2, 11) + randint(2, 11)

print('Hello player, please enter your name: ')

user_name = input('Please enter your Name: ')

print(user_name, 'do you waned to pick a card? ')  # player pick a card

print('yes or no')

while True:
    answer = input()
    if answer in ('y', 'yes'):
        first_card_score = first_card
        break

    elif answer in ('n', 'no'):
        first_card_score = 0
        break

while True:
    first_bot_choice1 = randint(0, 1)  # first bot random pick a card
    if first_bot_choice1 == 1:
        first_bot_card1_score = first_bot_card1
        break

    elif first_bot_choice1 == 0:
        first_bot_card1_score = 0
        break

while True:
    second_bot_choice1 = randint(0, 1)  # second bot random pick a card
    if second_bot_choice1 == 1:
        second_bot_card1_score = second_bot_card1
        break

    elif second_bot_choice1 == 0:
        second_bot_card1_score = 0
        break

user_score = first_card_score  # score all players
first_bot_score = first_bot_card1_score
second_bot_score = second_bot_card1_score

print('your score is', user_score)

print('Do you want pick ome more card? ')  # second round
print('yes or no')
while True:
    answer = input()
    if answer in ('y', 'yes'):
        second_card_score = second_card
        break

    elif answer in ('n', 'no'):
        second_card_score = 0
        break

while True:
    first_bot_choice2 = randint(0, 1)
    if first_bot_choice2 == 1:
        first_bot_card2_score = first_bot_card2
        break

    elif first_bot_choice2 == 0:
        first_bot_card2_score = 0
        break

while True:
    second_bot_choice2 = randint(0, 1)
    if second_bot_choice2 == 1:
        second_bot_card2_score = second_bot_card2
        break

    elif second_bot_choice2 == 0:
        second_bot_card2_score = 0
        break

user_score = (first_card_score + second_card_score)  # score for second round
first_bot_score = (first_bot_card1_score + first_bot_card2_score)
second_bot_score = (second_bot_card1_score + second_bot_card2_score)

print('your score is', user_score)
print('Do you want pick last card? ')  # third round
print('yes or no')
while True:
    answer = input()
    if answer in ('y', 'yes'):
        c = third_card
        break

    elif answer in ('n', 'no'):
        c = 0
        break

while True:
    first_bot_choice3 = randint(0, 1)
    if first_bot_choice3 == 1:
        c1 = first_bot_card3
        break

    elif first_bot_choice3 == 0:
        c1 = 0
        break

while True:
    second_bot_choice3 = randint(0, 1)
    if second_bot_choice3 == 1:
        c2 = second_bot_card3
        break

    elif second_bot_choice3 == 0:
        c2 = 0
        break

user_score = (first_card_score + second_card_score + c)  # all game score
first_bot_score = (first_bot_card1_score + b1 + c1)
second_bot_score = (second_bot_card1_score + b2 + c2)
    
print('your score is', user_score)
print('first bot score is', first_bot_score)
print('second bot score is', second_bot_score)

while first_bot_score > 21:  # if bot's have more then 21 they should not win
    first_bot_score = 0

while second_bot_score > 21:
    second_bot_score = 0

while True:  # condition for victory
    if user_score <= 21:
        if user_score > first_bot_score or second_bot_score:
            print('congratulations', user_name, 'you are winner ')
            break
        elif first_bot_score > user_score or second_bot_score:
            print(' first bot win')
            break
        elif second_bot_score > user_score or first_bot_score:
            print('second bot win ')
            break

    elif user_score > 21:
        print('You lose', user_name, 'Game over ')
        if first_bot_score > second_bot_score:
            print('first bot win ')
            break
        elif second_bot_score > first_bot_score:
            print('second bot win ')
            break
    break
