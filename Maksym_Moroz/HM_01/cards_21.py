from random import randrange

while True: # main cycle

    print("Game starting...")

    chance_1 = randrange(2, 12) #first card
    chance_2 = randrange(2, 12) # second card
    my_score = chance_1 + chance_2 # player score
    score_bot1 = 0 # first bot score
    score_bot2 = 0 # second bot score

    print("Your first card is", chance_1)

    print("Your second card is", chance_2)

    print("You have", my_score, "score!") # print score after 2 cards

    while my_score <= 21: # players logic

        if my_score == 20 or my_score == 21:

            break

        if my_score <= 19:

            question = input("Need card? (Enter no or yes) \n")

            if question == "yes":

                chance = randrange(2, 12) # card in cycle
                my_score = my_score + chance

                print("You card is ", chance)

            elif question == "no":

                print("You have", my_score, "score!") # print score if player has enough cards

                break

            else:

                print("You answer is incorrect. Please try again enter yes or no!")

        print("You have", my_score, "score!") # print score after next card





    while True: # first bot logic (if bot has <= 16 points - it will play, if bot has >= 17 points, it will pass)

        chance_bot1 = randrange(2, 12) # bot's card in cycle
        score_bot1 = score_bot1 + chance_bot1

        print("First bot's card is", chance_bot1) # each card

        print("First bot has", score_bot1, "score!") # print score after each card


        if score_bot1 >= 16:

            break

    while True: # second bot logic (if <= 16 points - it play, if 17 and 18 points - random make disitiond (if "0" - pass, if "1" - play), if 19, 20, 21 points - pass )

        chance_bot2 = randrange(2, 12) # bot's card in cycle
        score_bot2 = score_bot2 + chance_bot2
        weight = randrange(0, 2) # random weight make disition

        print("Second bot's card is", chance_bot2) # each card

        print("Second bot has", score_bot2, "score!") # print score after each card

        if weight == 1 and score_bot2 == 18:

            break

        if weight == 1 and score_bot2 == 17:

            break

        if score_bot2 >= 19:

            break
# print all score
    print ("You  = ", my_score)

    print ("Bot1 = ", score_bot1)

    print ("Bot2 = ", score_bot2)

    question_end = input("New game? (Enter no or yes) \n") # question about next game?

    while question_end != "yes" and question_end != "no": # answer logic

        print("You answer is incorrect. Please try again enter yes or no!")

        question_end = input("New game? (Enter no or yes) \n")

    if question_end == "yes":

        print("Mew game!")

    if question_end == "no":

        print("Game end!")

        break
