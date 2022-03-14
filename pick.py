# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pick.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 640, 480))
        self.widget.setStyleSheet("background-color: rgb(255, 217, 0);")
        self.widget.setObjectName("widget")
        self.cancel = QtWidgets.QPushButton(self.widget)
        self.cancel.setGeometry(QtCore.QRect(230, 380, 161, 51))
        self.cancel.setStyleSheet("background-color: rgb(240, 0, 104);\n"
"font: 87 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.cancel.setObjectName("cancel")
        self.pic1 = QtWidgets.QLabel(self.widget)
        self.pic1.setGeometry(QtCore.QRect(80, 80, 141, 161))
        self.pic1.setText("")
        self.pic1.setPixmap(QtGui.QPixmap("Images/coffeeCopy.png"))
        self.pic1.setObjectName("pic1")
        self.coffee = QtWidgets.QPushButton(self.widget)
        self.coffee.setGeometry(QtCore.QRect(70, 250, 161, 51))
        self.coffee.setStyleSheet("background-color: rgb(240, 0, 104);\n"
"font: 87 18pt \"Arial Black\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.coffee.setObjectName("coffee")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cancel.setText(_translate("MainWindow", "CANCEL"))
        self.coffee.setText(_translate("MainWindow", "COFFEE"))
# import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
