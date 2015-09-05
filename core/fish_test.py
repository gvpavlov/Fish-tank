import unittest
from fish import Fish
from unit import Directions


class TestFish(unittest.TestCase):
    def setUp(self):
        self.constraint = (1000, 1000)
        self.fish = Fish(self.constraint, 100, 100, Directions.left, 1)

    def test_init_no_params(self):
        fish = Fish(self.constraint)
        self.assertEqual(fish.x, 0)
        self.assertEqual(fish.y, 0)
        self.assertEqual(fish.direction, (1, 0))
        self.assertEqual(fish.size, 0)
        self.assertEqual(fish.image_size, 80)
        radius = (fish.size * 15 + 41) / 2
        self.assertEqual(fish.radius, radius)
        self.assertFalse(fish.hungry)
        self.assertFalse(fish.dead)

    def test_init(self):
        self.assertEqual(self.fish.x, 100)
        self.assertEqual(self.fish.y, 100)
        self.assertEqual(self.fish.direction, Directions.left)
        self.assertEqual(self.fish.size, 1)
        radius = (self.fish.size * 15 + 41) / 2
        self.assertEqual(self.fish.radius, radius)

    def test_starve(self):
        self.fish.starve()
        self.assertTrue(self.fish.dead)
        self.assertEqual(self.fish.state, 'die')
        self.assertFalse(self.fish.mirrored)
        self.assertEqual(self.fish.frame, 0)

        self.fish.mirrored = True
        self.fish.starve()
        self.assertEqual(self.fish.frame, 720)

    # # How to test time()??? works every 10 seconds..
    # def test_hungry_check(self):
    #     self.fish.last_fed = 9
    #     self.fish.hungry_check()
    #     self.assertTrue(self.fish.hungry)

    def test_eat(self):
        food = 5
        growth = self.fish.growth
        size = self.fish.size
        self.fish.eat(food)
        self.assertFalse(self.fish.hungry)
        self.assertEqual(self.fish.growth, growth + food)
        self.assertEqual(self.fish.size, size)

        self.fish.eat(food)
        self.assertNotEqual(self.fish.size, size)


if __name__ == '__main__':
    unittest.main()
