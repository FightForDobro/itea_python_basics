import random
import deck_and_cheez
import bot

colors = ['○', '●']

deck = deck_and_cheez.Deck(random.choice(colors))
checker_pos = deck_and_cheez.CurrentChecker()

player = None
enemy = None


while True:

    print('I greet you in the game of checkers\n '
          'you will play against the most intelligent robot in the universe (No)')
    start = input('Press any button to start')

    if start or not start:
        break

while True:

    print(f'Your color is: {deck.color}')
    deck.print_current_deck()

    if player is None:

        player = deck.color

    elif enemy is None:

        enemy = deck.color

        bott = bot.Bot(deck.deck, enemy)

    if deck.color == player:

        while True:

            checker = input('Choose you checker').upper()

            if len(checker) == 2 and checker[1].isdigit() and deck.check_position(checker):

                if deck.check_checker_pos(checker):

                    current_checker = checker_pos.coord(checker)

                    move_coordinates = input('Enter coordinates').upper()

                    if len(move_coordinates) == 2 and move_coordinates[1].isdigit() and deck.move(move_coordinates, current_checker):

                        deck.change_color()

                        break

            print('You cant move')

    elif deck.color == enemy:

        bott.move_bot()

        deck.deck = bott.deck
        deck.change_color()
        continue
