# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 868)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 95, 55);")
        self.centralwidget.setObjectName("centralwidget")
        self.welcome = QtWidgets.QLabel(self.centralwidget)
        self.welcome.setGeometry(QtCore.QRect(300, 170, 840, 180))
        self.welcome.setStyleSheet("font: 120pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome.setObjectName("welcome")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(450, 565, 540, 140))
        self.start.setStyleSheet("QPushButton{\n"
"font: 60pt \"MS Shell Dlg 2\";\n"
"color: rgb(255,255,255);\n"
"border-radius: 45px;\n"
"background-color: rgb(0, 170, 0);\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgb(115, 230, 0);\n"
"}\n"
"")
        self.start.setObjectName("start")
        self.start.raise_()
        self.welcome.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome.setText(_translate("MainWindow", "WELCOME"))
        self.start.setText(_translate("MainWindow", "START"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

