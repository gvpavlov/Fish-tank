from unit import Unit


class Alien(Unit):
    def __init__(self, x=0, y=0, direction=(1, 0), kind=0):
        Unit.__init__(self, x, y, direction, 160, 65)
        self.health = 100
        if kind:
            self.kind = 'lion'
        else:
            self.kind = 'blue'

    def hit(self):
        self.health -= 10

    def is_dead(self):
        if self.health <= 0:
            return True
        return False
