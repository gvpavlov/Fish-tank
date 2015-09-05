import unittest
from unit import Unit, Directions


class TestUnit(unittest.TestCase):
    def setUp(self):
        self.unit = Unit(100, 100, Directions.left, 160, 65)

    def test_init(self):
        self.assertEqual(self.unit.x, 100)
        self.assertEqual(self.unit.y, 100)
        self.assertEqual(self.unit.direction, Directions.left)
        self.assertEqual(self.unit.image_size, 160)
        self.assertEqual(self.unit.radius, 65)

    def test_move_random(self):
        x = self.unit.x
        y = self.unit.y
        self.unit.move_random()
        self.assertNotEqual((x, y), (self.unit.x, self.unit.y))

    def test_change_direction(self):
        direction = self.unit.direction
        self.unit.change_direction(self.unit.direction)
        self.assertNotEqual(direction, self.unit.direction)

    def test_constrain(self):
        self.unit.direction = Directions.down
        self.unit.y = 1000
        self.unit.constrain()
        self.assertEqual(self.unit.direction, Directions.up)

        self.unit.direction = Directions.up
        self.unit.y = -1000
        self.unit.constrain()
        self.assertEqual(self.unit.direction, Directions.down)

        self.unit.direction = Directions.right
        self.unit.x = 3000
        self.unit.constrain()
        self.assertEqual(self.unit.direction, Directions.left)

        self.unit.direction = Directions.left
        self.unit.x = -100
        self.unit.constrain()
        self.assertEqual(self.unit.direction, Directions.right)

    def test_collision_circle(self):
        x = self.unit.x + self.unit.image_size / 2
        y = self.unit.y + self.unit.image_size / 2
        coordinates = (x, y, self.unit.radius)
        self.assertEqual(self.unit.collision_circle(), coordinates)

    def test_get_direcion(self):
        x = 0
        y = 0
        self.unit.x = 0
        self.unit.direction = Directions.down
        self.unit.y = 1000
        self.unit.get_direction(x, y)
        self.assertEqual(self.unit.direction, Directions.up)

        self.unit.x = 0
        self.unit.direction = Directions.up
        self.unit.y = -1000
        self.unit.get_direction(x, y)
        self.assertEqual(self.unit.direction, Directions.down)

        self.unit.y = 0
        self.unit.direction = Directions.right
        self.unit.x = 3000
        self.unit.get_direction(x, y)
        self.assertEqual(self.unit.direction, Directions.left)

        self.unit.y = 0
        self.unit.direction = Directions.left
        self.unit.x = -100
        self.unit.get_direction(x, y)
        self.assertEqual(self.unit.direction, Directions.right)

    def test_chase(self):
        x = self.unit.x
        y = self.unit.y
        prey = Unit(200, 200, Directions.left, 100, 100)
        self.unit.chase(prey)
        self.assertNotEqual((x, y), (self.unit.x, self.unit.y))

        prey = Unit(98, 100, Directions.left, 100, 100)
        self.unit.chase(prey)
        self.assertEqual((prey.x, prey.y), (self.unit.x, self.unit.y))

        prey = Unit(100, 98, Directions.left, 100, 100)
        self.unit.chase(prey)
        self.assertEqual((prey.x, prey.y), (self.unit.x, self.unit.y))


if __name__ == '__main__':
    unittest.main()
