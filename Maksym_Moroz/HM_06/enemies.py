class Enemy:

    def __init__(self):

        self._hp = 10
        self._damage = 20

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


class Underdog(Enemy):

    def __init__(self):

        print('I am underdog')
        super().__init__()
        self._hp *= 1.5
        self._damage *= 1.5

    def on_death(self):
        return 'Aaaaaa'



ENEMIES_TYPES = [Murloc, Undead, Underdog]
