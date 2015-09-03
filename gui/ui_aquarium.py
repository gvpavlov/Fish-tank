# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aquarium.ui'
#
# Created: Thu Sep  3 18:58:57 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_aquarium(object):
    def setupUi(self, aquarium):
        aquarium.setObjectName("aquarium")
        aquarium.resize(1000, 700)

        self.retranslateUi(aquarium)
        QtCore.QMetaObject.connectSlotsByName(aquarium)

    def retranslateUi(self, aquarium):
        _translate = QtCore.QCoreApplication.translate
        aquarium.setWindowTitle(_translate("aquarium", "Aquarium"))

