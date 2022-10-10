import sys

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup
from pick_test import Ui_MainWindow
from serial import Serial
from functools import partial

ser = Serial('COM1')
cup = []
drinks = []

class communicate(QObject):
    signal1 = pyqtSignal(str)
    signal2 = pyqtSignal(str)

class MainWindow(QMainWindow):
    def __init__(self):
        self.c = communicate()
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.personal.clicked.connect(self.changePersonalCupBtnColor)
        self.uic.plastic.clicked.connect(self.changePlasticCupBtnColor)
        self.uic.coffee.clicked.connect(self.changeCoffeeBtnColor)
        self.uic.tea.clicked.connect(self.changeTeaBtnColor)

        self.c.signal1.connect(self.printSignal1)
        self.c.signal2.connect(self.printSignal2)

        self.uic.next.clicked.connect(self.send)

    def changePersonalCupBtnColor(self):
        self.uic.personal.setStyleSheet("QPushButton{\n"
                                        "font: 18pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(115, 230, 0);\n"
                                        "border-radius: 25px;\n"
                                        "}\n")

        self.uic.plastic.setStyleSheet("QPushButton{\n"
                                      "font: 18pt \"MS Shell Dlg 2\";\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(0, 170, 0);\n"
                                      "border-radius: 25px;\n"
                                      "}\n")

        self.c.signal1.emit('personal')
    def changePlasticCupBtnColor(self):
        self.uic.plastic.setStyleSheet("QPushButton{\n"
                                        "font: 18pt \"MS Shell Dlg 2\";\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(115, 230, 0);\n"
                                        "border-radius: 25px;\n"
                                        "}\n")
        self.uic.personal.setStyleSheet("QPushButton{\n"
                                       "font: 18pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(0, 170, 0);\n"
                                       "border-radius: 25px;\n"
                                       "}\n")

        self.c.signal1.emit('plastic')

    def changeCoffeeBtnColor(self):
        self.uic.coffee.setStyleSheet("QPushButton{\n"
                                       "font: 18pt \"MS Shell Dlg 2\";\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(115, 230, 0);\n"
                                       "border-radius: 25px;\n"
                                       "}\n")
        self.uic.tea.setStyleSheet("QPushButton{\n"
                                    "font: 18pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(0, 170, 0);\n"
                                    "border-radius: 25px;\n"
                                    "}\n")
        self.c.signal2.emit('coffee')

    def changeTeaBtnColor(self):
        self.uic.tea.setStyleSheet("QPushButton{\n"
                                    "font: 18pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(115, 230, 0);\n"
                                    "border-radius: 25px;\n"
                                    "}\n")
        self.uic.coffee.setStyleSheet("QPushButton{\n"
                                    "font: 18pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(0, 170, 0);\n"
                                    "border-radius: 25px;\n"
                                    "}\n")
        self.c.signal2.emit('tea')

    def printSignal1(self, x):
        print(x)
        cup.append(x)
        if len(cup) and len(drinks) >= 1:
            self.uic.next.setEnabled(True)

    def printSignal2(self, x):
        print(x)
        drinks.append(x)
        if len(cup) and len(drinks) >= 1:
            self.uic.next.setEnabled(True)

    def send(self):
        print(cup[-1])
        print(drinks[-1])
        ser.write(bytes(cup[-1] + "_" + drinks[-1], 'utf8'))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())