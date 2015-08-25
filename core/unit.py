from time import time
from random import randint, sample


class Directions:
    """ Movement directions """
    left = (-1, 0)
    right = (1, 0)
    up = (0, -1)
    down = (0, 1)
    all = [left, right, up, down]


class Unit:
    """ Basic class for all kinds of fishes and aliens. """
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.time = time()

    """ General movement pattern for every creature in the game. """
    def move_random(self):
        if self.time < time():
            self.change_direction(self.direction)
            self.time = time() + randint(3, 5)
        self.constrain()
        self.x += self.direction[0] * 5
        self.y += self.direction[1] * 5

    """ Picks a random direction, different from the current one. """
    def change_direction(self, current_direction):
        next = [x for x in Directions.all if x != current_direction]
        self.direction = sample(next, 1)[0]
        if self.direction == current_direction:
            self.change_direction(self.direction)

    """
    Keeps unit from leaving the game window boundaries by switching
    the direction to the opposite one.
    """
    def constrain(self):
        if self.y >= 540:
            self.direction = Directions.up
        if self.y <= 0:
            self.direction = Directions.down
        if self.x >= 840:
            self.direction = Directions.left
        if self.x <= 0:
            self.direction = Directions.right
