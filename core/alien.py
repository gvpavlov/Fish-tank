from unit import Unit


class Alien(Unit):
    def __init__(self, x=0, y=0, direction=(1, 0), kind=0):
        Unit.__init__(self, x, y, direction, 160, 65)
        if kind:
            self.kind = 'lion'
            self.health = 200
        else:
            self.kind = 'blue'
            self.health = 100

    def hit(self, power):
        self.health -= power

    def is_dead(self):
        if self.health <= 0:
            return True
        return False
