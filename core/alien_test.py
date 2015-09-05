import unittest
from alien import Alien
from unit import Directions


class TestAlien(unittest.TestCase):
    def setUp(self):
        self.constraint = (1000, 1000)
        self.alien = Alien(self.constraint, 100, 100, Directions.left, 1)

    def test_init_no_params(self):
        alien = Alien(self.constraint)
        self.assertEqual(alien.x, 0)
        self.assertEqual(alien.direction, (1, 0))
        self.assertEqual(alien.kind, 'blue')
        self.assertEqual(alien.health, 100)
        self.assertEqual(alien.image_size, 160)
        self.assertEqual(alien.radius, 65)

    def test_init(self):
        self.assertEqual(self.alien.x, 100)
        self.assertEqual(self.alien.y, 100)
        self.assertEqual(self.alien.direction, Directions.left)
        self.assertEqual(self.alien.kind, 'lion')

    def test_hit(self):
        previous_health = self.alien.health
        self.alien.hit(10)
        self.assertEqual(self.alien.health, previous_health - 10)

    def test_is_dead(self):
        self.assertFalse(self.alien.is_dead())
        self.alien.health = 0
        self.assertTrue(self.alien.is_dead())


if __name__ == '__main__':
    unittest.main()
