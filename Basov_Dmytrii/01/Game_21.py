from random import randint

print('\n Let\'s play a game 21!')
print('\nEnter "pass" or "Pass" to pass if you had enough points!\n \n Enter "pick" or "Pick" to pick one more card!')

# player variables

player_card_1 = randint(2, 11)
player_card_2 = randint(2, 11)
player_sum = player_card_1 + player_card_2  # First cards sum
player_overflow = False                     # Status overflow

# bot 1 variables

bot1_card_1 = randint(2, 11)
bot1_card_2 = randint(2, 11)
bot1_sum = bot1_card_1 + bot1_card_2        # First cards sum
bot1_overflow = False                       # Status overflow

# bot 2 variables

bot2_card_1 = randint(2, 11)
bot2_card_2 = randint(2, 11)
bot2_sum = bot2_card_1 + bot2_card_2        # First cards sum
bot2_overflow = False                       # Status overflow

print('\nYour cards: ' + f'{player_card_1}' + ' and ' + f'{player_card_2}.', 'Current sum = ' + f'{player_sum}')
print('\nBot 1 cards: ' + f'{bot1_card_1}' + ' and ' + f'{bot1_card_2}.', 'Current sum = ' + f'{bot1_sum}')
print('\nBot 2 cards: ' + f'{bot2_card_1}' + ' and ' + f'{bot2_card_2}.', 'Current sum = ' + f'{bot2_sum}')

# Player logic
while True:

    if player_sum > 21:
        print('\nPlayer Overflow!!!')
        player_overflow = True
        break

    choice = input('\nWhat is your choice? ')

    if choice == 'pass' or choice == 'Pass':
        break

    elif choice == 'pick' or choice == 'Pick':

        card_x = randint(2, 11)         # additional card
        player_sum = player_sum + card_x
        print('\nLast card is:', f'{card_x}. ' + 'Your sum is:', player_sum)

    else:
        print('\nincorrect input')
        continue

# bot 1 logic

while True:

    if bot1_sum > 21:
        print('\nBot 1 Overflow!!!')
        bot1_overflow = True
        break

    if bot1_sum == 20 or bot1_sum == 21:
        print('\nBot 1 choice: Pass')
        break

    bot1_choice = randint(0, 1)

    if bot1_choice == 1:
        print('\nBot 1 choice: Pass')
        break

    else:

        print('\nBot 1 choice: Pick a card')
        card_x = randint(2, 11)           # additional card
        bot1_sum = bot1_sum + card_x
        print('\nLast card is:', f'{card_x}. ' + 'Bot 1 cards sum = ', bot1_sum)

# Bot 2 logic

while True:

    if bot2_sum > 21:
        print('\nBot 2 Overflow!!!')
        bot2_overflow = True
        break

    if bot2_sum == 20 or bot2_sum == 21:
        print('\nBot 2 choice: Pass')
        break

    bot2_choice = randint(0, 1)

    if bot2_choice == 1:
        print('\nBot 2 choice: Pass')
        break

    else:

        print('\nBot 2 choice: Pick a card')
        card_x = randint(2, 11)           # additional card
        bot2_sum = bot2_sum + card_x
        print('\nLast card is:', f'{card_x}. ' + 'Bot 2 cards sum = ', bot2_sum)

# Comparison conditions

