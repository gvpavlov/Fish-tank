class SinkingItem:
    """ Combines food and coin common trades. """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sinking = True
        self.frame = 0

    """ Sinks the item and says if it can keep sinking. """
    def sink(self):
        self.y += 5
        if self.y >= 640:
            self.sinking = False
