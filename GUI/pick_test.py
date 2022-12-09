# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pick_test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 868)
        MainWindow.setStyleSheet("background-color: rgb(0, 95, 55);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(50, 50, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Wingdings")
        font.setPointSize(60)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.back.setFont(font)
        self.back.setStyleSheet("QPushButton{\n"
"font: 60pt \"Wingdings\";\n"
"background-color: rgb(0, 95, 55);\n"
"color: rgb(0, 170, 0);\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgb(0, 95, 55);\n"
"color:rgb(115, 230, 0);\n"
"}")
        self.back.setObjectName("back")
        self.cup = QtWidgets.QLineEdit(self.centralwidget)
        self.cup.setGeometry(QtCore.QRect(140, 240, 560, 81))
        self.cup.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 45pt \"MS Shell Dlg 2\";\n"
"border: none;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"padding-bottom: 5px;\n"
"")
        self.cup.setObjectName("cup")
        self.personal = QtWidgets.QPushButton(self.centralwidget)
        self.personal.setGeometry(QtCore.QRect(140, 380, 560, 90))
        self.personal.setStyleSheet("QPushButton{\n"
"font: 35pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);\n"
"border-radius: 40px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color:rgb(115, 230, 0);\n"
"}\n"
"")
        self.personal.setObjectName("personal")
        self.plastic = QtWidgets.QPushButton(self.centralwidget)
        self.plastic.setGeometry(QtCore.QRect(140, 550, 560, 90))
        self.plastic.setStyleSheet("QPushButton{\n"
"font: 35pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);\n"
"border-radius: 40px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color:rgb(115, 230, 0);\n"
"}")
        self.plastic.setObjectName("plastic")
        self.drinks = QtWidgets.QLineEdit(self.centralwidget)
        self.drinks.setGeometry(QtCore.QRect(740, 240, 560, 81))
        self.drinks.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 45pt \"MS Shell Dlg 2\";\n"
"border: none;\n"
"border-bottom: 2px solid rgb(255, 255, 255);\n"
"padding-bottom: 5px;\n"
"")
        self.drinks.setObjectName("drinks")
        self.coffee = QtWidgets.QPushButton(self.centralwidget)
        self.coffee.setEnabled(True)
        self.coffee.setGeometry(QtCore.QRect(740, 380, 560, 90))
        self.coffee.setStyleSheet("QPushButton{\n"
"font: 35pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);\n"
"border-radius: 40px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color:rgb(115, 230, 0);\n"
"}")
        self.coffee.setObjectName("coffee")
        self.tea = QtWidgets.QPushButton(self.centralwidget)
        self.tea.setGeometry(QtCore.QRect(740, 550, 560, 90))
        self.tea.setStyleSheet("QPushButton{\n"
"font: 35pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);\n"
"border-radius: 40px;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color:rgb(115, 230, 0);\n"
"}")
        self.tea.setObjectName("tea")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setEnabled(True)
        self.next.setGeometry(QtCore.QRect(1310, 50, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Wingdings")
        font.setPointSize(60)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.next.setFont(font)
        self.next.setStyleSheet("QPushButton{\n"
"font: 60pt \"Wingdings\";\n"
"background-color: rgb(0, 95, 55);\n"
"color: rgb(0, 170, 0);\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgb(0, 95, 55);\n"
"color:rgb(115, 230, 0);\n"
"}")
        self.next.setObjectName("next")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.back.setText(_translate("MainWindow", "⇦"))
        self.cup.setText(_translate("MainWindow", "CHOOSE CUP"))
        self.personal.setText(_translate("MainWindow", "PERSONAL CUP"))
        self.plastic.setText(_translate("MainWindow", "PLASTIC CUP"))
        self.drinks.setText(_translate("MainWindow", "CHOOSE DRINKS"))
        self.coffee.setText(_translate("MainWindow", "COFFEE"))
        self.tea.setText(_translate("MainWindow", "TEA"))
        self.next.setText(_translate("MainWindow", "⇨"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