if not player_overflow and not bot1_overflow and not bot2_overflow:

    if bot1_sum < player_sum > bot2_sum:            # Player has more points (No overflow)

        print('\nBot 1 sum = ' + f'{bot1_sum}!')
        print('\nBot 2 sum = ' + f'{bot2_sum}!')
        print('\nPlayer wins with ' + f'{player_sum}!!!')

    elif player_sum < bot1_sum > bot2_sum:          # Bot 1 has more points (No overflow)

        print('\nPlayer sum = ' + f'{player_sum}!')
        print('\nBot 2 sum = ' + f'{bot2_sum}!')
        print('\nBot 1 wins with ' + f'{bot1_sum}!!!')

    elif player_sum < bot2_sum > bot1_sum:          # Bot 2 has more points (No overflow)

        print('\nPlayer sum = ' + f'{player_sum}!')
        print('\nBot 1 sum = ' + f'{bot1_sum}!')
        print('\nBot 2 wins with ' + f'{bot2_sum}!!!')

    elif player_sum == bot1_sum == bot2_sum:        # Full draw conditions
        print('\nIt\'s a full draw!')

    elif (player_sum == bot1_sum) and player_sum > bot2_sum:       # player & bot 1 draw
        print('\nIt\'s a draw! \nBot 2 lose')

    elif (player_sum == bot2_sum) and player_sum > bot1_sum:       # player & bot 2 draw
        print('\nIt\'s a draw! \nBot 1 lose')

    elif (bot1_sum == bot2_sum) and bot2_sum > player_sum:       # bot 1 & bot 2 draw
        print('\nIt\'s a draw! \nPlayer lose')

else:

    # two overflows

    if player_overflow and bot1_overflow and bot2_overflow:          # All lose
        print('\nAll lose with overflow!')

    elif player_overflow and bot1_overflow and not bot2_overflow:       # Only bot 2 wins

        print('\nPlayer sum = ' + f'{player_sum}!')
        print('\nBot 1 sum = ' + f'{bot1_sum}!')
        print('\nPlayer and bot 1 lose with overflow!!! \nBot 2 wins with ' + f'{bot2_sum}!!!')

    elif player_overflow and bot2_overflow and not bot1_overflow:       # Only bot 1 wins

        print('\nPlayer sum = ' + f'{player_sum}!')
        print('\nBot 2 sum = ' + f'{bot2_sum}!')
        print('\nPlayer and bot 2 lose with overflow!!! \nBot 1 wins with ' + f'{bot1_sum}!!!')

    elif bot1_overflow and bot2_overflow and not player_overflow:        # Only player wins

        print('\nBot 1 sum = ' + f'{bot1_sum}!')
        print('\nBot 2 sum = ' + f'{bot2_sum}!')
        print('\nBot 1 and bot 2 lose with overflow!!! \nPlayer wins with ' + f'{player_sum}!!!')

    # one overflow

    elif bot2_overflow and not (bot1_overflow and player_overflow):        # only bot 2 overflow

        if player_sum > bot1_sum:
            print('\nBot 1 sum = ' + f'{bot1_sum}!')
            print('\nBot 1 lose. \nPlayer wins with ' + f'{player_sum}!!!')

        else:
            print('\nPlayer sum = ' + f'{player_sum}!')
            print('\nPlayer lose. \nBot 1 wins with ' + f'{bot1_sum}!!!')

    elif bot1_overflow and not (bot2_overflow and player_overflow):         # only bot 1 overflow

        if player_sum > bot2_sum:
            print('\nBot 2 sum = ' + f'{bot2_sum}!')
            print('\nBot 2 lose. \nPlayer wins with ' + f'{player_sum}!!!')

        else:
            print('\nPlayer sum = ' + f'{player_sum}!')
            print('\nPlayer lose. \nBot 2 wins with ' + f'{bot2_sum}!!!')

    elif not (bot1_overflow and bot2_overflow) and player_overflow:          # only player overflow

        if bot1_sum > bot2_sum:
            print('\nBot 2 sum = ' + f'{bot2_sum}!')
            print('\nBot 2 lose. \nBot 1 wins with ' + f'{bot1_sum}!!!')

        else:
            print('\nBot 1 sum = ' + f'{bot1_sum}!')
            print('\nBot 1 lose. \nBot 2 wins with ' + f'{bot2_sum}!!!')

    else:
        print('logic fault')        # previous condition check only

# Check results
# print(player_sum, bot1_sum, bot2_sum)
# print(player_overflow, bot1_overflow, bot2_overflow)
