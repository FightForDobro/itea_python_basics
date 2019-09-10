
print('\t The game of 21 \n')

from random import randint

card_1, card_2 = randint(2, 11), randint(2, 11) # multiple assignment

summ = card_1 + card_2

cards_left = 8

while cards_left != 0: #number of attemps / or number of cards
    
    if card_1 == card_2 == 11 :
        print('You have a jackpot!!!')
        break

    elif summ == 21:
        print('You win! Your total SUM is', summ)
        break

    elif summ > 21:
        print('You lose :( Your SUM is ', summ)
        break

    else: # summ < 21: 

        print('You have ', summ, ' in total.\n')
        
        pick = input(r'Do you want to continue? Y\N :')

        while True:

            if not (pick == 'Y' or pick == 'y' or pick == 'N' or pick == 'n'):
                print('Please input \'Y\' or \'N\'')
                pick = input(r'Do you want to continue? Y\N :')
            else:
                break


        if pick == 'Y' or pick ==  'y':
            
            cards_left -= 1

            card_new = randint(2, 11)

            summ += card_new 
          
        else:
            break
     
print('Turn is switched to the next player -> \n')


#----------------------------------
# Player_1
#----------------------------------

card_3, card_4 = randint(2, 11), randint(2, 11) 

summ_1 = card_3 + card_4

cards_left_1 = 8

print('The Players_1 first SUM is', summ_1) #check for sum

picker = 1

while cards_left_1 != 0 and picker == 1:

    picker = randint(0,1)
    print('The player pick ', picker, 'cards.') #check for pick
    
    if card_3 == card_4 == 11 :
        print('Player_1 has a jackpot!!!')
        break

    elif summ_1 == 21:
        print('Player_1 has 21!')
        break

    elif summ_1 > 21:
        print('Player_1 lost :)')
        break

    else:

        if picker == 1:
            
            cards_left_1 -= 1

            card_new_1 = randint(2, 11)

            summ_1 += card_new_1 
          

print('The Players_1 total SUM is ', summ_1) #check for exit sum

print('Turn is switched to the next player -> \n')



'''
    # The solvetion for 2 players
   
if summ > summ_1:
    print('You win the game!')

elif summ == summ_1:
    print('You are equal')

else:
    print('You lose sucker!')

print('Game over')

'''



#----------------------------------
# Player_2 or Croupier
#----------------------------------

card_5, card_6 = randint(2, 11), randint(2, 11) 

summ_2 = card_5 + card_6

cards_left_2 = 8

print('The Players_2 first SUM is', summ_2) #check for sum

picker_2 = 1

while cards_left_2 != 0 and picker_2 == 1:

    picker_2 = randint(0,1)
    
    print('The player pick ', picker_2, 'cards.') #check for pick
    
    if card_5 == card_6 == 11 :
        print('Player_2 has a jackpot!!!')
        break

    elif summ_2 == 21:
        print('Player_2 has 21!')
        break

    elif summ_2 > 21:
        print('Player_2 lost :)')
        break

    else:

        if picker_2 == 1:
            
            cards_left_2 -= 1

            card_new_2 = randint(2, 11)

            summ_2 += card_new_2 
          
print('The Players_2 total SUM is ', summ_2, '\n') #check for exit sum



#----------------------------------
# Results of the whole game
#----------------------------------



if summ == summ_1 == summ_2 <= 21:
    print('It is a miracle! Everybody won!')


if summ <=21 and summ_1 <=21 and summ_2 <=21:

    if summ > summ_1 and summ > summ_2:
        print('You win the game!')

    elif summ_1 > summ and summ_1 > summ_2:
        print('Player_1 win the game!')

    elif summ_2 > summ and summ_2 > summ_1:
        print('Player_2 win the game!')

    elif summ_2 == summ_1 and summ_2 > summ:
        print('Player_1 and Player_2 are equal, but You lose(')
    
    elif summ_2 == summ and summ_2 > summ_1:
        print('You and Player_2 are equal, but Player_1 lose')
        
    elif summ_1 == summ and summ_1 > summ_2:
        print('You and Player_1 are equal, but Player_1 lose')



# if summ or summ_1 or summ_2 > 21:

if summ > 21 or summ_1 > 21 or summ_2 > 21:
    
    if summ > 21 :
        
        if (summ > 21 and summ_1 > 21) and summ_2 <= 21:
            print('Player_2 win the game!')

        elif summ_1 > summ_2 and (summ_1 <= 21 and summ_2 <= 21):
            print('Player_1 win the game!')
            
        elif summ_2 > summ_1 and (summ_1 <= 21 and summ_2 <= 21):
            print('Player_2 win the game!')

        elif summ_2 == summ_1 and (summ_1 <= 21 and summ_2 <= 21):
            print('Player_1 and Player_2 are equal')

    if summ_1 > 21 :

        if (summ_1 > 21 and summ_2 > 21) and summ <= 21:
            print('You win the game!')

        elif summ > summ_2 and (summ <= 21 and summ_2 <= 21):
            print('You win the game!')
            
        elif summ_2 > summ and (summ <= 21 and summ_2 <= 21):
            print('Player_2 win the game!')
            
        elif summ_2 == summ and (summ <= 21 and summ_2 <= 21):
            print('You and Player_2 are equal')

    if summ_2 > 21 :
        
        if (summ > 21 and summ_2 > 21) and summ_1 <= 21:
            print('Player_1 win the game!')
            
        elif summ > summ_1 and (summ <= 21 and summ_1 <= 21):
            print('You win the game!')
            
        elif summ_1 > summ and (summ <= 21 and summ_1 <= 21):
            print('Player_1 win the game!')
                    
        elif summ_1 == summ and (summ <= 21 and summ_1 <= 21):
            print('You and Player_1 are equal')



print('\n-----------\n Game over \n-----------\n')

