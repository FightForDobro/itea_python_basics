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

        self._hp -= enemy.attack()
        is_dead = self.is_dead()

        if is_dead:
            return is_dead

        print(f'Char hp: {self._hp}')
        enemy.take_damage(self._damage)

    def move(self):

        """
        Function to describe move
        """
        Choose_move = input("Choose move(up, down, left, right")
        move = ["up", "left", "right", "down"]
        if Choose_move in move:
            return Choose_move


    def heal(self):

        """
        Function to heal
        """

        self._hp += 10

        return print(f"hp {self._hp}")


class Orc(Character):

    """
    Class to describe Orc race
    """

    def __init__(self, name):

        super().__init__(name)  # call to Character().__init__

        self._hp *= 1.5
        self._damage *= 1.2

class Undead(Character):
    """
    Class to describe Undead race
    """
    def __init__(self, name):
        super().__init__(name)

        self._hp *= 1.5
        self._damage *= 1.1



# races to be checked within a game loop
RACES = {'orc': Orc, 'Undead': Undead}
