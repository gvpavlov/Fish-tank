import unittest
from game import Game
from fish import Fish
from alien import Alien
from coin import Coin
from food import Food
from unit import Directions


class TestGame(unittest.TestCase):
    def setUp(self):
        self.constraint = (1000, 1000)
        self.game = Game(self.constraint)

    def test_init(self):
        self.assertEqual(self.game.score, 100)
        self.assertEqual(self.game.weapon_power, 11)
        self.assertEqual(self.game.food_quality, 1)

    def test_set_objects(self):
        self.assertIsInstance(self.game.fishes[0], Fish)
        self.game.spawn_alien()
        self.assertIsInstance(self.game.aliens[0], Alien)
        self.assertIsInstance(self.game.coins, list)
        self.assertIsInstance(self.game.food, list)

    def test_spawn_alien(self):
        self.game.spawn_alien()
        self.assertIsInstance(self.game.aliens[0], Alien)

    def test_spawn_fish(self):
        self.game.spawn_fish()
        self.assertIsInstance(self.game.fishes[2], Fish)

    def test_upgrade_weapon(self):
        weapon_power = self.game.weapon_power
        self.game.upgrade_weapon()
        self.assertNotEqual(self.game.weapon_power, weapon_power)

    def test_upgrade_food(self):
        food = self.game.food_quality
        self.game.upgrade_food()
        self.assertNotEqual(self.game.food_quality, food)

    def test_mouse_press(self):
        self.game.aliens.append(Alien(self.constraint))
        self.game.mouse_press(50, 50)
        self.assertNotEqual(self.game.aliens[0].health,
                            Alien(self.constraint).health)

        score = self.game.score
        self.game.mouse_press(1000, 1000)
        self.assertIsInstance(self.game.food[0], Food)
        self.assertNotEqual(self.game.score, score)

    def test_clicked(self):
        self.assertFalse(self.game.clicked(0, 0, Alien(400, 400)))
        self.assertTrue(self.game.clicked(50, 50, Alien(0, 0)))

    def test_alien_action(self):
        self.game.spawn_alien()
        x = self.game.aliens[0].x
        y = self.game.aliens[0].y
        self.game.alien_action()
        self.assertNotEqual((x, y), (self.game.aliens[0].x,
                            self.game.aliens[0].y))

    def test_fish_action(self):
        self.game.spawn_fish()
        self.game.food.append(Food(self.constraint))
        self.game.fishes[0].hungry = True
        x = self.game.fishes[0].x
        y = self.game.fishes[0].y
        self.game.fish_action()
        self.assertNotEqual((x, y), (self.game.fishes[0].x,
                            self.game.fishes[0].y))

        x = self.game.fishes[0].x
        y = self.game.fishes[0].y
        self.game.fishes[0].hungry = False
        self.game.fish_action()
        self.assertNotEqual((x, y), (self.game.fishes[0].x,
                                     self.game.fishes[0].y))

        self.game.fishes[0].drop_coin = True
        self.game.fish_action()
        self.assertNotEqual(self.game.coins, [])
        self.assertFalse(self.game.fishes[0].drop_coin)

        self.game.fishes[0].dead = True
        y = self.game.fishes[0].y
        self.game.fish_action()
        self.assertNotEqual(y, self.game.fishes[0].y)

    def test_get_closest(self):
        self.game.spawn_alien()
        self.game.spawn_fish()
        self.game.spawn_fish()
        self.assertIsInstance(self.game.get_closest(self.game.aliens[0],
                              self.game.fishes), Fish)

    def test_sink_coin(self):
        self.game.coins.append(Coin(self.constraint, 1500, 1500))
        self.game.sink_coin()
        self.assertEqual(self.game.coins, [])

        self.game.coins.append(Coin(self.constraint))
        y = self.game.coins[0].y
        self.game.sink_coin()
        self.assertNotEqual(y, self.game.coins[0].y)

    def test_sink_food(self):
        self.game.food.append(Food(self.constraint, 1000, 1000))
        self.game.sink_food()
        self.assertEqual(self.game.food, [])

        self.game.food.append(Food(self.constraint))
        y = self.game.food[0].y
        self.game.sink_food()
        self.assertNotEqual(y, self.game.food[0].y)

    def test_set_move_frame(self):
        self.game.spawn_fish()
        frame = self.game.fishes[0].frame
        self.game.set_move_frame(self.game.fishes[0], 80, 800)
        self.assertNotEqual(self.game.fishes[0].frame, frame)

        self.game.fishes[0].frame = 1000
        self.game.set_move_frame(self.game.fishes[0], 80, 800)
        self.assertEqual(self.game.fishes[0].frame, 0)
        self.assertEqual(self.game.fishes[0].state, 'swim')

        self.game.fishes[0].state = 'something'
        self.game.fishes[0].frame = 80
        frame = self.game.fishes[0].frame
        self.game.fishes[0].mirrored_rotation = True
        self.game.set_move_frame(self.game.fishes[0], 80, 800)
        self.assertNotEqual(self.game.fishes[0].frame, frame)
        self.assertEqual(self.game.fishes[0].state, 'swim')
        self.assertFalse(self.game.fishes[0].mirrored_rotation)

        self.game.fishes[0].dead = True
        frame = self.game.fishes[0].frame
        self.game.set_move_frame(self.game.fishes[0], 80, 800)
        self.assertNotEqual(self.game.fishes[0].frame, frame)

        self.game.fishes[0].frame = 8000
        self.game.set_move_frame(self.game.fishes[0], 80, 800)
        self.assertEqual(self.game.fishes[0].frame, 720)

        frame = self.game.fishes[0].frame
        self.game.fishes[0].mirrored = True
        self.game.set_move_frame(self.game.fishes[0], 80, 800)
        self.assertNotEqual(self.game.fishes[0].frame, frame)

        self.game.fishes[0].mirrored = True
        self.game.fishes[0].frame = -1000
        self.game.set_move_frame(self.game.fishes[0], 80, 800)
        self.assertEqual(self.game.fishes[0].frame, 0)

        self.game.fishes[0].mirrored = True
        self.game.fishes[0].frame = -1000
        self.game.fishes[0].direction = Directions.left
        self.game.set_move_frame(self.game.fishes[0], 80, 800)
        self.assertEqual(self.game.fishes[0].frame, 0)

        self.game.fishes[0].direction = Directions.left
        self.game.set_move_frame(self.game.fishes[0], 80, 800)
        self.assertFalse(self.game.fishes[0].mirrored)

    def test_set_sink_frame(self):
        self.game.coins.append(Coin(self.constraint))
        frame = self.game.coins[0].frame
        self.game.set_sink_frame(self.game.coins[0], 80, 800)
        self.assertNotEqual(self.game.coins[0].frame, frame)

        self.game.coins[0].frame = 1000
        self.game.set_sink_frame(self.game.coins[0], 80, 800)
        self.assertEqual(self.game.coins[0].frame, 0)

    def test_collision(self):
        self.game.coins.append(Coin(self.constraint))
        self.game.coins.append(Coin(self.constraint))
        self.assertTrue(self.game.collision(self.game.coins[0],
                                            self.game.coins[1]))

        self.game.coins.append(Coin(500, 500))
        self.assertFalse(self.game.collision(self.game.coins[0],
                                             self.game.coins[2]))

    def test_distance(self):
        self.assertEqual(self.game.distance((0, 0), (0, 1)), 1)


if __name__ == '__main__':
    unittest.main()
