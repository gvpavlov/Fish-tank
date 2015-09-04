from sinking_item import SinkingItem


class Food(SinkingItem):
    def __init__(self, x=0, y=0):
        SinkingItem.__init__(self, x, y, 40, 5)
