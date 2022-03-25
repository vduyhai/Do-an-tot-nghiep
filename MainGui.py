from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import welcomescreen, pick, squat1
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
    ui.coffee.clicked.connect(squat1UI)
    MainWindow.show()

def squat1UI():
    global ui
    ui = squat1.Ui_Dialog()
    ui.setupUi(MainWindow)
    cap = cv.VideoCapture(0)
    while True:
        _, frame = cap.read()
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        h,w, c = frame.shape
        step = c * w

        qFrame = QtGui.QImage(frame.data, w, h, step, QtGui.QImage.Format_RGB888)

        ui.label.setPiximap(QtGui.QPixmap.fromImage(qFrame))

        MainWindow.show()
        cv.waitKey(1)

startUI()
sys.exit(app.exec_())