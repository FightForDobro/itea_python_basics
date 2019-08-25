from random import randint

card_1 = randint(2 , 11)
card_2 = randint(2 , 11)
card_b1 = randint(2 , 11)
card_b2 = randint(2 , 11)
card_bo1= randint(2 , 11)
card_bo2= randint(2 , 11)

sum = card_1 + card_2 # Player
sum_b = card_b1 + card_b2 # Stiven Bot
sum_bo = card_bo1 + card_bo2 # Sambo Bot

print(card_1 , card_2)
print(sum)

if card_1 == 11 and card_2 == 11:
    print('You are winner!!! Golden victory')

while True:
    answer = input(' Do you want one more card ? (yes or no) : ')

    if answer == 'yes' or answer == 'Yes':

        new_card = randint(2 , 11)
        sum = sum + new_card

        print(' + ' , new_card)
        print(sum)

        if sum == 21:

            print(' 21 - you are winner')
            break

        elif sum > 21:

            print(' you are loser ')
            break

    if answer == 'no' or answer == 'No':

        print(sum)
        break

print(' now is Stiven bot\'s tern ') # Stiven Bot
print(card_b1, card_b2)
print(sum_b)

if card_b1 == 11 and card_b2 == 11:
    print(' Stiven Bot is win ')

while True:    # bot

    choice = randint(0 , 1)

    if choice == 0: # bot doesn't take one more card

        break

    else: # bot take one more card

        new_card_b = randint(2, 11)
        sum_b = sum_b + new_card_b

        print(' + ', new_card_b)
        print(sum_b)

        if sum_b >= 21:

            break

print(' now is bot\'s_2 tern ')  # Sambo bot
print(card_bo1, card_bo2)
print(sum_bo)

if card_bo1 == 11 and card_bo2 == 11:
    print(' Sambo bot is win ')

while True:

    choice_2 = randint(0 , 1)

    if choice_2 == 0: # Sambo bot doesn't take one more card

        if sum_bo > sum_b and sum_bo > sum and sum_bo <= 21  :

            print(' Sambo bot win ')
            break

        elif sum_b > sum and sum_b > sum_bo and sum_b <= 21:

            print(' Stiven Bot win')
            break

        elif sum > sum_b and sum > sum_bo and sum <= 21:

            print(' Player win ')
            break

        elif sum == sum_b == sum_bo:

            print(' It is draw ')
            break

        elif sum > 21 and sum_b > 21:

            print(' Sambo bot win ')
            break

        elif sum > 21 and sum_b <= 21:

            if sum_b > sum_bo:

                print(' Stiven Bot win ')
                break

            elif sum_b == sum_bo:

                print(' Sambo bot and Stiven Bot win ')
                break

            else:

                print(' Sambo bot win ')
                break

        elif sum_b > 21 and sum <= 21:

            if sum > sum_bo:

                print(' Player win ')
                break

            elif sum == sum_bo:

                print(' Sambo bot and Player win ')
                break

            else:

                print(' Sambo bot win ')
                break

    else: # Sambo bot takes one more card

        new_card_bo = randint(2, 11)
        sum_bo = sum_bo + new_card_bo

        print(' + ', new_card_bo)
        print(sum_bo)

        if sum_bo > sum_b and sum_bo > sum and sum_bo <= 21:

            print(' Sambo bot win ')
            break

        elif sum_b > sum and sum_b > sum_bo and sum_b <= 21:

            print(' Stiven Bot win')
            break

        elif sum > sum_b and sum > sum_bo and sum <= 21:

            print(' Player win ')
            break

        elif sum == sum_b == sum_bo:

            print(' It is draw ')
            break

        elif sum > 21 and sum_b > 21 and sum_bo <= 21:

            print(' Sambo bot win ')
            break

        elif sum > 21 and sum_b <= 21 and sum_bo <= 21:

            if sum_b > sum_bo:

                print(' Stiven Bot win ')
                break

            elif sum_b == sum_bo:

                print(' Sambo bot and Stiven Bot win ')
                break

            else:

                print(' Sambo bot win ')
                break

        elif sum_b > 21 and sum <= 21 and sum_bo <= 21:

            if sum > sum_bo:

                print(' Player win ')
                break

            elif sum == sum_bo:

                print(' Sambo bot and Player win ')
                break

            else:

                print (' Sambo bot win ')
                break

        elif sum_bo > 21 and sum <= 21 and sum_b <= 21:

            if sum > sum_b:

                print(' Player win ')
                break

            elif sum == sum_b:

                print(' Stiven Bot and Player win ')
                break

            else:

                print(' Stiven Bot win ')
                break

        elif sum > 21 and sum_b > 21 and sum_bo > 21:

            print(' You are losers ')
            break

print(' Player ' , sum)
print(' Stiven Bot ' , sum_b)
print(' Sambo bot ' , sum_bo)