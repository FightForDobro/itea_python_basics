class Deck:

    BLACK_PIECE = '○'
    WHITE_PIECE = '●'

    def __init__(self, color):
        """
        Function construct deck and store current information about checkers
        :param color: color of your checkers
        :rtype: str
        """

        self.deck = [[' ', '●', ' ', '●', ' ', '●', ' ', '●'],
                     ['●', ' ', '●', ' ', '●', ' ', '●', ' '],
                     [' ', '●', ' ', '●', ' ', '●', ' ', '●'],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                     ['○', ' ', '○', ' ', '○', ' ', '○', ' '],
                     [' ', '○', ' ', '○', ' ', '○', ' ', '○'],
                     ['○', ' ', '○', ' ', '○', ' ', '○', ' ']]

        self.color = color

        self.w_checker = []
        self.b_checker = []
        self.queen_list = []

    def print_current_deck(self):
        """
        Function prints current deck
        """

        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
        letter_count = 0

        print(f'\t {" ".join(numbers)}\n')

        for line in self.deck:

            a = '|'.join(line)
            print(f'{letters[letter_count]}\t|{a}|\t{letters[letter_count]}')
            letter_count += 1

        print(f'\n\t {" ".join(numbers)}')

    def __coordinates(self, usr_inp):
        """
        Function user friendly input to computer
        :param usr_inp: Coordinate of cell
        :return: x and y coordinate
        :rtype: tuple
        """

        dict_pos = {'A': 0,
                    'B': 1,
                    'C': 2,
                    'D': 3,
                    'E': 4,
                    'F': 5,
                    'G': 6,
                    'H': 7
                    }

        if usr_inp[0] not in dict_pos.keys():

            return False

        x = dict_pos[usr_inp[0]]
        y = int(usr_inp[1])

        return x, y - 1

    def check_position(self, usr_inp):

        """
        Function checks whether coordinates are correct or not
        :param usr_inp: Coordinates
        :return: Coordinates
        :rtype: tuple
        """

        coordinates = self.__coordinates(usr_inp)

        if not coordinates:

            print('Invalid letter')
            return False

        elif coordinates[0] < 0 or coordinates[1] < 0:

            print('Your coordinates is negative')
            print('Please enter correct coordinate')
            return False

        elif coordinates[0] > 8 or coordinates[1] > 8:

            print('Your coordinates out from scope')
            print('Please enter correct coordinate')
            return False

        return coordinates

    def calculate_possible_moves(self):
        """
        Function calculates white and black checkers and possible move for them
        :return:
        """

        self.w_checker.clear()
        self.b_checker.clear()

        for l_index, line in enumerate(self.deck):

            for e_index, element in enumerate(line):

                if element == Deck.WHITE_PIECE:
                    self.w_checker.append((l_index, e_index))

                elif element == Deck.BLACK_PIECE:
                    self.b_checker.append((l_index, e_index))


    def calculate_possible_move_for_check(self, usr_inp, cur_check):
        """
        Function calculates possible move for each checker
        :param usr_inp: Coordinate of move
        :param cur_check: Coordinate of checker
        :return: True or False
        :rtype: bool
        """

        if self.color == Deck.WHITE_PIECE:

            if self.deck[cur_check[0]][cur_check[1]] == self.color:

                if usr_inp[0] == cur_check[0] + 1:

                    if usr_inp[0] > cur_check[0] and sum(usr_inp) == sum(cur_check):  # Left variant

                        if self.check_cell(usr_inp):
                            return False

                        return True

                    elif usr_inp[0] > cur_check[0] and sum(usr_inp) == sum(cur_check) + 2:  # Right variant

                        if self.check_cell(usr_inp):
                            return False

                    return True

                else:

                    return False

        elif self.color == Deck.BLACK_PIECE:

            if usr_inp[0] == cur_check[0] - 1:

                if usr_inp[0] < cur_check[0] and sum(usr_inp) == sum(cur_check) - 2:  # Left variant

                    if self.check_cell(usr_inp):

                        return False

                    return True

                elif usr_inp[0] < cur_check[0] and sum(usr_inp) == sum(cur_check):  # Right variant

                    if self.check_cell(usr_inp):

                        return False

                    return True

            else:

                return False

    def attack(self, usr_inp, cur_check):
        """
        Function describe attack
        :param usr_inp: Coordinate of move
        :param cur_check: Coordinate of checker
        :return: True or False
        :rtype: bool
        """

        u_x = usr_inp[0]
        u_y = usr_inp[1]

        c_x = cur_check[0]
        c_y = cur_check[1]

        if u_x - 1 >= 0 and u_y - 1 >= 0 and u_x + 1 < 8 and u_y + 1 < 8 and\
                c_x - 1 >= 0 and c_y - 1 >= 0 and c_x + 1 < 8 and c_y + 1 < 8:

            if self.deck[u_x][u_y] != ' ' and self.deck[u_x][u_y] != self.color:

                if self.deck[u_x - 1][u_y + 1] == ' ':  # Up right

                    if self.deck[c_x - 1][c_y + 1] != ' ' and self.deck[c_x - 1][c_y + 1] != self.color:

                        if u_x == c_x - 1 and u_y == c_y + 1:

                            self.deck[c_x][c_y] = ' '
                            self.deck[u_x][u_y] = ' '
                            self.deck[u_x - 1][u_y + 1] = self.color

                            return True

            if self.deck[u_x - 1][u_y - 1] == ' ':  # Up left

                if self.deck[c_x - 1][c_y - 1] != ' ' and self.deck[c_x - 1][c_y - 1] != self.color:

                    if u_x == c_x - 1 and u_y == c_y - 1:

                        self.deck[c_x][c_y] = ' '
                        self.deck[u_x][u_y] = ' '
                        self.deck[u_x - 1][u_y - 1] = self.color

                        return True

            if self.deck[u_x + 1][u_y - 1] == ' ':  # Down left

                if self.deck[c_x + 1][c_y - 1] != ' ' and self.deck[c_x + 1][c_y - 1] != self.color:

                    if u_x == c_x + 1 and u_y == c_y - 1:

                        self.deck[c_x][c_y] = ' '
                        self.deck[u_x][u_y] = ' '
                        self.deck[u_x + 1][u_y - 1] = self.color

                        return True

            if self.deck[u_x + 1][u_y + 1] == ' ':  # Down right

                if self.deck[c_x + 1][c_y + 1] != ' ' and self.deck[c_x + 1][c_y + 1] != self.color:

                    if u_x == c_x + 1 and u_y == c_y + 1:

                        self.deck[c_x][c_y] = ' '
                        self.deck[u_x][u_y] = ' '
                        self.deck[u_x + 1][u_y + 1] = self.color

                        return True

        else:

            print('You cant attack')
            return False

    def move(self, usr_inp, cur_check):
        """
        Function describe move and this function main in module
        all magic starst from here
        :param usr_inp: String user friendly coordinate
        :param cur_check: Coordinate
        :return: True or False
        :rtype: bool
        """

        coordinate = self.check_position(usr_inp)

        if not coordinate:
            return False

        move_coordinates = tuple(coordinate)

        if self.is_queen(cur_check) or cur_check in self.queen_list:

            print('You choose a Queen')

            if self.play_like_a_queen(move_coordinates, cur_check):

                self.queen_list.remove(cur_check)
                self.queen_list.append(move_coordinates)

                return True

            return False

        self.calculate_possible_moves()

        moves = self.calculate_possible_move_for_check(move_coordinates, cur_check)

        attack_list = self.attack_list()

        if moves:

            if len(attack_list) == 0:

                if not self.attack(move_coordinates, cur_check):

                    self.deck[move_coordinates[0]][move_coordinates[1]] = self.color

                    self.deck[cur_check[0]][cur_check[1]] = ' '

                    return True

            elif len(attack_list) > 0 and not self.attack(move_coordinates, cur_check):

                print('You must attack')

                return False

            while len(self.attack_list()) > 0 and cur_check in attack_list:

                self.print_current_deck()

                print(self.color)
                self.move(input('Next attack').upper(), self.__calculate_new_cords(move_coordinates, cur_check))

            return True

        elif not moves:

            if len(attack_list) > 0:

                if self.attack(move_coordinates, cur_check):

                    return True

                print('You must attack')

                return False

            while len(attack_list) > 0:

                self.print_current_deck()

                print(self.color)

                new_move = input('Next attack').upper()

                self.move(new_move, self.__calculate_new_cords(move_coordinates, cur_check))

                return True

            return False

    def check_checker_pos(self, usr_inp):
        """
        Function check if checker in cell
        :param usr_inp: Move coordinate
        :return: coordinate
        :rtype:tuple
        """

        coordinates = self.__coordinates(usr_inp)

        if self.deck[coordinates[0]][coordinates[1]] == '':

            print('Is no checker here')
            print('Please enter correct coordinate')

            return False

        return coordinates

    def change_color(self):
        """
        Function change color
        :return:
        """

        if self.color == Deck.WHITE_PIECE:
            self.color = Deck.BLACK_PIECE

        else:
            self.color = Deck.WHITE_PIECE

    def check_cell(self, usr_inp):
        """
        Function check if cell is empty
        :param usr_inp: Move coordinate
        :return: True or False
        :rtype: bool
        """

        if self.deck[usr_inp[0]][usr_inp[1]] != ' ' and len(self.attack_list()) == 0:

            print('This cell is field')
            print('Please enter correct coordinate')

            return True

        return False

    def can_attack(self, cur_check):

        """
        Function check if checker can attack
        :param cur_check: Checker coordinate
        :return: True or False
        :rtype: bool
        """

        x = cur_check[0]
        y = cur_check[1]

        if x - 2 >= 0 or y - 2 >= 0 and x + 2 < 8 or y + 2 < 8:

            if x - 2 >= 0 and y - 2 >= 0 and self.deck[x - 1][y - 1] != ' ' and \
                    self.deck[x - 1][y - 1] != self.color and self.deck[x - 2][y - 2] == ' '\
                    and self.deck[x][y] == self.color and x - 1 >= 0 and y - 1 >= 0:  # Left up

                return True

            if x - 2 >= 0 and y + 2 < 8 and self.deck[x - 1][y + 1] != ' ' and \
                    self.deck[x - 1][y + 1] != self.color and self.deck[x - 2][y + 2] == ' '\
                    and self.deck[x][y] == self.color and x - 1 >= 0 and y + 1 < 8:  # Right up

                return True

            if x + 2 < 8 and y - 2 >= 0 and self.deck[x + 1][y - 1] != ' ' and \
                    self.deck[x + 1][y - 1] != self.color and self.deck[x + 2][y - 2] == ' '\
                    and self.deck[x][y] == self.color and x + 1 < 8 and y >= 0:  # Down left

                return True

            if x + 2 < 8 and y + 2 < 8 and self.deck[x + 1][y + 1] != ' ' and \
                    self.deck[x + 1][y + 1] != self.color and self.deck[x + 2][y + 2] == ' '\
                    and self.deck[x][y] == self.color and x + 1 < 8 and y + 1 < 8:  # Down right

                return True

        return False

    def attack_list(self):

        """
        Function generate attack list
        :return: attack list
        :rtype: list
        """

        self.calculate_possible_moves()

        if self.color == Deck.WHITE_PIECE:

            attack_list = []

            for coordinate in self.w_checker:

                if self.can_attack(coordinate):

                    attack_list.append(coordinate)

        elif self.color == Deck.BLACK_PIECE:

            attack_list = []

            for coordinate in self.b_checker:

                if self.can_attack(coordinate):

                    attack_list.append(coordinate)

        return attack_list

    def __calculate_new_cords(self, usr_inp, cur_check):

        """
        Calculate new coordinate for current checker
        :param usr_inp: Move coordinate
        :param cur_check: Checker coordinate
        :return: x and y coordinate
        :rtype: tuple
        """

        u_x = usr_inp[0]
        u_y = usr_inp[1]

        c_x = cur_check[0]
        c_y = cur_check[1]

        a = -((u_x - c_x) * 2)
        b = -((u_y - c_y) * 2)

        x = c_x - a
        y = c_y - b

        return x, y

    def is_queen(self, cur_check):
        """
        Function check if checker is a queen
        :param cur_check: Current checker
        :return: True or false
        :rtype: bool
        """

        if self.color == Deck.WHITE_PIECE and cur_check[0] == 7:

            self.queen_list.append(cur_check)

            return True

        elif self.color == Deck.BLACK_PIECE and cur_check[0] == 0:

            self.queen_list.append(cur_check)

            return True

        return False

    def play_like_a_queen(self, usr_inp, cur_check):
        """
        Function describe queen logic
        :param usr_inp: Move coordinate
        :param cur_check: Checker coordinate
        :return: True or False
        :rtype: bool
        """

        u_x = usr_inp[0]
        u_y = usr_inp[1]

        c_x = cur_check[0]
        c_y = cur_check[1]

        if u_x != c_x or u_y != c_y:

            if self.deck[u_x][u_y] == self.color:
                print('You cant move on self checker')

            elif self.deck[u_x][u_y] != self.color and self.deck[u_x][u_y] != ' ' and\
                    u_x - 1 >= 0 and u_y - 1 >= 0 and u_x + 1 < 8 and u_y + 1 < 8 and\
                    c_x - 1 >= 0 and c_y - 1 >= 0 and c_x + 1 < 8 and c_y + 1 < 8:

                    if self.deck[u_x - 1][u_y - 1] == ' ':  # Up Left

                        self.deck[u_x - 1][u_y - 1] = self.color
                        self.deck[u_x][u_y] = ' '

                        return True

                    elif self.deck[u_x - 1][u_y + 1] == ' ':  #Up Right

                        self.deck[u_x - 1][u_y + 1] = self.color
                        self.deck[u_x][u_y] = ' '

                        return True

                    elif self.deck[u_x + 1][u_y - 1] == ' ':  #Down left

                        self.deck[u_x + 1][u_y - 1] = self.color
                        self.deck[u_x][u_y] = ' '

                        return True

                    elif self.deck[u_x + 1][u_y + 1] == ' ':  # Down left

                        self.deck[u_x + 1][u_y + 1] = self.color
                        self.deck[u_x][u_y] = ' '

                        return True

            else:

                self.deck[u_x][u_y] = self.color

                self.deck[c_x][c_y] = ' '

                return True

    def is_exit(self, usr_inp):
        """
        Function describe exit from input
        :param usr_inp: Some input
        :return: True or False
        :rtype: bool
        """

        if usr_inp == 'R':
            return True


class CurrentChecker:
    """
    Descibe current checker
    """

    def __init__(self, coordinates=None):
        """
        Construct current checker
        :param coordinates:
        """

        self.coordinates = coordinates

    def coord(self, usr_inp):
        """
        Function get correct coordinate
        :param usr_inp: Coordinate of checker
        :return: Coordinates
        :rtype: tuple
        """

        cords = Deck(1).check_position(usr_inp)

        self.coordinates = cords

        return self.coordinates

