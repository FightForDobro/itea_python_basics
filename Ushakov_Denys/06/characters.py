import random
import enemies

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

    def on_combat(self, enemy):

        """
        Function to describe fighting
        """
        while not enemy.is_dead():

            self._hp -= enemy.attack()
            is_dead = self.is_dead()

            if is_dead:
                return is_dead

            print(f'Hero health: {self._hp}')
            enemy.take_damage(self._damage)

    def move(self, key):
        """
        Function describe moving
        """

        key_list = ('w', 'a', 's', 'd')

        if key in key_list:

            current_enemy = random.choice(enemies.ENEMIES_TYPES)()
            print(f'Current enemy: {current_enemy.name}')
            return current_enemy

    def heal(self):
        """
        Healing func
        """

        self._hp += 100

    def item(self):
        """
        Item func
        """

        self._hp += 200
        self._damage *= 2


class Jedi(Character):

    """
    Class to describe Jedi race
    """

    def __init__(self, name):

        super().__init__(name)  # call to Character().__init__

        self._hp *= 2
        self._damage *= 1.5


class Sith(Character):
    """
    Class to describe Sith race
    """

    def __init__(self, name):

        super().__init__(name)

        self._hp *= 1.5
        self._damage *= 2

# races to be checked within a game loop
RACES = {'jedi': Jedi, 'sith': Sith}
