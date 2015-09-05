from sinking_item import SinkingItem


class Food(SinkingItem):
    def __init__(self, constraint, x=0, y=0):
        SinkingItem.__init__(self, constraint, x, y, 40, 8)
