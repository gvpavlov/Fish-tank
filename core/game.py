from alien import Alien
from fish import Fish
from unit import Directions
from random import randint

""" Movement directions """
LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)


class Game:
    def __init__(self):
        self.set_objects()

    def set_objects(self):
        self.aliens = [Alien(randint(0, 600), randint(0, 600),
                             Directions.left, 'lion'),
                       Alien(randint(0, 600), randint(0, 600),
                             Directions.left, 'lion'),
                       Alien(randint(0, 600), randint(0, 600),
                             Directions.left),
                       Alien(randint(0, 600), randint(0, 600),
                             Directions.left)]
        self.fishes = [Fish(randint(0, 600), randint(0, 600),
                            Directions.left, 0),
                       Fish(randint(0, 600), randint(0, 600),
                            Directions.left, 0),
                       Fish(randint(0, 600), randint(0, 600),
                            Directions.left, 0),
                       Fish(randint(0, 600), randint(0, 600),
                            Directions.left, 1),
                       Fish(randint(0, 600), randint(0, 600),
                            Directions.left, 1),
                       Fish(randint(0, 600), randint(0, 600),
                            Directions.left, 1),
                       Fish(randint(0, 600), randint(0, 600),
                            Directions.left, 2),
                       Fish(randint(0, 600), randint(0, 600),
                            Directions.left, 2),
                       Fish(randint(0, 600), randint(0, 600),
                            Directions.left, 2)]
