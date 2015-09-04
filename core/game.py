from alien import Alien
from fish import Fish
from coin import Coin
from food import Food
from unit import Directions
from random import randint
from math import sqrt
from time import time


class Game:
    """ Core class. """
    def __init__(self):
        self.set_objects()
        self.score = 100
        self.start_time = time()
        self.tracked_time = time()
        self.weapon_power = 11
        self.food_quality = 1

    def set_objects(self):
        """ Each level starts with only 2 fish. """
        self.fishes = [Fish(randint(0, 600), randint(0, 600),
                            Directions.left, 0),
                       Fish(randint(0, 600), randint(0, 600),
                            Directions.left, 0)]
        self.aliens = []
        self.coins = []
        self.food = []

    def track_time(self):
        """
        Controls all the action influenced by time.
        + 1 for dodging the spawn of the alien when elapsed is 0,
        self.tracked_time prevents mupltiple spawns in the same second.
        """
        elapsed = int(time() - self.start_time) + 1
        # Alien
        if (self.tracked_time != elapsed) and ((elapsed % 40) == 0):
            self.spawn_alien()
        # Fish
        for fish in self.fishes:
            fish.hungry_check()
            fish.coin_check()
        self.tracked_time = elapsed

    def spawn_alien(self):
        """ Spawns an alien at a random location. """
        self.aliens.append(Alien(randint(100, 500), randint(100, 500),
                           Directions.left, randint(0, 1)))

    def spawn_fish(self):
        """ Spawns a fish at a random location. Used by sidebar button. """
        self.fishes.append(Fish(randint(0, 600), randint(0, 600),
                           Directions.left, 0))

    def upgrade_weapon(self):
        """ Upgrades weapon. Used by sidebar button. """
        self.weapon_power += self.weapon_power

    def upgrade_food(self):
        """ Upgrades food. Used by sidebar button. """
        self.food_quality += 1

    def mouse_press(self, x, y):
        """ Takes action depending on what was clicked. """
        empty_click = True
        # Coin
        coin = [coin for coin in self.coins if self.clicked(x, y, coin)]
        if coin:
            self.score += (coin[0].worth + 1) * 25
            self.coins.remove(coin[0])
            empty_click = False
        # Alien
        alien = [alien for alien in self.aliens if self.clicked(x, y, alien)]
        if alien:
            alien[0].hit(self.weapon_power)
            empty_click = False
            if alien[0].is_dead():
                self.aliens.remove(alien[0])
                self.score += 200
        # Nothing
        if empty_click:
            if self.score:
                self.food.append(Food(x - 20, y - 20))
                self.score -= 5

    def clicked(self, x, y, unit):
        """ Checks if the mouse has clicked the unit. """
        if self.distance((x, y), unit.collision_circle()) <= unit.radius:
            return True
        return False

    def actions(self):
        self.track_time()
        self.alien_action()
        self.fish_action()
        self.sink_coin()
        self.sink_food()

    def alien_action(self):
        """ Chases closest fish or moves randomly if there are none. """
        for alien in self.aliens:
            if self.fishes:
                closest_fish = self.get_closest(alien, self.fishes)
                alien.chase(closest_fish)
                if self.collision(alien, closest_fish):
                    self.fishes.remove(closest_fish)
            else:
                alien.move_random()
            self.set_move_frame(alien, alien.image_size, 1600)

    def fish_action(self):
        """
        Chases closest food if hungry, moves randomly otherwise,
        gives a coin from time to time and dies if not fed.
        """
        for fish in self.fishes:
            if fish.dead:
                fish.sink()
                if not fish.sinking:
                    self.fishes.remove(fish)
            else:
                if fish.hungry and self.food:
                    closest_food = self.get_closest(fish, self.food)
                    fish.chase(closest_food)
                    if self.collision(fish, closest_food):
                        fish.eat(self.food_quality)
                        self.food.remove(closest_food)
                else:
                    fish.move_random()
                if fish.drop_coin:
                    self.coins.append(Coin(fish.x, fish.y, fish.size - 1))
                    fish.drop_coin = False
            self.set_move_frame(fish, fish.image_size, 800)

    def get_closest(self, chaser, targets):
        """ Retuns the closest target to the chaser. """
        closest = targets[0]
        lowest = self.distance((chaser.x, chaser.y), (closest.x, closest.y))
        for prey in targets[1:]:
            current = self.distance((chaser.x, chaser.y), (prey.x, prey.y))
            if current < lowest:
                lowest = current
                closest = prey
        return closest

    def sink_coin(self):
        for coin in self.coins:
            coin.sink()
            self.set_sink_frame(coin, coin.image_size, 400)
        self.coins = [coin for coin in self.coins if coin.sinking]

    def sink_food(self):
        for food in self.food:
            food.sink()
            self.set_sink_frame(food, food.image_size, 400)
        self.food = [food for food in self.food if food.sinking]

    def set_move_frame(self, unit, frame_width, width):
        """ Determines which image will be used for the next repaint. """
        if unit.previous_direction == unit.direction:
            if unit.dead:
                if unit.mirrored:
                    unit.frame -= frame_width
                else:
                    unit.frame += frame_width
                if unit.frame >= width or unit.frame <= 0:
                    if unit.mirrored:
                        unit.frame = 0
                    else:
                        unit.frame = width - frame_width
            else:
                if unit.mirrored_rotation:
                    unit.frame -= frame_width
                    if unit.frame <= 0:
                        unit.frame = 0
                        unit.state = 'swim'
                        unit.mirrored_rotation = False
                else:
                    unit.frame += frame_width
                    if unit.frame >= width:
                        unit.frame = 0
                        unit.state = 'swim'
        # Start rotation if the different directions are left and right
        # AND the current picture is in the other direction.
        elif ((unit.direction == Directions.right and
               not unit.mirrored) or
              (unit.direction == Directions.left and
               unit.mirrored)):
            unit.frame = 0
            unit.state = 'turn'
            # If the rotation is from right to left take the images in reverse.
            if unit.direction == Directions.left:
                unit.mirrored_rotation = True
                unit.frame = width - frame_width
        # Use the appropriate image based on direction.
        if unit.direction == Directions.left:
            unit.mirrored = False
        elif unit.direction == Directions.right:
            unit.mirrored = True
        unit.previous_direction = unit.direction

    def set_sink_frame(self, item, frame_width, width):
        item.frame += frame_width
        if item.frame >= width:
            item.frame = 0

    def collision(self, first, second):
        """ Check for collision between first and second object. """
        first_coords = first.collision_circle()
        second_coords = second.collision_circle()
        if (self.distance(first_coords, second_coords) <=
                first_coords[2] + second_coords[2]):
            return True
        return False

    def distance(self, first_coords, second_coords):
        """ Distance formula: sqrt[(x1 - x2)^2 + (y1 - y2)^2] """
        return sqrt((first_coords[0] - second_coords[0]) ** 2 +
                    (first_coords[1] - second_coords[1]) ** 2)
