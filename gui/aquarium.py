import os
import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore
from PyQt5 import QtGui

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
resource_directory = os.path.join(current_directory, "resources")
sys.path.append(os.path.join(parent_directory, "core"))

from game import Game
from unit import Directions


class Aquarium(QWidget):
    def __init__(self, parent):
        super(Aquarium, self).__init__()
        self.game = Game()
        self.load_pictures()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.action)
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
        for coin in self.game.coins:
            self.draw_coin(canvas, coin)
        for food in self.game.food:
            self.draw_food(canvas, food)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.game.mouse_press(event.x(), event.y())

    def load_pictures(self):
        # Alien
        self.alien_images = {
            'lion': QtGui.QPixmap(
                os.path.join(resource_directory, "alien.png")),
            'blue': QtGui.QPixmap(
                os.path.join(resource_directory, "alien2.png"))}
        self.alien_images_mirrored = {}.fromkeys(self.alien_images)
        self.fill_mirrored(self.alien_images, self.alien_images_mirrored)

        # Fish
        self.fish_images = {
            'swim': QtGui.QPixmap(
                os.path.join(resource_directory, "fish_swim.png")),
            'eat': QtGui.QPixmap(
                os.path.join(resource_directory, "fish_eat.png")),
            'turn': QtGui.QPixmap(
                os.path.join(resource_directory, "fish_turn.png")),
            'hungry_die': QtGui.QPixmap(
                os.path.join(resource_directory, "fish_die.png")),
            'hungry_swim': QtGui.QPixmap(
                os.path.join(resource_directory, "hungry_swim.png")),
            'hungry_eat': QtGui.QPixmap(
                os.path.join(resource_directory, "hungry_eat.png")),
            'hungry_turn': QtGui.QPixmap(
                os.path.join(resource_directory, "hungry_turn.png"))}
        self.fish_images_mirrored = {}.fromkeys(self.fish_images)
        self.fill_mirrored(self.fish_images, self.fish_images_mirrored)

        # Food
        self.food_image = QtGui.QPixmap(
            os.path.join(resource_directory, "food.png"))

        # Coin
        self.coin_image = QtGui.QPixmap(
            os.path.join(resource_directory, "coin.png"))

        # Background
        self.background = QtGui.QPixmap(
            os.path.join(resource_directory, "background.png"))

    def fill_mirrored(self, normal_images, mirrored):
        for key, value in normal_images.items():
            mirror = value.toImage()
            mirror = mirror.mirrored(True, False)
            mirrored[key] = QtGui.QPixmap().fromImage(mirror)

    def action(self):
        """ Incorporates all objects' actions and calls the repaint event."""
        self.game.actions()
        self.repaint()

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
                          alien.frame, state, 160, 160)

    def draw_fish(self, canvas, fish):
        state = fish.state
        if fish.hungry:
            state = 'hungry_' + state
        if fish.mirrored:
            image = self.fish_images_mirrored[state]
        else:
            image = self.fish_images[state]
        canvas.drawPixmap(fish.x, fish.y, image,
                          fish.frame, fish.size * 80, 80, 80)

    def draw_coin(self, canvas, coin):
        canvas.drawPixmap(coin.x, coin.y, self.coin_image,
                          coin.frame, coin.worth * 72, 72, 72)

    def draw_food(self, canvas, food):
        canvas.drawPixmap(food.x, food.y, self.food_image,
                          food.frame, 0, 40, 40)
