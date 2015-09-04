from unit import Unit


class Alien(Unit):
    def __init__(self, x=0, y=0, direction=(1, 0), kind=0):
        Unit.__init__(self, x, y, direction, 160, 70)
        self.health = 100
        if kind:
            self.kind = 'lion'
        else:
            self.kind = 'blue'

    def hit(self):
        self.health -= 5

    def dead(self):
        if self.health <= 0:
            return True
        return False
