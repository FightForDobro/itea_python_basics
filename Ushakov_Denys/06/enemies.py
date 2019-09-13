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
            print('\nYou killed enemy:')
            print(self.on_death())
            return is_dead

        print(f'Enemy health: {self._hp}')

    def is_dead(self):

        if self._hp <= 0:
            return True

    def on_death(self):
        print('I am dead')


class BattleDorid(Enemy):

    def __init__(self):

        self.name = 'Battle Droid l-33-t'
        print('beep-beep... I am battle droid l-33-t')
        print('You will give your life for the life of the empire\n')
        super().__init__()
        self._hp *= 1.5
        self._damage *= 0.5

    def on_death(self):
        return 'E 010110110101101101011000 R'


class AssasinDroid(Enemy):

    def __init__(self):

        self.name = 'Assassin Droid IG-88'
        print('beep... Im an Assassin Droid')
        print(f'Im here to kill you\n')
        super().__init__()
        self._hp *= 1.5
        self._damage *= 1.1

    def on_death(self):
        return 'ERROR: 2B585E575D62'


class Boos(Enemy):

    def __init__(self):

        self.name = 'General Grievous'
        print('''        I'm no errand boy. 
        And I'm not in this war for Dooku's politics. 
        I am the leader of the most powerful droid army the galaxy has ever seen!\n''')
        super().__init__()
        self._hp *= 5
        self._damage *= 1.5

    def on_death(self):
        self._hp *= 2
        self._damage *= 2

        return f'We are not done....'


ENEMIES_TYPES = [BattleDorid, AssasinDroid]
