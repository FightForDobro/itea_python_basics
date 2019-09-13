import random


class Character:
    """
    Class describes character
    """
    def __init__(self, name):

        self.name = name
        self._hp = 100
        self._damage = 5

    def is_dead(self):

        """
        Function to check if char is dead
        """

        if self._hp <= 0:
            return True

    def move(self):
        """
        Function to describe move of character
        :return: Function returns player move
        :rtype: str
        """
        movement = input('Where do you want to go? Enter: up, down, left or right. ').lower()
        move_list = ['right', 'left', 'up', 'down']

        if movement in move_list:
            result_move = movement
            print('You are moving', result_move)
        else:
            result_move = 'stay'
            print('You chose to', result_move)

        return result_move

    def on_combat(self, enemy):

        """
        Function to describe fighting
        """

        self._hp -= enemy.attack()
        is_dead = self.is_dead()

        if is_dead:
            return is_dead

        print(f'Char hp: {self._hp}')
        enemy.take_damage(self._damage) 

    def heal(self):
        """
        Function to describe process of hero healing.
        :return: Function returns renewed hp value
        :rtype: int
        """
        heal_points = random.randint(1, 20)
        print(f'You take additional {heal_points} heal points!')
        self._hp += heal_points
        print(f'Current hp: {self._hp}')

        return self._hp


class Orc(Character):

    """
    Class to describe Orc race
    """

    def __init__(self, name):

        super().__init__(name)  # call to Character().__init__

        self._hp *= 1.5
        self._damage *= 1.2


class Human(Character):

    """
    Class to describe Human race
    """


class Elf(Character):

    """
    Class to describe Elf race
    """

    def __init__(self, name):

        super().__init__(name)

        self._hp *= 0.7
        self._damage *= 2.5


# races to be checked within a game loop
RACES = {'orc': Orc, 'human': Human, 'elf': Elf}
