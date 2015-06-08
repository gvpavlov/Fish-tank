import unit


class GoldFish(Unit):
    def __init__(self, x=0, y=0, direction="right", hunger=0):
        Unit.__init__(self, x, y, direction)
        self.hunger = hunger
