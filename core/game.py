from alien import Alien

""" Movement directions """
LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)


class Game:
    def __init__(self):
        self.set_objects()

    def set_objects(self):
        self.alien = Alien(800, 100, LEFT)
