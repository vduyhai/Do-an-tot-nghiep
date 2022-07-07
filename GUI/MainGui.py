from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import welcomescreen, pick, squat1, camera
from time import sleep
import cv2 as cv
# <name>.setWindowFlags(QtCore.Qt.FramelessWindowHint)
# <name>.setAttribute(QtCore.Qt.WA_TranslucentBackground)

sec = 0.03
ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def startUI():
    global ui
    ui = welcomescreen.Ui_Dialog()
    ui.setupUi(MainWindow)
    ui.start.clicked.connect(pickUI)
    MainWindow.show()

def pickUI():
    global ui
    ui = pick.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.cancel.clicked.connect(startUI)
    # ui.coffee.clicked.connect(cameraUI)
    MainWindow.show()

# def cameraUI():
#     global ui
#     ui = camera.Ui_Dialog()
#     ui.setupUi(MainWindow)
#     MainWindow.show()


startUI()
sys.exit(app.exec_())