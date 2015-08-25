from unit import Unit


class Alien(Unit):
    def __init__(self, x=0, y=0, direction=(1, 0), health=100):
        Unit.__init__(self, x, y, direction)
        self.health = health

    def move(self):
        self.move_random()
