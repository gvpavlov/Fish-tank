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


class Aquarium(QMainWindow):
    def __init__(self):
        super(Aquarium, self).__init__()
        self.ui = Ui_aquarium()
        self.ui.setupUi(self)
        self.set_objects()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.movement)
        self.timer.start(40)

    def paintEvent(self, event):
        canvas = QtGui.QPainter()
        canvas.begin(self)
        #canvas.scale(self.size().width(), self.size().height())
        canvas.setPen(QtCore.Qt.NoPen)
        canvas.drawPixmap(0, 0, self.background.scaled(1000, 700))
        self.draw_alien(canvas)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def movement(self):
        self.move_alien()
        self.repaint()

    def move_alien(self):
        self.game.alien.move()
        self.set_alien_frame(self.game.alien.direction)

    """ Determines which image will be used for the next repaint. """
    def set_alien_frame(self, direction):
        if self.previous_direction == direction:
            self.alien_frameX += 160
        if self.alien_frameX >= 1600:
            self.alien_frameX = 0
        print(self.alien_frameX)
        self.previous_direction = direction


    def draw_alien(self, canvas):
        self.alien_image = QtGui.QPixmap(os.path
            .join(resource_directory, "alien.png"))
        canvas.drawPixmap(self.game.alien.x, self.game.alien.y,
                          self.alien_image, self.alien_frameX,
                          self.alien_frameY, 160, 160)

    """ Objects are accessible through game. """
    def set_objects(self):
        self.game = Game()
        self.previous_direction = (-1, 0)
        self.alien_frameX = 0
        self.alien_frameY = 0
        self.background = QtGui.QPixmap(
            os.path.join(resource_directory, "background.png"))
