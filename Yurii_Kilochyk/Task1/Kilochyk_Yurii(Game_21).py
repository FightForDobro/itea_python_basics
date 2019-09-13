from random import randint

print ('================================================================================\n')
print ('Card game 21, Blackjack or Ochko\n')
print ('================================================================================\n')

play = input('Will you play: y/n\n')

if play == 'y':
    
    a = input('Enter your name:\n')
    
    while a == False:
        
        print('You did not enter your name!!!')
        a = input('Enter your name:\n')
      
    while a.isalpha() == False:
        
        print('You entered an invalid name!!!')
        a = input('Enter your name correctly:\n')
                
    # bot2_choise = randint(0,1)

    # if bot2_choise == 0:

        # print('Player 2 do not play with you!')
   
    print('\n\n')
    print(a, 'your rivals in the game:\n')
    print('1. Casino') # bot1
    print('2. Vasily Alibabaevich') # bot2
    print ('================================================================================\n')
    print ('Start the game.\n')
    print ('Good luck!!!\n')
    print ('================================================================================\n\n')
  
    user_score = 0
    bot1_score = 0
    bot2_score = 0
    user_card = randint(2,11)
    bot1_card = randint(2,11)
    bot2_card = randint(2,11)
    print('You took card value is', user_card)
    print('Casino took card value is', bot1_card)
    print('Vasily Alibabaevich took card value is', bot2_card)
    user_score = user_score + user_card
    bot1_score = bot1_score + bot1_card
    bot2_score = bot2_score + bot2_card
    print('Your current score is: ', user_score)
    print('Casino current score is: ', bot1_score)
    print('Vasily Alibabaevich current score is: ', bot2_score)

    while user_score < 21 and bot1_score < 21 and bot2_score < 21:

        user_choise = input('\nWill you take a card? y/n\n\n')
               
        if user_choise == 'y':
            
            bot1_choise = 1
            bot2_choise = 1
            user_card = randint(2,11)
            bot1_card = randint(2,11)
            bot2_card = randint(2,11)
            print('You came across a face value card ', user_card)
            print('Casino came across a face value card ', bot1_card)
            print('Vasily Alibabaevich came across a face value card ', bot2_card)
            user_score = user_score + user_card
            bot1_score = bot1_score + bot1_card
            bot2_score = bot2_score + bot2_card
            print('Your current score is: ', user_score)
            print('Casino current score is: ', bot1_score)
            print('Vasily Alibabaevich current score is: ', bot2_score)

        if user_choise == 'n':
            
            bot1_choise = randint(0,1)
            bot2_choise = randint(0,1)
            print ('You refused to draw a card, the move goes to the next player.\n')

            if bot1_choise == 0:
                
                print ('Casino refused to draw a card.\n')
                
            if bot2_choise == 0:
                
                print ('Vasily Alibabaevich refused to draw a card.\n')

            if bot1_choise == 1:
                
                bot1_card = randint(2,11)
                print('Casino came across a face value card ', bot1_card)
                bot1_score = bot1_score + bot1_card
                print('Casino current score is: ', bot1_score)
               
            if bot2_choise == 1:
                
                bot2_card = randint(2,11)
                print('Vasily Alibabaevich came across a face value card ', bot2_card)
                bot2_score = bot2_score + bot2_card
                print('Vasily Alibabaevich current score is: ', bot2_score)

    if user_score == 21:
        
        print ('You win!!!')

    if bot1_score == 21:
        
        print ('Casino win!!!')

    if bot2_score == 21:
        
        print ('Vasily Alibabaevich win!!!')

    if user_score > 21:
        
        print ('You have too much. You lose!!!')

    if bot1_score > 21:
        
        print ('Casino have too much. You lose!!!')

    if bot2_score > 21:
        
        print ('Vasily Alibabaevich have too much. You lose!!!')
                          
print ('================================================================================\n')
print ('Game over! See you next time.\n')
print ('================================================================================\n\n')


