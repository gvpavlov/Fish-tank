from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from PyQt5 import QtGui
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.game.hide()
        self.ui.aquarium.pause()
        self.connect_buttons()
        self.ui.aquarium.score_changed.connect(self.change_score)
        self.change_score()

    def connect_buttons(self):
        self.ui.buy_fish.clicked.connect(self.ui.aquarium.spawn_fish)
        self.ui.upgrade_weapon.clicked.connect(self.ui.aquarium.upgrade_weapon)
        self.ui.upgrade_food.clicked.connect(self.ui.aquarium.upgrade_food)
        self.ui.upgrade_food.clicked.connect(self.ui.aquarium.upgrade_food)
        self.ui.menu.clicked.connect(self.open_menu)
        self.ui.start_game.clicked.connect(self.close_menu)
        self.ui.exit.clicked.connect(self.close)

    @QtCore.pyqtSlot()
    def close_menu(self):
        self.ui.game.show()
        self.ui.main_menu.hide()
        self.ui.aquarium.unpause()

    @QtCore.pyqtSlot()
    def open_menu(self):
        self.ui.aquarium.pause()
        self.ui.game.hide()
        self.ui.main_menu.show()

    @QtCore.pyqtSlot()
    def change_score(self):
        self.ui.score.setText(str(self.ui.aquarium.score))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
