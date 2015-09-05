import unittest
from sinking_item import SinkingItem


class TestSinkingItem(unittest.TestCase):
    def setUp(self):
        self.constraint = (1000, 1000)
        self.item = SinkingItem(self.constraint, 100, 100, 40, 14)

    def test_init(self):
        self.assertEqual(self.item.x, 100)
        self.assertEqual(self.item.y, 100)
        self.assertEqual(self.item.image_size, 40)
        self.assertEqual(self.item.radius, 14)

    def test_sink(self):
        self.item.y = 1000
        y = self.item.y
        self.item.sink()
        self.assertNotEqual(self.item.y, y)
        self.assertFalse(self.item.sinking)

    def test_collision_circle(self):
        x = self.item.x + self.item.image_size / 2
        y = self.item.y + self.item.image_size / 2
        coordinates = (x, y, self.item.radius)
        self.assertEqual(self.item.collision_circle(), coordinates)


if __name__ == '__main__':
    unittest.main()
