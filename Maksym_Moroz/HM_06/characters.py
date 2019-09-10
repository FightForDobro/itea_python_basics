import random

class Character:
    """
    Class describes character
    """
    def __init__(self, name):

        self.name = name
        self._hp = 100
        self._damage = 11
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

        self._hp -= enemy.attack()
        is_dead = self.is_dead()

        if is_dead:
            return is_dead

        print(f'Char hp: {self._hp}')
        enemy.take_damage(self._damage)


    def move(self):

        """
        Function to describe move
        :return: Return list
        :rtype: list
        """

        move = ["left", "right", "up", "down"]
        return move


    def heall(self):

        """
        Function to describe variants heall
        :return: Return number
        :rtype: int
        """
        heall = [5, 7, 10]
        return random.choice(heall)


    def heall_take(self):

        self._hp += self.heall()
        return self._hp


class Orc(Character):

    """
    Class to describe Orc race
    """

    def __init__(self, name):

        super().__init__(name)  # call to Character().__init__

        self._hp *= 1.5
        self._damage *= 1.2


class Goblin(Character):

    """
    Class to describe Goblin race
    """

    def __init__(self, name):

        super().__init__(name)  # call to Character().__init__

        self._hp *= 1.9
        self._damage *= 1.1



# races to be checked within a game loop
RACES = {'orc': Orc, 'goblin': Goblin}
