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
    """ Basic class for fishes and aliens. """
    def __init__(self, x, y, direction, image_size, radius):
        self.x = x
        self.y = y
        self.direction = direction
        self.time = time()
        self.image_size = image_size
        self.radius = radius

        # Variables for choosing the correct image for each unit.
        self.state = 'swim'
        self.previous_direction = direction
        self.frame = 0
        self.mirrored = False
        self.mirrored_rotation = False

    def move_random(self):
        """ General movement pattern for every creature in the game. """
        if self.time < time():
            self.change_direction(self.direction)
            self.time = time() + randint(3, 5)
        self.constrain()
        self.x += self.direction[0] * 2
        self.y += self.direction[1] * 2

    def change_direction(self, current_direction):
        """ Picks a random direction, different from the current one. """
        next = [x for x in Directions.all if x != current_direction]
        self.direction = sample(next, 1)[0]
        if self.direction == current_direction:
            self.change_direction(self.direction)

    def constrain(self):
        """
        Keeps unit from leaving the game window boundaries by
        switching the direction to the opposite one.
        """
        if self.y >= 540:
            self.direction = Directions.up
        if self.y <= 0:
            self.direction = Directions.down
        if self.x >= 840:
            self.direction = Directions.left
        if self.x <= 0:
            self.direction = Directions.right

    def collision_circle(self):
        """ Returns the coordinates and radius of the collision cicle. """
        x = self.x + self.image_size / 2
        y = self.y + self.image_size / 2
        return (x, y, self.radius)

    def get_direction(self, x, y):
        if self.y < y:
            self.direction = Directions.down
        if self.y > y:
            self.direction = Directions.up
        if self.x > x:
            self.direction = Directions.left
        if self.x < x:
            self.direction = Directions.right

    def chase(self, unit):
        """ Chases the given coordinates. """
        speed = 4
        self.get_direction(unit.x, unit.y)
        self.x += self.direction[0] * speed
        self.y += self.direction[1] * speed
        # Stops chaser from spinning and never hitting prey's coordinates
        if abs(self.x - unit.x) < speed:
            self.x = unit.x
        if abs(self.y - unit.y) < speed:
            self.y = unit.y
