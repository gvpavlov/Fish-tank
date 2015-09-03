from unit import Unit


class Fish(Unit):
    def __init__(self, x=0, y=0, direction=(1, 0), size=0):
        Unit.__init__(self, x, y, direction)
        self.hungry = False
        # Fish size: 0 - small, 1 - normal, 2 - big
        self.size = size

    def move(self):
        self.move_random()
