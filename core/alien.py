from unit import Unit


class Alien(Unit):
    def __init__(self, x=0, y=0, direction=(1, 0), kind='blue'):
        Unit.__init__(self, x, y, direction, 160, 70)
        self.health = 100
        self.kind = kind
