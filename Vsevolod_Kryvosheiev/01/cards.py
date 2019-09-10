# home work lesson 3
# Vsevolod Kryvosheiev
# Cards Game 21

from random import randint

print('This is a game of 21.')
print('You want to play on your own or with one or two computer players')
print('If you yourself then select 1 player, if with one computer player then select 2 players,')
print('and if with two computer players then select 3 players\n')

while True:

    player_qty = int(input('How many players? (1/2/3) '))

    # check correct answer
    if player_qty != 1 and player_qty != 2 and player_qty !=3:

        print('Incorrect answer. Please try again')
        continue

    else:

        break

input('Are you ready? press any key\n')

total_score = 0
count_card = 0
need_card = 'y'

while True:

    # select cards. We consider their number and the amount of points
    random_card = randint(2, 11)
    total_score += random_card
    count_card += 1

    print('You new card: ', random_card, ' Total score: ', total_score)

#if the first 2 cards are 11 each, then the winning combination
    if total_score == 22 and count_card == 2:

        print('Congratulations')
        break

# if the amount of cards is more than 21 then the player has lost
    if total_score > 21:

        print('You lose')
        break

    if total_score == 21:

        print('Congratulations')
        break

#if the number of cards is more than 2, then ask the player if he needs new cards
    if count_card >= 2:

        while True:

            need_card = input('Do you want another card? (y/n): ')

            # check correct answer
            if need_card != 'y' and need_card != 'n':

                print('Incorrect answer. Please try again')
                continue

            else:

                break

# if the cards are not needed, display the number of points and exit
    if need_card == 'n':

        print('Your score: ', total_score)
        break

# bots


i = 0

while i < player_qty - 1:

    total_score = 0
    count_card = 0
    need_card = 1

    while True:

        random_card = randint(2, 11)
        total_score += random_card
        count_card += 1
        print('Bot ', i + 1, 'new card: ', random_card, ' Total score: ', total_score)

        #if the first 2 cards are 11 each, then the winning combination
        if total_score == 22 and count_card == 2:

            print('Congratulations bot')
            break

         # if the amount of cards is more than 21 then the player has lost
        if total_score > 21:

            print('Bot lose')
            break

        if total_score == 21:

            print('Congratulations bot')
            break

        if count_card >= 2:
            need_card = randint(0,1)

        if need_card == 0:

            print('Bot ', i, ' score: ', total_score)
            break
    i += 1
