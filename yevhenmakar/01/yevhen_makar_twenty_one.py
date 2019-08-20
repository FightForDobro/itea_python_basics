from random import randint

print('Welcome to game "twenty one"')
while True:
    players_quantity = int(input('Write down how much player do you want to play with? Maximum 3.\n'))
    if players_quantity < 0 or players_quantity > 3:
        print('Write down correct number: 1, 2 or 3')
        continue
    else:
        break

# Game for player
first_random_card = randint(2, 11)
print('Your first card is:', first_random_card)
second_random_card = randint(2, 11)
print('Your second card is:', second_random_card)
points_sum = first_random_card + second_random_card
print('Your points are:', points_sum)

if points_sum == 22:
    print('You are super champion')
elif points_sum < 20:
    while True:
        answer = input('Do you want to pick more?? Write down "pick" or "pass"!\n')
        if answer == 'pick':
            points_sum += randint(2, 11)
            print('Your points are:', points_sum)
            if points_sum > 21:
                print('You lose!')
                points_sum = 0
                break
        if answer == 'pass':
            print('Your overal score is', points_sum)
            break

# Game for first bot
    first_random_card_for_first_bot = randint(2, 11)
    second_random_card_for_first_bot = randint(2, 11)
    points_sum_for_fisrt_bot = first_random_card_for_first_bot + second_random_card_for_first_bot

    while True:
        answer = randint(0, 1)
        if answer == 0:
            points_sum_for_fisrt_bot += randint(2, 11)
            if points_sum_for_fisrt_bot > 21:
                points_sum_for_fisrt_bot = 0
                break
        if answer == 1:
            break

# Game for second bot
    first_random_card_for_second_bot = randint(2, 11)
    second_random_card_for_second_bot = randint(2, 11)
    points_sum_for_second_bot = first_random_card_for_second_bot + second_random_card_for_second_bot

    while True:
        answer = randint(0, 1)
        if answer == 0:
            points_sum_for_second_bot += randint(2, 11)
            if points_sum_for_second_bot > 21:
                points_sum_for_second_bot = 0
                break
        if answer == 1:
            break


#Game results
if players_quantity == 1:
    print('Player won, score is:', points_sum)

if players_quantity == 2:
    if points_sum > points_sum_for_fisrt_bot:
        print('Player won, score is:', points_sum, '\nScore for first bot:', points_sum_for_fisrt_bot)
    else:
        print('First bot won, score is:', points_sum_for_fisrt_bot, 'Score for player:', points_sum)

if players_quantity == 3:
    if points_sum > points_sum_for_fisrt_bot and points_sum > points_sum_for_second_bot:
        print('Player won, score is:', points_sum, '\nScore for first bot:', points_sum_for_fisrt_bot,
              '\nScore for second bot:', points_sum_for_second_bot)
    elif points_sum_for_fisrt_bot > points_sum and points_sum_for_fisrt_bot > points_sum_for_second_bot:
        print('First bot won, score is:', points_sum_for_fisrt_bot, 'Score for player:', points_sum,
              'Score for second bot:', points_sum_for_second_bot)
    else:
        print('Second bot won, score is:', points_sum_for_second_bot, 'Score for player:', points_sum,
              'Score for first bot:', points_sum_for_fisrt_bot)