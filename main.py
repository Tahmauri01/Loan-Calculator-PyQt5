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
        self.UiComponents()
        #Show window
        self.show()

    #Function for adding widgets
    def UiComponents(self):
        head = QLabel("Loan Calculator \n XYZ Bank", self) #Title on the app
        head.setGeometry(0, 10, 400, 60) #x, y, width, hieght
        font = QFont("Times", 15) #font
        font.setBold(True)
        head.setFont(font)
        head.setAlignment(Qt.AlignCenter) #centers head
        color = QGraphicsColorizeEffect(self) #color
        color.setColor(Qt.green) 
        head.setGraphicsEffect(color)
        #Creates Intrest Label
        i_label = QLabel("Annual Interest", self)
        #Properties of Interest Label
        i_label.setAlignment(Qt.AlignCenter)
        i_label.setGeometry(20, 100, 170, 40)
        i_label.setStyleSheet("QLabel" "{"
                            "border : 2px solid black;"
                            "background: rbga(70, 70, 70, 35);"
                                        "}")
        
        i_label.setFont(QFont("Times", 9))













#Create app object, initializes Qt app
App = QApplication(sys.argv)

#Create window class
window = Window()

#Start the app, makes sure everything is blocked until the app is exited
sys.exit(App.exec())
