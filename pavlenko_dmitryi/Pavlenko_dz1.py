from random import randint

player_card = randint(1, 11) + randint(1, 11)
bot1_card = randint(1, 11) + randint(1, 11)
bot2_card = randint(1, 11) + randint(1, 11)

print (f"You have  {player_card}  points.")

if player_card == 22:
	print ("You winer")
		
else:
	choice = input("Will you draw a card? Enter your answer Y or N : ")

	while choice == "Y" or choice == "y" or choice ==  "yes" :
		
		new_card = randint(1, 11)
		player_card = player_card + new_card
		print (f"You have  {player_card}  points.")
					
		if player_card > 21:
			print ("You lose")
			player_card = 0
			choice = ""	

		else:
			choice = input("Will you draw a card? Enter your answer Y or N : ")

	while choice == "N" or choice == "n" or choice ==  "no" :	
		
		bot1_choice = randint(0, 1)
		bot2_choice = randint(0, 1)

		while bot1_choice == 1:
			bot1_card = bot1_card + randint(1, 11)
			bot1_choice = randint(0, 1)

			if bot1_card > 21:
				print ("Bot1 lose")
				bot1_card = 0


		while bot2_choice == 1:
			bot2_card = bot2_card + randint(1, 11)
			bot2_choice = randint(0, 1)

			if bot2_card > 21:
				print ("Bot2 lose")
				bot2_card = 0

		choice = ""	

if player_card > bot1_card and player_card > bot2_card:
	print ("You winer")	
elif bot1_card > bot2_card and bot1_card > player_card:
	print ("Bot1 winer")	
else:
	print ("Bot2 winer")

