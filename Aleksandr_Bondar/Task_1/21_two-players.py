from random import randint

print('=== it\'s O4KO game with one bot ===')

user_score = 0
bot_score = 0

while user_score < 21 and bot_score < 21:

    user_choise = input('enter your choise, "pick" or "pass": ')
    bot_choise = randint(0,1)
    
    if user_choise == 'pick' and bot_choise == 1:
        
        user_card = randint(2,11)
        bot_card = randint(2,11)
        print('you picked ', user_card)
        print('bot picked ', bot_card)
        user_score = user_score + user_card
        bot_score = bot_score + bot_card
        print('your current score is: ', user_score)
        print('bot current score is: ', bot_score)
                       
    elif user_choise == 'pick' and bot_choise == 0:
        
        while user_score < 21 and bot_score < 21:

            if user_choise == 'pick':
                
                user_card = randint(2,11)
                print('you picked ', user_card, ', bot passed')
                user_score = user_score + user_card
                print('your current score is: ', user_score)
                print('bot current score is: ', bot_score, ', bot passed')

            elif user_choise == 'pass':
                print('you passed')
                break
            
            user_choise = input('enter your choise, "pick" or "pass": ')
            
        break
              
    elif user_choise == 'pass' and bot_choise == 1:
        
        print('you passed')
        
        while user_score < 21 and bot_score < 21:
                       
            if bot_choise == 1:
                
                bot_card = randint(2,11)
                print('bot picked ', bot_card)
                bot_score = bot_score + bot_card
                print('bot current score is: ', bot_score,)
                print('your current score is: ', user_score)

            else:
                print('bot passed')
                break
            
            bot_choise = randint(0,1)

        break
            
    elif user_choise == 'pass' and bot_choise == 0:

        print('you passed, bot passed')
        break
		
if user_score > 21 and bot_score > 21:
    print('Both parties lost, your score is: ', user_score, 'bot score is: ', bot_score)

elif user_score > 21 and bot_score <= 21:
    print('You lost, your score is: ', user_score, 'bot score is: ', bot_score)

elif user_score <= 21 and bot_score > 21:
    print('You win, your score is: ', user_score, 'bot score is: ', bot_score)

elif user_score == bot_score:
    print('Both parties win, bot score is: ', bot_score, 'your score is: ', user_score)

elif user_score > bot_score:
    print('Congratulations, your score is: ', user_score, ', you win! Bot score is: ', bot_score)    
        
elif user_score < bot_score:
    print('You lost, your score is: ', user_score, ' bot score is: ', bot_score)


print('GAME OVER')
