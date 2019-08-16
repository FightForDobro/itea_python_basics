# Simple Black Jack v - Alpha 0.2
from random import randint as ri
from random import choice

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
            # Ошибка нужна помощь
            '''if game_menu_button == 'H' or game_menu_button == 'S':
                print('Choose Hit or Stand')
                continue'''

            # Game logic

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

            # Score info
            print(f'Your score is: {player_score}')
            print(f'Dealer score is: {dealer_score}')

            # if equals

            if player_score == dealer_score:
                print('Score\'s are equal')
                print('DRAW')

            # if more then 21 option

            if dealer_score > 21:

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

            print('Start mode with single bot')

            # Single bot
            single_bot_first_card = ri(1, 11)
            single_bot_second_card = ri(1, 11)
            single_bot_score = single_bot_first_card + single_bot_second_card
            bots_names = ['Jon', 'Steve', 'Ivan', 'Olga', 'Katya', 'Rebecka']
            random_bot_name = choice(bots_names)

            # Player
            first_p_c = ri(1, 11)
            second_d_c = ri(1, 11)
            player_score = first_p_c + second_d_c
            print(f'Your\'s score is: {player_score}')

            # Dealer
            first_d_c = ri(1, 11)
            second_d_c = ri(1, 11)
            dealer_score = first_d_c + second_d_c
            print(f'Delear\'s first card is: {first_d_c}')

            # Easy win option
            if player_score == 22 and single_bot_score == 22:
                print(f'You and [BOT]{random_bot_name} win\'s')

            elif player_score == 22:
                print('You win')

            elif single_bot_score == 22:
                print(f'[BOT]{random_bot_name} win')

            # Return to main menu
            print('If you want play again?\nEnter PA \nOr press enter to exit')
            play_again_option = input('Enter here ───> ')

            if play_again_option.lower() == 'pa':
                continue

            else:
                exit('Game Over :(')

            # Super Smart Artificial Intelligence also also known as SSAI
            SSAI = ri(0, 5)  # 0-passive 5-aggressive
            print(f'Bot mood is: {SSAI}')
            if SSAI == 1:
                if single_bot_score <= 5:
                    single_bot_score += ri(1, 11)
            elif SSAI == 2:
                if single_bot_score <= 7:
                    single_bot_score += ri(1, 11)
            elif SSAI == 3:
                if single_bot_score <= 10:
                    single_bot_score += ri(1, 11)
            elif SSAI == 4:
                if single_bot_score <= 15:
                    single_bot_score += ri(1, 11)
            elif SSAI == 5:
                single_bot_score += ri(1, 11)

            # Game menu

            print('If you want to Hit enter H')
            print('If you want to Stand enter S')

            game_menu_button = input('Enter Here ───> ')

            # Ошибка нужна помощь
            '''if not game_menu_button.lower() == 'h' or 's':

                print('Choose Hit or Stand')
                continue'''

            # Game logic

            if game_menu_button.lower() == 'h':

                player_score += ri(1, 11)

                dealer_score += ri(1, 11)

            if game_menu_button.lower() == 's':
                dealer_score += ri(1, 11)

            # Score info
            print(f'Your score is: {player_score}')
            print(f'Dealer score is: {dealer_score}')
            print(f'[BOT]{random_bot_name} score is: {single_bot_score}')

            # if equals

            if dealer_score == single_bot_score == player_score:
                print('All score equals')
                print('DRAW')

                # Return to main menu
                print('If you want play again?\nEnter PA \nOr press enter to exit')
                play_again_option = input('Enter here ───> ')

                if play_again_option.lower() == 'pa':
                    continue

                else:
                    exit('Game Over :(')

            if single_bot_score == dealer_score:

                print(f'{random_bot_name} and dealer score equals')
                if player_score > single_bot_score:
                    print('You win')
                elif player_score < single_bot_score:
                    print('DRAW')

                # Return to main menu
                print('If you want play again?\nEnter PA \nOr press enter to exit')
                play_again_option = input('Enter here ───> ')

                if play_again_option.lower() == 'pa':
                    continue

                else:
                    exit('Game Over :(')

            if single_bot_score == player_score:

                print('All score equals')
                print('DRAW')

                # Return to main menu
                print('If you want play again?\nEnter PA \nOr press enter to exit')
                play_again_option = input('Enter here ───> ')

                if play_again_option.lower() == 'pa':
                    continue

                else:
                    exit('Game Over :(')

            # if more then 21

            if dealer_score > 21 and single_bot_score > 21:

                print(f'Dealer and [BOT]{random_bot_name} have more then 21')
                print('You win')

                # Return to main menu
                print('If you want play again?\nEnter PA \nOr press enter to exit')
                play_again_option = input('Enter here ───> ')

                if play_again_option.lower() == 'pa':
                    continue

                else:
                    exit('Game Over :(')

            if player_score > 21:

                print('You have more then 21')
                print('You Lose')
                # Return to main menu
                print('If you want play again?\nEnter PA \nOr press enter to exit')
                play_again_option = input('Enter here ───> ')

                if play_again_option.lower() == 'pa':
                    continue

                else:
                    exit('Game over :(')

            if single_bot_score > 21:

                print('Bot have more then 21')
                print('Bot lose')

                if dealer_score > player_score:

                    print('Dealer have more score')
                    print('You lose')

                elif dealer_score == player_score:
                    print('Score are equal')
                    print('DRAW')

                    # Return to main menu
                    print('If you want play again?\nEnter PA \nOr press enter to exit')
                    play_again_option = input('Enter here ───> ')

                    if play_again_option.lower() == 'pa':
                        continue

                    else:
                        exit('Game Over :(')

                elif player_score > dealer_score:

                    print('You have more score then dealer')
                    print('You win')

                    # Return to main menu
                    print('If you want play again?\nEnter PA \nOr press enter to exit')
                    play_again_option = input('Enter here ───> ')

                    if play_again_option.lower() == 'pa':
                        continue

                    else:
                        exit('Game Over :(')
                elif player_score == dealer_score:
                    print('Score are equals')
                    print('DRAW')
            # Win Option

            if player_score > single_bot_score and player_score > dealer_score:
                print('You win all of them')

                # Return to main menu
                print('If you want play again?\nEnter PA \nOr press enter to exit')
                play_again_option = input('Enter here ───> ')

                if play_again_option.lower() == 'pa':
                    continue

                else:
                    exit('Game Over :(')

            # Lose option
            if single_bot_score > player_score and single_bot_score > dealer_score:
                print('Bot win all of as')

                # Return to main menu
                print('If you want play again?\nEnter PA \nOr press enter to exit')
                play_again_option = input('Enter here ───> ')

                if play_again_option.lower() == 'pa':
                    continue

                else:
                    exit('Game Over :(')

            elif single_bot_score < dealer_score:
                print('Casino wins')

                # Return to main menu
                print('If you want play again?\nEnter PA \nOr press enter to exit')
                play_again_option = input('Enter here ───> ')

                if play_again_option.lower() == 'pa':
                    continue

                else:
                    exit('Game Over :(')

            elif dealer_score > player_score:
                print('You lose')

                # Return to main menu
                print('If you want play again?\nEnter PA \nOr press enter to exit')
                play_again_option = input('Enter here ───> ')

                if play_again_option.lower() == 'pa':
                    continue

                else:
                    exit('Game Over :(')

        elif main_menu_button == '3':

            print('Start mode with two bot\'s')

            # First Bot
            first_fb_c = ri(1, 11)
            second_fb_c = ri(1, 11)
            first_bot_score = first_fb_c + second_fb_c
            boy_bots_names = ['Jon', 'Steve', 'Ivan']
            random_boy_bot_name = choice(boy_bots_names)

            # Second Bot
            first_sb_c = ri(1, 11)
            second_sb_c = ri(1, 11)
            second_bot_score = first_sb_c + second_sb_c
            girl_bots_names = ['Olga', 'Katya', 'Rebecka']
            random_girl_bot_name = choice(girl_bots_names)

            # Player
            first_p_c = ri(1, 11)
            second_p_c = ri(1, 11)
            player_score = first_p_c + second_p_c

            # Dealer
            first_d_c = ri(1, 11)
            second_d_c = ri(1, 11)
            dealer_score = first_d_c + second_d_c

            # Easy win option
            if player_score == 22 and first_bot_score == 22 and second_bot_score == 22:
                print(f'You and [BOT]{boy_bots_names} and [BOT]{girl_bots_names} win\'s')

                # Return to main menu
                print('If you want play again?\nEnter PA \nOr press enter to exit')
                play_again_option = input('Enter here ───> ')

                if play_again_option.lower() == 'pa':
                    continue

                else:
                    exit('Game Over :(')

            elif player_score == 22:
                print('You win')

                # Return to main menu
                print('If you want play again?\nEnter PA \nOr press enter to exit')
                play_again_option = input('Enter here ───> ')

                if play_again_option.lower() == 'pa':
                    continue

                else:
                    exit('Game Over :(')

            elif first_bot_score == 22:
                print(f'[BOT]{boy_bots_names} win')

                # Return to main menu
                print('If you want play again?\nEnter PA \nOr press enter to exit')
                play_again_option = input('Enter here ───> ')

                if play_again_option.lower() == 'pa':
                    continue

                else:
                    exit('Game Over :(')

            elif second_bot_score == 22:
                print(f'[BOT]{girl_bots_names} win')

                # Return to main menu
                print('If you want play again?\nEnter PA \nOr press enter to exit')
                play_again_option = input('Enter here ───> ')

                if play_again_option.lower() == 'pa':
                    continue

                else:
                    exit('Game Over :(')

            # Advance Super Smart Artificial Intelligence also also known as ASSAI
            # For first bot
            ASSAI_boy = ri(0, 5)  # 0-passive 5-aggressive
            print(f'First Bot mood is: {ASSAI_boy}')
            if ASSAI_boy == 1:
                if dealer_score > first_bot_score:
                    if first_bot_score <= 5:
                        first_bot_score += ri(1, 11)
            elif ASSAI_boy == 2:
                if dealer_score > first_bot_score:
                    if first_bot_score <= 5:
                        first_bot_score += ri(1, 11)
            elif ASSAI_boy == 3:
                if dealer_score > first_bot_score:
                    if first_bot_score <= 15:
                        first_bot_score += ri(1, 11)
            elif ASSAI_boy == 4:
                if dealer_score > first_bot_score:
                    if first_bot_score <= 18:
                        first_bot_score += ri(1, 11)
            elif ASSAI_boy == 5:
                first_bot_score += ri(1, 11)

            # For second bot
            ASSAI_girl = ri(0, 5)  # 0-passive 5-aggressive
            print(f'Second Bot mood is: {ASSAI_girl}')
            if ASSAI_girl == 1:
                if dealer_score > second_bot_score:
                    if second_bot_score <= 3:
                        second_bot_score += ri(1, 11)
            elif ASSAI_girl == 2:
                if dealer_score > second_bot_score:
                    if second_bot_score <= 6:
                        second_bot_score += ri(1, 11)
            elif ASSAI_girl == 3:
                if dealer_score > second_bot_score:
                    if second_bot_score <= 9:
                        second_bot_score += ri(1, 11)
            elif ASSAI_girl == 4:
                if dealer_score > second_bot_score:
                    if second_bot_score <= 13:
                        second_bot_score += ri(1, 11)
            elif ASSAI_girl == 5:
                if dealer_score > second_bot_score:
                    if second_bot_score <= 16:
                        second_bot_score += ri(1, 11)

            # Game menu

            print('If you want to Hit enter H')
            print('If you want to Stand enter S')

            game_menu_button = input('Enter Here ───> ')

            # Game logic

            bots = first_bot_score and second_bot_score

            if game_menu_button.lower() == 'h':

                player_score += ri(1, 11)

                dealer_score += ri(1, 11)

            if game_menu_button.lower() == 's':
                dealer_score += ri(1, 11)

            # Score info
            print(f'Your score is: {player_score}')
            print(f'Dealer score is: {dealer_score}')
            print(f'[BOT]{random_boy_bot_name} score is: {first_bot_score}')
            print(f'[BOT]{random_girl_bot_name} score is: {second_bot_score}')

            # if equal

            if dealer_score == player_score == second_bot_score == first_bot_score:

                print('equal all')
                print('DRAW1')

            # if more then 21
            elif player_score > 21:
                print('You have more then 21')
                print('You lose1')

            elif dealer_score > 21 and bots > 21:

                print('all have more then 21')
                print('You win1')

            elif dealer_score > 21 and first_bot_score > 21:

                if player_score > second_bot_score:
                    print('You have more score')
                    print('You win2')

                elif player_score < second_bot_score:
                    print(f'{girl_bots_names} have more score')
                    print('You lose2')

                elif player_score == second_bot_score:
                    print('Score are equal')
                    print('Draw2')

            elif first_bot_score > 21 and second_bot_score > 21:

                if player_score > dealer_score:
                    print('You have more score')
                    print('You win3')

                elif player_score < dealer_score:
                    print('Dealer have more score')
                    print('You lose3')

                elif player_score == dealer_score:
                    print('Score are equal')
                    print('Draw3')

            elif dealer_score > 21 and second_bot_score > 21:

                if player_score > first_bot_score:
                    print('You have more score')
                    print('You win4')

                elif player_score < first_bot_score:
                    print(f'{boy_bots_names} have more score')
                    print('You lose4')

                elif player_score == first_bot_score:
                    print('Score are equal')
                    print('Draw4')

            elif dealer_score > 21:

                if player_score == bots:
                    print('Score are equal')
                    print('DRAW5')

                elif player_score > second_bot_score and player_score > first_bot_score:
                    if player_score == second_bot_score:
                        print('Score are equal')
                        print('DRAW6')
                    elif player_score == first_bot_score:
                        print('Score are equal')
                        print('DRAW7')
                    else:
                        print('You have more score')
                        print('You win5')

                elif player_score < second_bot_score:
                    print(f'{girl_bots_names} have more score')
                    print('You lose5')

                elif player_score < first_bot_score:
                    print(f'{boy_bots_names} have more score')
                    print('You lose6')

            elif first_bot_score > 21:

                if player_score == second_bot_score and player_score == dealer_score:
                    print('Score are equal')
                    print('DRAW9')

                elif player_score > second_bot_score and player_score > dealer_score:
                    if player_score == second_bot_score:
                        print('Score are equal')
                        print('DRAW10')
                    elif player_score == dealer_score:
                        print('Score are equal')
                        print('DRAW11')
                    else:
                        print('You have more score')
                        print('You win7')

                elif player_score < second_bot_score:
                    print(f'{girl_bots_names} have more score')
                    print('You lose7')

                elif player_score < dealer_score:
                    print('Dealer have more score')
                    print('You lose8')

            elif second_bot_score > 21:

                if player_score == dealer_score and player_score == first_bot_score:
                    print('Score are equal')
                    print('DRAW')

                elif player_score > dealer_score and player_score > first_bot_score:
                    if player_score == first_bot_score:
                        print('Score are equal')
                        print('DRAW')
                    elif player_score == dealer_score:
                        print('Score are equal')
                        print('DRAW')
                    else:
                        print('You have more score')
                        print('You win')

                elif player_score < dealer_score:
                    print('Dealer have more score')
                    print('You lose')

                elif player_score < first_bot_score:
                    print(f'{boy_bots_names} have more score')
                    print('You lose')




            # Win option
            elif player_score > dealer_score and first_bot_score and second_bot_score:
                print('You win10')


            # Lose option
            elif dealer_score > player_score or first_bot_score > player_score or second_bot_score > player_score:
                print('You lose10')



        elif main_menu_button == '4':

            exit('Game Over :(')
    break
