from unit import Unit


class Alien(Unit):
    def __init__(self, x=0, y=0, direction=(1, 0), health=100):
        Unit.__init__(self, x, y, direction)
        self.health = health
        self.previous_direction = direction
        self.frameX = 0
        self.frameY = 0
        self.mirrored = False
        self.mirrored_rotation = False

    def move(self):
        self.move_random()
