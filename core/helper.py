import unit


class Helper(Unit):
    def __init__(self, x=0, y=0, direction="right"):
        Unit.__init__(self, x, y, direction)
