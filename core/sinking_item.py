class SinkingItem:
    """ Combines food and coin common trades. """
    def __init__(self, x, y, image_size, radius):
        self.x = x
        self.y = y
        self.sinking = True
        self.frame = 0
        self.image_size = image_size
        self.radius = radius

    def sink(self):
        """ Sinks the item and changes item state when it hits the bottom. """
        self.y += 2
        if self.y >= 640:
            self.sinking = False

    def collision_circle(self):
        """ Returns the coordinates and radius of the collision cicle. """
        x = self.x + self.image_size / 2
        y = self.y + self.image_size / 2
        return (x, y, self.radius)
