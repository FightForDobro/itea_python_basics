from random import choice


class Bot:
    """
    Describe Bot
    """

    BLACK_PIECE = '○'
    WHITE_PIECE = '●'

    def __init__(self, deck, color):
        """
        Function construct bot
        :param deck: Current deck
        :param color: Bot color
        """

        self.deck = deck
        self.color = color
        self.checkers = []
        self.enemy_checkers = []
        self.moves = []
        self.queen_list = []

    def search_for_checker(self):
        """
        Function search all possible action for bot
        :return:
        """

        for l_index, line in enumerate(self.deck):

            for e_index, element in enumerate(line):

                if element == self.color:

                    self.checkers.append((l_index, e_index))

                elif element != self.color and element != ' ':

                    self.enemy_checkers.append((l_index, e_index))

                elif element == ' ':

                    if l_index - 1 > 0 and e_index - 1 > 0 and l_index + 1 < 8 and e_index + 1 < 8:

                        if self.color == Bot.WHITE_PIECE:

                            if self.deck[l_index - 1][e_index - 1] == self.color or self.deck[l_index - 1][e_index + 1] == self.color:

                                self.moves.append((l_index, e_index))

                        elif self.color == Bot.BLACK_PIECE:

                            if self.deck[l_index + 1][e_index + 1] == self.color or self.deck[l_index + 1][e_index - 1] == self.color:

                                self.moves.append((l_index, e_index))

    def move_bot(self):
        """
        Function describe bot move
        :return: Deck
        :rtype: list
        """

        self.register_queen()

        can_move = self.can_move()
        queen_move = self.move_like_queen()

        if can_move and not queen_move and not self.move_like_queen() and not self.can_attack():
            self.deck[can_move[1][0]][can_move[1][1]] = self.color
            self.deck[can_move[0][0]][can_move[0][1]] = ' '

            self.clears()
            return self.deck

        elif self.attack_like_queen() or queen_move or self.can_attack():

            if queen_move:

                self.deck[queen_move[1][0]][queen_move[1][1]] = self.color
                self.deck[queen_move[0][0]][queen_move[0][1]] = ' '

                self.queen_list.remove((queen_move[0][0], queen_move[0][1]))
                self.queen_list.append((queen_move[1][0], queen_move[1][1]))

            self.clears()
            return self.deck

    def can_move(self, checker=None):
        """
        Function check if bot can move
        :param checker: Checker coordinate
        :return: checker and move
        :rtype: tuple
        """

        self.search_for_checker()

        possible_move = []

        for checker in self.checkers:

            for move in self.moves:

                c_x = checker[0]
                c_y = checker[1]
                m_x = move[0]
                m_y = move[1]

                if self.color == Bot.WHITE_PIECE:

                    if c_x + 1 == m_x and c_y - 1 == m_y and self.deck[m_x][m_y] == ' ' or c_x + 1 == m_x and c_y + 1 == m_y and self.deck[m_x][m_y] == ' ':

                        possible_move.append((checker, move))
                        continue

                elif self.color == Bot.BLACK_PIECE:

                    if c_x - 1 == m_x and c_y - 1 == m_y and self.deck[m_x][m_y] == ' ' or c_x - 1 == m_x and c_y + 1 == m_y and self.deck[m_x][m_y] == ' ':

                        possible_move.append((checker, move))
                        continue
            continue

        return choice(possible_move)

    def can_attack(self):
        """
        Function check if bot can attack
        :return: True or False
        :rtype: bool
        """

        self.search_for_checker()

        for checker in self.checkers:

            for enemy in self.enemy_checkers:

                if self.can_attack_more(checker, enemy):

                    return True

        return False

    def register_queen(self):
        """
        Function make list of all queens
        """

        for checkers in self.checkers:

            if self.color == Bot.WHITE_PIECE and checkers[0] == 7:
                self.queen_list.append(checkers)

            elif self.color == Bot.BLACK_PIECE and checkers[0] == 0:
                self.queen_list.append(checkers)

    def move_like_queen(self):
        """
        Function describe logic of queen moving
        :return:
        """

        if len(self.queen_list) == 0:
            return False

        possible_move = []

        for queen in self.queen_list:

            for move in self.moves:

                q_x = queen[0]
                q_y = queen[1]
                m_x = move[0]
                m_y = move[1]

                if q_x != m_x and q_y != m_y and q_x - m_x == q_y - m_y or q_x - m_x == m_y -q_y:

                    possible_move.append((queen, move))
                    continue

            continue

        if len(possible_move) != 0:

            return choice(possible_move)

    def attack_like_queen(self):
        """
        Function describe logic of queen attack
        """

        if len(self.queen_list) == 0:
            return False

        for queen in self.queen_list:

            for enemy in self.enemy_checkers:

                q_x = queen[0]
                q_y = queen[1]
                e_x = enemy[0]
                e_y = enemy[1]
                try:

                    if q_x != e_x or q_y != e_y and ((q_x - e_x)/2) - e_x > 0 < 8:

                        if self.deck[((q_x - e_x)/2) - e_x][((q_y - e_y)/2) - e_y] == ' ':

                            new_pos = (((q_x - e_x)/2) - e_x, ((q_y - e_y)/2) - e_y)

                            self.deck[q_x][q_y] = ' '
                            self.deck[e_x][e_y] = ' '
                            self.deck[new_pos[0]][new_pos[1]] = self.color

                            return queen, enemy, new_pos

                    return False

                except TypeError:
                    pass

    def clears(self):
        """
        Clear unused list
        """

        self.checkers.clear()
        self.enemy_checkers.clear()
        self.moves.clear()

    def can_attack_more(self, checker, enemy):
        """
        Check if bot can attack again
        :param checker: Checker coordinate
        :param enemy: Enemy coordinate
        :return: True or False
        :rtype: bool
        """

        c_x = checker[0]
        c_y = checker[1]
        e_x = enemy[0]
        e_y = enemy[1]

        if e_x + 1 < 8 and e_y + 1 < 8 and e_x - 1 >= 0 and e_y - 1 >= 0 and self.deck[c_x][c_y] == self.color:

            if c_x - e_x == 1 and c_y - e_y == 1 and self.deck[e_x + 1][e_y + 1] == ' ':  # Up Left

                self.deck[c_x][c_y] = ' '
                self.deck[e_x][e_y] = ' '
                self.deck[e_x - 1][e_y - 1] = self.color

                for enemy in self.enemy_checkers:

                    if self.can_attack_more((e_x - 1, e_y - 1), enemy):

                        return True

                return True

            elif c_x - e_x == 1 and c_y - e_y == -1 and self.deck[e_x - 1][e_y + 1] == ' ':  # Up Right

                self.deck[c_x][c_y] = ' '
                self.deck[e_x][e_y] = ' '
                self.deck[e_x - 1][e_y + 1] = self.color

                for enemy in self.enemy_checkers:

                    if self.can_attack_more((e_x - 1, e_y + 1), enemy):
                        return True

                return True

            elif c_x - e_x == -1 and c_y - e_y == 1 and self.deck[e_x - 1][e_y + 1] == ' ':  # Down left

                self.deck[c_x][c_y] = ' '
                self.deck[e_x][e_y] = ' '
                self.deck[e_x + 1][e_y - 1] = self.color

                for enemy in self.enemy_checkers:

                    if self.can_attack_more((e_x + 1, e_y - 1), enemy):
                        return True

                return True

            elif c_x - e_x == -1 and c_y - e_y == -1 and self.deck[e_x - 1][e_y - 1] == ' ':  # Down right

                self.deck[c_x][c_y] = ' '
                self.deck[e_x][e_y] = ' '
                self.deck[e_x + 1][e_y + 1] = self.color

                for enemy in self.enemy_checkers:

                    if self.can_attack_more((e_x + 1, e_y + 1), enemy):
                        return True

                return True
