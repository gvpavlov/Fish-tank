import os
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from PyQt5 import QtGui
from ui_aquarium import Ui_aquarium

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
resource_directory = os.path.join(current_directory, "resources")
sys.path.append(os.path.join(parent_directory, "core"))

from game import Game
from unit import Directions


class Aquarium(QMainWindow):
    def __init__(self):
        super(Aquarium, self).__init__()
        self.ui = Ui_aquarium()
        self.ui.setupUi(self)
        self.set_objects()
        self.load_pictures()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.movement)
        self.timer.start(40)

    def paintEvent(self, event):
        canvas = QtGui.QPainter()
        canvas.begin(self)
        canvas.setPen(QtCore.Qt.NoPen)
        canvas.drawPixmap(0, 0, self.background.scaled(self.size().width(),
                          self.size().height()))
        for alien in self.game.aliens:
            self.draw_alien(canvas, alien)
        for fish in self.game.fishes:
            self.draw_fish(canvas, fish)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    """ Loads all lists of objects and sets the current ones for drawing. """
    def set_objects(self):
        self.game = Game()

    def load_pictures(self):
        # Alien
        self.alien_images = {
            'lion': QtGui.QPixmap(os.path
                .join(resource_directory, "alien.png")),
            'blue': QtGui.QPixmap(os.path
                .join(resource_directory, "alien2.png"))}
        self.alien_images_mirrored = {}.fromkeys(self.alien_images)
        self.fill_mirrored(self.alien_images, self.alien_images_mirrored)

        # Fish
        self.fish_images = {
            'swim': QtGui.QPixmap(os.path
                .join(resource_directory, "fish_swim.png")),
            'eat': QtGui.QPixmap(os.path
                .join(resource_directory, "fish_eat.png")),
            'turn': QtGui.QPixmap(os.path
                .join(resource_directory, "fish_turn.png")),
            'hungry_swim': QtGui.QPixmap(os.path
                .join(resource_directory, "hungry_swim.png")),
            'hungry_eat': QtGui.QPixmap(os.path
                .join(resource_directory, "hungry_eat.png")),
            'hungry_turn': QtGui.QPixmap(os.path
                .join(resource_directory, "hungry_turn.png"))}

        self.fish_images_mirrored = {}.fromkeys(self.fish_images)
        self.fill_mirrored(self.fish_images, self.fish_images_mirrored)

        self.background = QtGui.QPixmap(
            os.path.join(resource_directory, "background.png"))

    def fill_mirrored(self, normal_images, mirrored):
        for key, value in normal_images.items():
            mirror = value.toImage()
            mirror = mirror.mirrored(True, False)
            mirrored[key] = QtGui.QPixmap().fromImage(mirror)

    """ Incorporates all objects' movement and calls the repaint event. """
    def movement(self):
        self.move_alien()
        self.move_fish()
        self.repaint()

    def move_alien(self):
        for alien in self.game.aliens:
            alien.move()
            self.set_frame(alien, 160, 1600)

    def move_fish(self):
        for fish in self.game.fishes:
            fish.move()
            self.set_frame(fish, 80, 800)

    """ Determines which image will be used for the next repaint. """
    def set_frame(self, unit, frame_width, width):
        if unit.previous_direction == unit.direction:
            if unit.mirrored_rotation:
                unit.frame_x -= frame_width
                if unit.frame_x <= 0:
                    unit.frame_x = 0
                    unit.state = 'swim'
                    unit.mirrored_rotation = False
            else:
                unit.frame_x += frame_width
                if unit.frame_x >= width:
                    unit.frame_x = 0
                    unit.state = 'swim'

        # Start rotation if the different directions are left and right
        # AND the current picture is in the other direction.
        elif ((unit.direction == Directions.right and
               not unit.mirrored) or
              (unit.direction == Directions.left and
               unit.mirrored)):
            unit.frame_x = 0
            unit.state = 'turn'
            # If the rotation is from right to left take the images in reverse.
            if unit.direction == Directions.left:
                unit.mirrored_rotation = True
                unit.frame_x = width - frame_width

        # Use the appropriate image based on direction.
        if unit.direction == Directions.left:
            unit.mirrored = False
        elif unit.direction == Directions.right:
            unit.mirrored = True
        unit.previous_direction = unit.direction

    def draw_alien(self, canvas, alien):
        if alien.mirrored:
            image = self.alien_images_mirrored[alien.kind]
        else:
            image = self.alien_images[alien.kind]
        if alien.state == 'swim':
            state = 0
        else:
            state = 160
        canvas.drawPixmap(alien.x, alien.y, image,
                          alien.frame_x, state, 160, 160)

    def draw_fish(self, canvas, fish):
        state = fish.state
        if fish.hungry:
            state = 'hungry_' + state
        if fish.mirrored:
            image = self.fish_images_mirrored[state]
        else:
            image = self.fish_images[state]
        canvas.drawPixmap(fish.x, fish.y, image,
                          fish.frame_x, fish.size * 80, 80, 80)
