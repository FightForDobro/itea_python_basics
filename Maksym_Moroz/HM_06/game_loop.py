import characters
import enemies
import random
from time import sleep


char_race = input('Your race:\n')
char_name = input('Your name:\n')

# Check if char_race exists
if char_race in characters.RACES:

    # Create main_char instance
    main_char = characters.RACES[char_race](char_name)


while True:

    char_name = input('Your step (left/right/up/down:\n')
    char_name = char_name.lower()

    if char_name in main_char.move():

        step = random.choice(main_char.move())

        if char_name == step:

            # Randomly picked enemy
            current_enemy = random.choice(enemies.ENEMIES_TYPES)()

            is_dead = main_char.on_combat(current_enemy)

            if is_dead:
                print('Game over')
                break

            sleep(5)

        else:
            main_char.heall_take()
            print(main_char.heall_take())



    else:
        print("Your step isn't valid")




    
    



