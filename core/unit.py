# Basic class for all kinds of fishes and aliens.
class Unit:
    def __init__(self, x=0, y=0, direction="right"):
        self.x = x
        self.y = y
        self.direction = direction
