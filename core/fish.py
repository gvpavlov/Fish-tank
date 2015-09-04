from unit import Unit
from sinking_item import SinkingItem
from time import time


class Fish(Unit, SinkingItem):
    def __init__(self, x=0, y=0, direction=(1, 0), size=0):
        radius = (size * 15 + 41) / 2
        Unit.__init__(self, x, y, direction, 80, radius)
        SinkingItem.__init__(self, x, y, 80, radius)
        self.hungry = False
        self.dead = False
        self.growth = 0
        # Fish size: 0 - small, 1 - normal, 2 - big
        self.size = size
        self.last_fed = int(time())

    def starve(self):
        """ Fish starves and changes picture. """
        self.dead = True
        self.state = 'die'
        if self.mirrored:
            self.frame = 720
        else:
            self.frame = 0

    def hungry_check(self):
        """ Chooses fish state depending on last feeding time. """
        if not self.dead:
            hungry_time = int(time()) - self.last_fed + 1
            if hungry_time % 3 == 0:
                self.hungry = True
            if hungry_time % 20 == 0:
                self.starve()

    def eat(self):
        """ Removes hunger, adds to growth and remembers last feed time. """
        self.hungry = False
        self.last_fed = int(time())
        self.growth += 1
        if self.growth == 5 or self.growth == 10:
            self.size += 1
