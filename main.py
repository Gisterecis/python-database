#imports

import database
import webbrowser
import PySide2
from PySide2 import QtCore, QtWidgets, QtGui
import sys
from gui import Ui_MainWindow

#create app
app = QtWidgets.QApplication([])

#create form
Form = QtWidgets.QWidget()
ui = Ui_MainWindow()
ui.setupUi(Form)
Form.show()

#hook logic

def sigin():
    if database.password != QtWidgets.QLineEdit.text(ui.password) or database.login != QtWidgets.QLineEdit.text(ui.login):
        print("Password or login not matches!")
    if database.password == QtWidgets.QLineEdit.text(ui.password) or database.login == QtWidgets.QLineEdit.text(ui.login):
        print("Successfully signed in!")

def openlink():
    webbrowser.open_new('https://github.com/Gisterecis/python-database')

ui.signin.clicked.connect(sigin)
ui.link.clicked.connect(openlink)

#run main loop
sys.exit(app.exec_())