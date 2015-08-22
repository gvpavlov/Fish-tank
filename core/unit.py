# Basic class for all kinds of fishes and aliens.


class Unit:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        self.x += self.direction[0] * 5
        self.y += self.direction[1] * 5
