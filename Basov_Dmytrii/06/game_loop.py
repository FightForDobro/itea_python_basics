import characters
import enemies
import random
from time import sleep


while True:

    char_race = input('Your race: ').lower()
    char_name = input('Your name: ')

    # Check if char_race exists
    if char_race in characters.RACES:

        # Create main_char instance
        main_char = characters.RACES[char_race](char_name)
        break

    else:
        print('Incorrect input. Choose another race!')

while True:

    char_move = main_char.move()

    # Randomly picked enemy

    if char_move == 'stay':
        main_char.heal()

    else:
        current_enemy = random.choice(enemies.ENEMIES_TYPES)()

        enemy_move = random.choice(current_enemy.enemy_step())
        print(f'Your enemy went {enemy_move}. You are meeting. Good luck:)')

        is_dead = main_char.on_combat(current_enemy)

        if is_dead:
            print('Game over')
            break

    sleep(2)
