from alien import Alien
from unit import Directions

""" Movement directions """
LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)


class Game:
    def __init__(self):
        self.set_objects()

    def set_objects(self):
        self.alien = [
                      Alien(300, 300, Directions.left),
                      Alien(100, 300, Directions.left),
                      Alien(300, 500, Directions.left),
                      Alien(300, 200, Directions.left)
                     ]
