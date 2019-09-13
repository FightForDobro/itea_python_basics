import characters
import enemies
import random
import pickle
from time import sleep


# -----------------Start Screen-----------------
print('\t\t-/\-/\-/\-Jedi Force Speed-/\-/\-/\-')
print("""
                         .==.
                        ()''()-.
             .---.       ;--; /
           .'_:___". _..'.  __'.
           |__ --==|'-''' \\\'...;
           [  ]  :[|       |---\\
           |__| I=[|     .'    '.
           / / ____|     :       '._
          |-/.____.'      | :       :
         /___\ /___\      '-'._----'
""")
# -----------------------------------------------

# --------------------Choosing Block--------------
while True:

    char_race = list(characters.RACES.keys())

    print(f'You can choose {char_race[0].capitalize()} or {char_race[1].capitalize()}')
    char_race = input('Your race: ').lower()

    if char_race not in characters.RACES:
        continue

    char_name = input('Your name: ')

    # Check if char_race exists
    if char_race in characters.RACES:
        # Create main_char instance
        main_char = characters.RACES[char_race](char_name)
        break
# ----------------------------------------------------------

# ---------------------Default stats------------------------
room = 1
kills = 0
boos_kills = 0
key_list = ('w', 'a', 's', 'd')
boos_raise = 20
item_status = 0
heal_chance = random.randint(0, 4)

with open('stats.dat', 'rb') as f:

    leader_stat = pickle.load(f)
# ----------------------------------------------------------
print(leader_stat)
# --------------------Main Block of Game--------------------
while True:

    key = input('[W] [A] [S] [D]\n').lower()

    # ---------Check if correct key---------
    if key not in key_list:
        print('enter correct key')
        continue
    # -------------------------------------

    # ---------Info about game-----------
    if key == 'w':
        print('You went ahead')
    elif key == 'a':
        print('You went left')
    elif key == 's':
        print('You went backwards')
    elif key == 'd':
        print('You went right')

    print('-----------------------------------')
    print(f'|        You are in room: {room}        |')

    if kills != 0:
        print(f'|       You killed: {kills} enemy\'s      |')
    if boos_kills != 0:
        print(f'|       You killed: {boos_kills} boos\'s       |')
    print('-----------------------------------\n')
    sleep(0.5)
    # -------------------------------------------

    # ---------------Raise boos if you kill more then 20-----------
    if kills > boos_raise:

        is_dead = main_char.on_combat(enemies.Boos())
        boos_raise *= 2  # Make boss more powerful

        if not is_dead:
            boos_kills += 1  # Add statistic
    # --------------------------------------------------------------
    else:
        is_dead = main_char.on_combat(main_char.move(key))

    heal_status = random.randint(0, 4)  # Heal randomazier

    if is_dead:

        with open('stats.dat', 'wb') as f:

            score = int((kills + (boos_kills * 10) + room) / 2 + boos_kills)
            leader_stat[char_name] = score
            pickle.dump(leader_stat, f)

        print('Game over')
        break

    elif not is_dead:

        # Stats
        kills += 1
        room += 1
        # ---------

        # ---- If God of random decides
        if heal_status == heal_chance:
            main_char.heal()
            print('You drink health potion')
            print(f'Current health: {main_char._hp}')

        if kills >= 15:

            item = random.randint(0, 9)

            if item == 5 and item_status == 0:
                item_status += 1
                main_char.item()
                print('You find an item')
                print('You gain powerful power of CrossGuard Sword')
