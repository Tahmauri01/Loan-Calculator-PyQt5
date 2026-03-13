#imports
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

#main class
class Window(QMainWindow):
    #Constructor method
    def __init__(self):
        #Inherits method from superclass (QMainWindow)
        super().__init__()
        #Setting title
        self.setWindowTitle("Loan Calculator")
        #Setting geometry
        self.width = 400
        self.hieght = 500
        self.setGeometry(100, 100, self.width, self.hieght)
        #Show window
        self.show()


#Create app object, initializes Qt app
App = QApplication(sys.argv)

#Create window class
window = Window()

#Start the app, makes sure everything is blocked until the app is exited
sys.exit(App.exec())
