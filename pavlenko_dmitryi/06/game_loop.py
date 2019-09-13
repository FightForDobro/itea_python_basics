import characters
import enemies
import random
from time import sleep


char_race = input('Your race: ')
char_name = input('Your name: ')

# Check if char_race exists
if char_race in characters.RACES:

    # Create main_char instance
    main_char = characters.RACES[char_race](char_name)

while True:

    char_choise = input('will you move, Yes or No ? ')

    if char_choise.lower() == "yes":

        player_step = main_char.move()
        print (player_step)

        current_enemy = random.choice(enemies.ENEMIES_TYPES)()
        is_dead = main_char.on_combat(current_enemy)

        if is_dead:
            print('Game over')
            break


    elif char_choise.lower() == "no":

        heal_char = random.randint(0, 1)

        if heal_char == 1:
            heal = main_char.heal()


    else:
        print("repeat your choice")
        continue

    sleep(5)
        



    
    



