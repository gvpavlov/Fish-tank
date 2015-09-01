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
        for alien in self.game.alien:
            self.draw_alien(canvas, alien)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def set_objects(self):
        self.game = Game()
        self.current_alien = self.game.alien[0]

    def load_pictures(self):
        self.alien_image = QtGui.QPixmap(os.path
            .join(resource_directory, "alien2.png"))
        alien_image = self.alien_image.toImage()
        alien_image = alien_image.mirrored(True, False)
        self.alien_image_mirrored = QtGui.QPixmap().fromImage(alien_image)

        self.background = QtGui.QPixmap(
            os.path.join(resource_directory, "background.png"))

    def movement(self):
        self.move_alien()
        self.repaint()

    def move_alien(self):
        for alien in self.game.alien:
            self.current_alien = alien
            alien.move()
            self.set_alien_frame(alien.direction)

    """ Determines which image will be used for the next repaint. """
    def set_alien_frame(self, direction):
        if self.current_alien.previous_direction == direction:
            if self.current_alien.mirrored_rotation:
                self.current_alien.frameX -= 160
                if self.current_alien.frameX <= 0:
                    self.current_alien.frameX = 0
                    self.current_alien.frameY = 0
                    self.current_alien.mirrored_rotation = False
            else:
                self.current_alien.frameX += 160
                if self.current_alien.frameX >= 1600:
                    self.current_alien.frameX = 0
                    self.current_alien.frameY = 0

        # Start rotation if the different directions are left and right
        # AND the current picture is in the other directionn.
        elif ((direction == Directions.right and not self.current_alien.mirrored) or
              (direction == Directions.left and self.current_alien.mirrored)):
            self.current_alien.frameX = 0
            self.current_alien.frameY = 160
            # If the rotation is from right to left take the images in reverse.
            if direction == Directions.left:
                self.current_alien.mirrored_rotation = True
                self.current_alien.frameX = 1440

        # Use the appropriate image based on direction.
        if direction == Directions.left:
            self.current_alien.mirrored = False
        elif direction == Directions.right:
            self.current_alien.mirrored = True
        self.current_alien.previous_direction = direction

    def draw_alien(self, canvas, alien):
        print(alien)
        if alien.mirrored:
            image = self.alien_image_mirrored
        else:
            image = self.alien_image
        canvas.drawPixmap(alien.x, alien.y,
                          image, alien.frameX,
                          alien.frameY, 160, 160)
