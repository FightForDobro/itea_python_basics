class Enemy:

    def __init__(self):

        self._hp = 10
        self._damage = 20

    def enemy_step(self):
        """
        Function to describe move of character
        :return: Function returns list of bot enemies possible movements
        :rtype: list
        """
        move_list = ['right', 'left', 'up', 'down']
        return move_list

    def attack(self):

        return self._damage

    def take_damage(self, damage):

        self._hp -= damage
        is_dead = self.is_dead()

        if is_dead:
            print(self.on_death())
            return is_dead

        print(f'Enemy hp: {self._hp}')

    def is_dead(self):

        if self._hp <= 0:
            return True

    def on_death(self):

        print('I am dead')


class Murloc(Enemy):

    def __init__(self):

        print('I am murloc')
        super().__init__()
        self._hp *= 0.5
        self._damage *= 0.5

    def on_death(self):
        return 'Mrglglglg'


class Undead(Enemy):

    def __init__(self):

        print('I am undead')
        super().__init__()
        self._hp *= 1.2
        self._damage *= 1.1

    def on_death(self):
        return 'Uuuuuh'


class Goblin(Enemy):

    def __init__(self):

        print('I\'m Goblin')
        super().__init__()
        self._hp *= 0.8
        self._damage *= 1.5

    def on_death(self):
        return 'Brrrrrrrr'


class Dragon(Enemy):

    def __init__(self):

        print('Aaahh!!! I am dragon')
        super().__init__()
        self._hp *= 4
        self._damage *= 2.5

    def on_death(self):
        return 'Ssshhhhhhhh'


ENEMIES_TYPES = [Murloc, Undead, Goblin, Dragon]
