# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 868)
        MainWindow.setStyleSheet("background-color: rgb(0, 95, 55);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(665, 250, 110, 480))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Vertical)
        self.progressBar.setObjectName("progressBar")
        self.counting = QtWidgets.QLabel(self.centralwidget)
        self.counting.setGeometry(QtCore.QRect(840, 250, 300, 300))
        self.counting.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 150pt \"MS Shell Dlg 2\";\n"
"")
        self.counting.setFrameShape(QtWidgets.QFrame.Box)
        self.counting.setText("")
        self.counting.setAlignment(QtCore.Qt.AlignCenter)
        self.counting.setObjectName("counting")
        self.Continue = QtWidgets.QPushButton(self.centralwidget)
        self.Continue.setGeometry(QtCore.QRect(840, 650, 300, 80))
        self.Continue.setStyleSheet("QPushButton{\n"
"font: 35pt \"MS Shell Dlg 2\";\n"
"color: rgb(255,255,255);\n"
"border-radius: 30px;\n"
"background-color: rgb(0, 170, 0);\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgb(115, 230, 0);\n"
"}\n"
"")
        self.Continue.setDefault(False)
        self.Continue.setObjectName("Continue")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(1310, 50, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Wingdings 2")
        font.setPointSize(60)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("QPushButton{\n"
"font: 60pt \"Wingdings 2\";\n"
"background-color: rgb(0, 95, 55);\n"
"color: rgb(0, 170, 0);\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgb(0, 95, 55);\n"
"color:rgb(115, 230, 0);\n"
"}")
        self.cancel.setObjectName("cancel")
        self.camera = QtWidgets.QLabel(self.centralwidget)
        self.camera.setGeometry(QtCore.QRect(300, 250, 300, 480))
        self.camera.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.camera.setText("")
        self.camera.setObjectName("camera")
        self.cancel_2 = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_2.setGeometry(QtCore.QRect(50, 50, 80, 80))
        font = QtGui.QFont()
        font.setFamily("Wingdings")
        font.setPointSize(60)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cancel_2.setFont(font)
        self.cancel_2.setStyleSheet("QPushButton{\n"
"font: 60pt \"Wingdings\";\n"
"background-color: rgb(0, 95, 55);\n"
"color: rgb(0, 170, 0);\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgb(0, 95, 55);\n"
"color:rgb(115, 230, 0);\n"
"}")
        self.cancel_2.setObjectName("cancel_2")
        self.order = QtWidgets.QLabel(self.centralwidget)
        self.order.setEnabled(True)
        self.order.setGeometry(QtCore.QRect(220, 100, 1000, 80))
        self.order.setStyleSheet("background-color: rgb(155, 230, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 45pt \"MS Shell Dlg 2\";\n"
"border-radius: 35px;")
        self.order.setAlignment(QtCore.Qt.AlignCenter)
        self.order.setObjectName("order")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Continue.setText(_translate("MainWindow", "NEXT"))
        self.cancel.setText(_translate("MainWindow", "❎"))
        self.cancel_2.setText(_translate("MainWindow", "⇦"))
        self.order.setText(_translate("MainWindow", "PLEASE DO 20 SQUATS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

