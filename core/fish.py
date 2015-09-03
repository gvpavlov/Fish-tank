from unit import Unit


class Fish(Unit):
    def __init__(self, x=0, y=0, direction=(1, 0), size=0):
        Unit.__init__(self, x, y, direction, 80, (size * 15 + 33) / 2)
        self.hungry = True
        # Fish size: 0 - small, 1 - normal, 2 - big
        self.size = size
