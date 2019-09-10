import  random
"""Greeting"""
print('Welcome to the game')
input('Press enter to start')


"""Assign the value to the variables using random"""
first_card = random.randint(1, 11)
second_card = random.randint(1, 11)
sum_cards = 0

bot_first_card = random.randint(1, 11)
bot_sum_cards = 0


"""Display the values ??of the maps on the screen"""
print('Your first card is:' + str(first_card) +'\n' + 'Your second card is:' + str(second_card))
sum_cards = first_card + second_card
print('Now your score is',sum_cards)

bot_sum_cards = 0
print('Bot`s first card is', bot_first_card)


"""Asking the user about an extra card"""
if sum_cards  != 21:
  extra_question = (input('Want more? Press "1" Is it enough press "0"'))
else:
  print('You have winier score ,wait for bot')
bot_extra_card_question = True


if extra_question == "1":
  extra_question_bool = True
  while extra_question_bool:
    extra_card = random.randint(1, 11)
    sum_cards = sum_cards + extra_card
    print('Now your score is',sum_cards)

    if sum_cards > 21:
      print('You lose')
      extra_question_bool = False
      break

    extra_question = (input('Want more? Press "1" Is it enough press "0"'))
    if extra_question == "1":
      extra_question_bool = True
    else:
      extra_question_bool = False


"""Bot playing"""

while bot_extra_card_question:
  bot_extra_card = random.randint(1, 11)
  bot_sum_cards = bot_first_card + bot_extra_card
  if bot_sum_cards > 21:
    print('Bot lose')
    break
  elif sum_cards == 21 and (bot_sum_cards < 21 or bot_sum_cards > 21):
    print('You win')
    break
  elif bot_sum_cards == 21 and sum_cards != 21:
    print('Bot win')
    break
  elif bot_sum_cards == sum_cards:
    print("Draw")
    break
  elif bot_sum_cards < sum_cards and sum_cards < 21:
    print('Bot lose')
  else:
    print('Bot win')
  bot_extra_card_question = random.choice([True, False])
print('Bot score is: ',bot_sum_cards)
print('Yuor score is: ',sum_cards)

