from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStatusBar, QMenuBar, QMessageBox
from PyQt5 import uic
from math import sqrt


#Calculator class
class Calc(QMainWindow):
    #Init function
    def __init__(self):
        super(Calc, self).__init__()
        uic.loadUi("calcgui.ui", self)
        self.show()
        self.buttons_handling()
        self.displayedValue = ""
        self.equation = ""

    #Buttons handling function
    def buttons_handling(self):
        self.pushButton0.clicked.connect(lambda: self.addAndDisplay("0"))
        self.pushButton1.clicked.connect(lambda: self.addAndDisplay("1"))
        self.pushButton2.clicked.connect(lambda: self.addAndDisplay("2"))
        self.pushButton3.clicked.connect(lambda: self.addAndDisplay("3"))
        self.pushButton4.clicked.connect(lambda: self.addAndDisplay("4"))
        self.pushButton5.clicked.connect(lambda: self.addAndDisplay("5"))
        self.pushButton6.clicked.connect(lambda: self.addAndDisplay("6"))
        self.pushButton7.clicked.connect(lambda: self.addAndDisplay("7"))
        self.pushButton8.clicked.connect(lambda: self.addAndDisplay("8"))
        self.pushButton9.clicked.connect(lambda: self.addAndDisplay("9"))
        
        self.pushButtonSum.clicked.connect(lambda: self.addAndDisplay('+'))
        self.pushButtonSub.clicked.connect(lambda: self.addAndDisplay('-'))
        self.pushButtonMultp.clicked.connect(lambda: self.addAndDisplay('*'))
        self.pushButtonDiv.clicked.connect(lambda: self.addAndDisplay('/'))
        self.pushButtonRoot.clicked.connect(lambda: self.addAndDisplay('sqrt('))
        self.pushButtonLBrack.clicked.connect(lambda: self.addAndDisplay("("))
        self.pushButtonRBrack.clicked.connect(lambda: self.addAndDisplay(")"))
        self.pushButtonDot.clicked.connect(lambda: self.addAndDisplay("."))

        

        self.pushButtonRes.clicked.connect(lambda: self.displayResult())

        self.pushButtonC.clicked.connect(lambda: self.clear())
        self.pushButtonDel.clicked.connect(lambda: self.deleteLast())

        self.actionClose.triggered.connect(lambda: self.closeApp())

    #Displaying digits in box
    def addAndDisplay(self, digit):
        self.equation += digit
        self.displayedValue += digit
        self.displayBox.setText(self.displayedValue)
    
    #Calculating result of operation
    def calculateEquation(self):
        try:
            if float(eval(self.equation)).is_integer():
                return int(eval(self.equation))
            else:
                return eval(self.equation)
        except:
            return "Error"
        
    #Displaying result
    def displayResult(self):
        result = self.calculateEquation()
        self.displayedValue = str(result)
        self.equation = str(result)
        self.displayBox.setText(self.displayedValue)
        
    #Clearing entry
    def clearEntry(self):
        self.displayedValue = ""
        self.displayBox.setText(self.displayedValue)
    
    #Clearing entire memory
    def clear(self):
        self.displayedValue = ""
        self.equation = ""
        self.displayBox.setText(self.displayedValue)

    #Deleting last character in equation
    def deleteLast(self):
        self.equation = self.equation[:-1]
        self.displayedValue = self.equation
        self.displayBox.setText(self.displayedValue)
    
    #Closing the app with confirmation window
    def closeApp(self):
        
        confirmationBox = QMessageBox.question(self, "Closing...", "Are you sure you want to close the calculator?", QMessageBox.Yes | QMessageBox.No)

        if confirmationBox == QMessageBox.Yes:
            self.close()
        else:
            pass


        

def main():
    app = QApplication([])
    window = Calc()
    app.exec_()

if __name__ == '__main__':
    main()
