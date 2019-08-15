# Simple Black Jack v - Alpha 0.1
from random import randint as ri

# Welcome block

print('''╔╗───────────╔╗───────╔╗───────╔╗─
║╚╗╔╗─╔═╗─╔═╗║╠╗──────╠╣╔═╗─╔═╗║╠╗
║╬║║╚╗║╬╚╗║═╣║═╣─────╔╝║║╬╚╗║═╣║═╣
╚═╝╚═╝╚══╝╚═╝╚╩╝─────╚═╝╚══╝╚═╝╚╩╝
───────────────────────────────────''')

# Main Block

while True:

    # Main menu
    print('─────────Choose─Level──────────────')
    print('───────────1.Solo──────────────────')
    print('───────2.Player─Vs─Bot─────────────')
    print('──────3.Player─Vs─Bot\'s────────────')
    print('───────────4.Exit──────────────────')
    print('───────────────────────────────────')

    main_menu_button = input('Enter here ──> ')

    if not main_menu_button.isdigit():
        continue

    if main_menu_button.isdigit():

        if main_menu_button == '1':

            print('Solo Game start\'s')

            # Dealer's part
            first_d_c = ri(2, 11)
            second_d_c = ri(2, 11)
            dealer_score = first_d_c + second_d_c

            print(f'Dealer\'s first card score: {first_d_c}')

            # Player's part
            first_p_c = ri(2, 11)
            second_p_c = ri(2, 11)
            player_score = first_p_c + second_p_c

            print(f'Your current score is: {player_score}')

            # Easy win option

            if player_score == 22:

                print('Your lucky winner, you will receive your jackpot!')

                # Return to main menu

                print('If you want play again?\nEnter PA \nOr Enter anything to exit')

                play_again_option = input('Enter here ───> ')

                if play_again_option.lower() == 'pa':
                    continue

                else:
                    exit('Game Over :(')

            # Game menu

            print('If you want to Hit enter H')
            print('If you want to Stand enter S')

            game_menu_button = input('Enter Here ───> ')

            if game_menu_button.lower() == 'h':

                # Add's point to player
                add_card_hit_p = ri(2, 11)
                player_score = player_score + add_card_hit_p

                # Add's point to dealer
                add_card_hit_d = ri(2, 11)
                dealer_score = dealer_score + add_card_hit_d

            if game_menu_button.lower() == 's':

                # Add's point to dealer
                add_card_stand = ri(2, 11)
                dealer_score = dealer_score + add_card_stand

            # if more then 21 option

            if dealer_score > 21:

                print(f'Dealer\'s score is: {dealer_score}')
                print(f'Player\'s score is: {player_score}')

                print('Dealer score is more then 21')

                print('You Win!')
                print('Congratulation :)')

                print('If you want play again?\nEnter PA \nOr Enter anything to exit')

                # Return to main menu
                play_again_option = input('Enter here ───> ')

                if play_again_option.lower() == 'pa':
                    continue

                else:
                    exit('Game Over :(')

            elif player_score > 21:

                print(f'Dealer\'s score is: {dealer_score}')
                print(f'Player\'s score is: {player_score}')

                print('Your score is more then 21')

                print('You Lose!')

                print('If you want play again?\nEnter PA \nOr Enter anything to exit')

                # Return to main menu
                play_again_option = input('Enter here ───> ')

                if play_again_option.lower() == 'pa':
                    continue

                else:
                    exit('Game Over :(')

            # Lose option
            elif dealer_score > player_score:

                print(f'Dealer\'s score is: {dealer_score}')
                print(f'Player\'s score is: {player_score}')

                print('Dealer\'s score is more the your\'s')

                print('You Lose!')

                print('If you want play again?\nEnter PA \nOr press enter to exit')
                play_again_option = input('Enter here ───> ')

                # Return to main menu
                if play_again_option.lower() == 'pa':
                    continue

                else:
                    exit('Game Over :(')

            # Win Option
            elif player_score > dealer_score:

                print(f'Dealer\'s score is: {dealer_score}')
                print(f'Player\'s score is: {player_score}')

                print('Your\'s score more then dealer\'s')

                print('You Win!')
                print('Congratulation :)')

                print('If you want play again?\nEnter PA \nOr press enter to exit')

                # Return to main menu
                play_again_option = input('Enter here ───> ')

                if play_again_option.lower() == 'pa':
                    continue

                else:
                    exit('Game Over :(')

        elif main_menu_button == '2':

            print('Level 2')

        elif main_menu_button == '3':

            print('Level 3')

        elif main_menu_button == '4':

            exit('Game Over :(')
    break
