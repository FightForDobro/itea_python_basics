from random import randint

#Baner
print("\n______________")
print("_####_____##__")
print("#____#___#_#__")
print("____#______#__")
print("___#_______#__")
print("__#________#__")
print("_#_________#__")
print("######__######\n")

#Game start
print("game start\n")
print("deal the cards.....\n")

#Name player
player_1 = input("Enter your name: ")
while True:
    if not player_1:
        print("Empty name. Please try again: ")
        player_1 = input("Enter your name: ")
        continue
    break

player_2 = "BOT-1"#Bot1 name
player_3 = "BOT-2"#Bot2 name

#Dial 2 cards player_1
card_1, card_2 = int(randint(2, 11)), int(randint(2, 11))
hand_player_1 = card_1 + card_2
print(player_1, "First card:  ", card_1)
print(player_1, "Second card: ", card_2)
if card_1 == card_2 == 11:#2 cards wich value, each cards = 11 "Win
  hand_player_1 = 21

#Dial 2 cards bot1
card_1, card_2 = int(randint(2, 11)), int(randint(2, 11))
hand_player_2 = card_1 + card_2
if card_1 == card_2 == 11:#2 cards wich value, each cards = 11 "Win
    hand_player_2 = 21

#Dial 2 cards bot2
card_1, card_2 = int(randint(2, 11)), int(randint(2, 11))
hand_player_3 = card_1 + card_2
if card_1 == card_2 == 11:#2 cards wich value, each cards = 11 "Win
    hand_player_3 = 21

#Game started
counnter = 18# 18 enough cycles to complete the game
while counnter:

#Player_1
    chois = input(" dial card? press 'y' or and game press 'Enter': ")

    if "y" in chois:
        if hand_player_1 >= 20:
            pass
        else:
            card_3 = randint(2, 11)
            print(card_3)
            hand_player_1 = hand_player_1 + card_3
            counnter = counnter - 1
    elif not chois:
        counnter = counnter - counnter

#Bot1
    while hand_player_2 <= 19:
        thinks = randint(0, 1)
        if thinks == 1 or hand_player_2 < 11:
            hand_player_2 = hand_player_2 + randint(2, 11)
    else:
         pass

#Bot2
    while hand_player_3 <= 19:
        thinks = randint(0, 1)
        if thinks == 1 or hand_player_3 < 11:
            hand_player_3 = hand_player_3 + randint(2, 11)
    else:
         pass

#Result
if hand_player_1 <= 21 and hand_player_2 <= 21 and hand_player_3 <= 21:
    if hand_player_1 >= hand_player_2 and hand_player_1 >= hand_player_3:
        print(player_1, "Win with hand: ", hand_player_1)
        print(player_2, "have hand: ", hand_player_2)
        print(player_3, "have hand: ", hand_player_3)
    else:
        print(player_1, "loose with hand: ", hand_player_1)
        print(player_2, "have hand: ", hand_player_2)
        print(player_3, "have hand: ", hand_player_3)

if hand_player_1 <= 21 and hand_player_2 <= 21 and hand_player_3 > 21:
    if hand_player_1 >= hand_player_2:
        print(player_1, "Win with hand: ", hand_player_1)
        print(player_2, "have hand: ", hand_player_2)
        print(player_3, "have hand: ", hand_player_3)
    else:
        print(player_1, "loose with hand: ", hand_player_1)
        print(player_2, "have hand: ", hand_player_2)
        print(player_3, "have hand: ", hand_player_3)

if hand_player_1 <= 21 and hand_player_2 > 21 and hand_player_3 <= 21:
    if hand_player_1 >= hand_player_3:
        print(player_1, "Win with hand: ", hand_player_1)
        print(player_2, "have hand: ", hand_player_2)
        print(player_3, "have hand: ", hand_player_3)
    else:
        print(player_1, "loose with hand: ", hand_player_1)
        print(player_2, "have hand: ", hand_player_2)
        print(player_3, "have hand: ", hand_player_3)
if hand_player_1 <= 21 and hand_player_2 > 21 and hand_player_3 > 21:
    print(player_1, "Win with hand: ", hand_player_1)
    print(player_2, "have hand: ", hand_player_2)
    print(player_3, "have hand: ", hand_player_3)

if hand_player_1 > 21:
    print(player_1, "Loose with hand: ", hand_player_1)
    print(player_2, "have hand: ", hand_player_2)
    print(player_3, "have hand: ", hand_player_3)
