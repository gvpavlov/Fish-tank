from unit import Unit
from sinking_item import SinkingItem
from time import time

class Fish(Unit, SinkingItem):
    def __init__(self, x=0, y=0, direction=(1, 0), size=0):
        radius = (size * 15 + 33) / 2
        Unit.__init__(self, x, y, direction, 80, radius)
        SinkingItem.__init__(self, x, y, 80, radius)
        self.hungry = True
        # Fish size: 0 - small, 1 - normal, 2 - big
        self.size = size
        self.spawn_time = time()

    def starve(self):
        """ Fish starves if not fed in time and drops to the bottom. """
        self.dead = True
        self.state = 'die'
        self.frame = 0

