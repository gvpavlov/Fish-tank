import helper
import alien
import food
import coin
import gold_fish


# Will combine the different game clases and
# will be in charge of their interraction with one another.
class Game:
    def __init__(self):
        # Will take amounts for all items from the level file
        self.fishes = []
        self.aliens = []
        self.food = Food()
        self.coins = []
