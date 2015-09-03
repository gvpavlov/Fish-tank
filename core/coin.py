from sinking_item import SinkingItem


class Coin(SinkingItem):
    def __init__(self, x=0, y=0, worth=0):
        SinkingItem.__init__(self, x, y, 72, 14)
        # Worth: 0 - silver coin, 1 - golden coin
        self.worth = worth
