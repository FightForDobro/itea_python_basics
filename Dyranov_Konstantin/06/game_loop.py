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

    move = main_char.move()
    fate = random.randint(0, 2)
    if fate == 0:
        healing = main_char.heal()
    elif fate == 1:
        print("safe zone")
    else:
        current_enemy = random.choice(enemies.ENEMIES_TYPES)()
        is_dead = main_char.on_combat(current_enemy)

        if is_dead:
            print('Game over')
            break
