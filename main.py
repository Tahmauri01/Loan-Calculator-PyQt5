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




    #Annual Interest Label
        i_label = QLabel("Annual Interest", self)
        #Properties of Annual Interest
        i_label.setAlignment(Qt.AlignCenter)
        i_label.setGeometry(20, 100, 170, 40)
        i_label.setStyleSheet("QLabel" "{"
                            "border : 2px solid black;"
                            "background: red;"
                                        "}")
        i_label.setFont(QFont("Times", 9))

        #Input field for interest rate (QLineEdit)
        self.rate = QLineEdit(self)
        #Only integers accepted
        onlyInt = QIntValidator()
        self.rate.setValidator(onlyInt)
        #Set properties
        self.rate.setGeometry(200, 100, 180, 40)
        self.rate.setAlignment(Qt.AlignCenter)
        self.rate.setFont(QFont("Times", 9))






    #Number of years
        n_label = QLabel("Years", self)
        #Properties of years
        n_label.setAlignment(Qt.AlignCenter)
        n_label.setGeometry(20, 150, 170, 40)
        n_label.setStyleSheet("QLabel" "{"
                            "border : 2px solid black;"
                            "background: yellow;"
                                        "}")
        n_label.setFont(QFont("Times", 9))

        #Input field for num of years (QLineEdit)
        self.years = QLineEdit(self)
        #Only integers accepted
        onlyInt = QIntValidator()
        self.years.setValidator(onlyInt)
        #Set properties
        self.years.setGeometry(200, 150, 180, 40)
        self.years.setAlignment(Qt.AlignCenter)
        self.years.setFont(QFont("Times", 9))






    #Loan amount label
        a_label = QLabel("Loan Amount", self)
        #Properties of loan amount
        a_label.setAlignment(Qt.AlignCenter)
        a_label.setGeometry(20, 200, 170, 40)
        a_label.setStyleSheet("QLabel" "{"
                            "border : 2px solid black;"
                            "background: blue;"
                                        "}")
        a_label.setFont(QFont("Times", 9))

        #Input field for loan amount
        self.amount = QLineEdit(self)
        #Only integers accepted
        onlyInt = QIntValidator()
        self.amount.setValidator(onlyInt)
        #Set properties
        self.amount.setGeometry(200, 200, 180, 40)
        self.amount.setAlignment(Qt.AlignCenter)
        self.amount.setFont(QFont("Times", 9))

    #-------------------------------Compute Payment----------------------

        #Compute button
        calculate = QPushButton("Compute Payment", self)
        #set geometry of button
        calculate.setGeometry(125, 270, 150, 40)
        #Add action to calculate button
        calculate.clicked.connect(self.calculate_action)

        #---------------Output widget--------------
    
        #monthly payment
        self.m_payment = QLabel(self)
        #properties of monthly payment
        self.m_payment.setAlignment(Qt.AlignCenter)
        self.m_payment.setGeometry(30, 340, 300, 60)
        self.m_payment.setStyleSheet("QLabel" "{"
                            "border : 3px solid black;"
                            "background: rbga(225, 225, 225, 225);"
                                        "}")
        self.m_payment.setFont(QFont("Times", 11))

        #total payment
        self.t_payment = QLabel(self)
        #properties of total payment
        self.t_payment.setAlignment(Qt.AlignCenter)
        self.t_payment.setGeometry(70, 410, 300, 60)
        self.t_payment.setStyleSheet("QLabel" "{"
                            "border : 3px solid black;"
                            "background: white"
                                        "}")
        self.t_payment.setFont(QFont("Times", 11))

    
    def calculate_action(self):
        #Get annual interest rate, years, and loan amount
        annualInterestRate = self.rate.text()
        numYears = self.years.text()
        l_amount = self.amount.text()

        #check if no number entered
        if len(annualInterestRate) == 0 or annualInterestRate == '0' or len(numYears) == 0 or numYears == '0' or len(l_amount) == 0 or l_amount == '0':
            QMessageBox.critical(self, "ERROR!", "Fill the Blanks")

        #Get calculations

        annualInterestRate, numYears, l_amount = int(annualInterestRate), int(numYears), int(l_amount)
        
        #monthly interest rate = annual interest rate/[12 months x 100%]
        monthlyInterestRate = annualInterestRate/1200
        #Calculate monthly payment
        monthlyPayment = l_amount * monthlyInterestRate / (1-1/(1+monthlyInterestRate) ** (numYears * 12))
        #Monthly payments format is 2 decimal float
        monthlyPayment = "{:2f}".format(monthlyPayment)

        #Add text to monthly payment calculation
        self.m_payment.setText(f"Monthly Payment: ${monthlyPayment}")

        #Get total payment
        totalPayment = float(monthlyPayment) * 12 * numYears
        totalPayment = "{:2f}".format(totalPayment)
        self.t_payment.setText(f"Total Payment: ${totalPayment}")






#Create app object, initializes Qt app
App = QApplication(sys.argv)

#Create window class
window = Window()

#Start the app, makes sure everything is blocked until the app is exited
sys.exit(App.exec())
