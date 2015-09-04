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
        self.grow_time = int(time())
        self.drop_coin = False
        # Prevents multiple coin drops in the same second.
        self.coin_drop_time = time()

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
            if hungry_time % 10 == 0:
                self.hungry = True
            if hungry_time % 20 == 0:
                self.starve()

    def eat(self, food):
        """ Removes hunger, adds to growth and remembers last feed time. """
        self.hungry = False
        self.last_fed = int(time())
        self.growth += food
        if self.growth == 5 or self.growth == 10:
            self.grow_time = int(time())
            self.size += 1

    def coin_check(self):
        """ Enables coin drop if it's time. """
        if self.size:
            grown_time = int(time()) - self.grow_time
            if self.coin_drop_time != grown_time and grown_time % 10 == 0:
                self.drop_coin = True
            self.coin_drop_time = grown_time
