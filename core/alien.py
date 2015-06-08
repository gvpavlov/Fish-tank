import unit


class Alien(Unit):
    def __init__(self, x=0, y=0, direction="right", health=100):
        Unit.__init__(self, x, y, direction)
        self.health = health
