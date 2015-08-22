# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aquarium.ui'
#
# Created: Fri Aug 14 15:57:31 2015
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aquarium(object):
    def setupUi(self, aquarium):
        aquarium.setObjectName("aquarium")
        #aquarium.showFullScreen()
        aquarium.resize(1000, 700)

        self.retranslateUi(aquarium)
        QtCore.QMetaObject.connectSlotsByName(aquarium)

    def retranslateUi(self, aquarium):
        _translate = QtCore.QCoreApplication.translate
        aquarium.setWindowTitle(_translate("aquarium", "Form"))
