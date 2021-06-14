# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(386, 204)
        font = QFont()
        font.setFamily(u"Consolas")
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 91, 31))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(15)
        self.label.setFont(font1)
        self.login = QLineEdit(self.centralwidget)
        self.login.setObjectName(u"login")
        self.login.setGeometry(QRect(100, 10, 281, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 141, 31))
        self.label_2.setFont(font1)
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(140, 50, 241, 31))
        self.signin = QPushButton(self.centralwidget)
        self.signin.setObjectName(u"signin")
        self.signin.setGeometry(QRect(110, 90, 161, 51))
        self.signin.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 150, 151, 16))
        self.link = QPushButton(self.centralwidget)
        self.link.setObjectName(u"link")
        self.link.setGeometry(QRect(260, 170, 121, 28))

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login form", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.signin.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Created by Gisterecis", None))
        self.link.setText(QCoreApplication.translate("MainWindow", u"Open in browser", None))
    # retranslateUi

