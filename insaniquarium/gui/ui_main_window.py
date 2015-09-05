# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Sat Sep  5 15:23:35 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1100, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.game = QtWidgets.QFrame(self.centralwidget)
        self.game.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.game.setFrameShadow(QtWidgets.QFrame.Plain)
        self.game.setLineWidth(0)
        self.game.setObjectName("game")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.game)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sidebar = QtWidgets.QFrame(self.game)
        self.sidebar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sidebar.setObjectName("sidebar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sidebar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text = QtWidgets.QLabel(self.sidebar)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setObjectName("text")
        self.verticalLayout.addWidget(self.text)
        self.score = QtWidgets.QLabel(self.sidebar)
        self.score.setText("")
        self.score.setAlignment(QtCore.Qt.AlignCenter)
        self.score.setObjectName("score")
        self.verticalLayout.addWidget(self.score)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.buy_fish = QtWidgets.QPushButton(self.sidebar)
        self.buy_fish.setObjectName("buy_fish")
        self.verticalLayout.addWidget(self.buy_fish)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.upgrade_food = QtWidgets.QPushButton(self.sidebar)
        self.upgrade_food.setObjectName("upgrade_food")
        self.verticalLayout.addWidget(self.upgrade_food)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem2)
        self.upgrade_weapon = QtWidgets.QPushButton(self.sidebar)
        self.upgrade_weapon.setObjectName("upgrade_weapon")
        self.verticalLayout.addWidget(self.upgrade_weapon)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.menu = QtWidgets.QPushButton(self.sidebar)
        self.menu.setObjectName("menu")
        self.verticalLayout.addWidget(self.menu)
        self.horizontalLayout_2.addWidget(self.sidebar)
        self.aquarium = Aquarium(self.game)
        self.aquarium.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aquarium.sizePolicy().hasHeightForWidth())
        self.aquarium.setSizePolicy(sizePolicy)
        self.aquarium.setObjectName("aquarium")
        self.horizontalLayout_2.addWidget(self.aquarium)
        self.horizontalLayout.addWidget(self.game)
        self.main_menu = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_menu.sizePolicy().hasHeightForWidth())
        self.main_menu.setSizePolicy(sizePolicy)
        self.main_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_menu.setObjectName("main_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_menu)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.label = QtWidgets.QLabel(self.main_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.start_game = QtWidgets.QPushButton(self.main_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_game.sizePolicy().hasHeightForWidth())
        self.start_game.setSizePolicy(sizePolicy)
        self.start_game.setMinimumSize(QtCore.QSize(0, 0))
        self.start_game.setMaximumSize(QtCore.QSize(400, 16777215))
        self.start_game.setObjectName("start_game")
        self.verticalLayout_3.addWidget(self.start_game)
        self.scores = QtWidgets.QPushButton(self.main_menu)
        self.scores.setMaximumSize(QtCore.QSize(400, 16777215))
        self.scores.setObjectName("scores")
        self.verticalLayout_3.addWidget(self.scores)
        self.exit = QtWidgets.QPushButton(self.main_menu)
        self.exit.setMaximumSize(QtCore.QSize(400, 16777215))
        self.exit.setObjectName("exit")
        self.verticalLayout_3.addWidget(self.exit)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout.addWidget(self.main_menu)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aquarium"))
        self.text.setText(_translate("MainWindow", "Score:"))
        self.buy_fish.setText(_translate("MainWindow", "Fish \n"
"100$"))
        self.upgrade_food.setText(_translate("MainWindow", "Food \n"
"300$"))
        self.upgrade_weapon.setText(_translate("MainWindow", "Weapon \n"
"500$"))
        self.menu.setText(_translate("MainWindow", "Menu"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600;\">Aquarium</span></p></body></html>"))
        self.start_game.setText(_translate("MainWindow", "Start Game"))
        self.scores.setText(_translate("MainWindow", "Top Scores"))
        self.exit.setText(_translate("MainWindow", "Exit"))

from aquarium import Aquarium
