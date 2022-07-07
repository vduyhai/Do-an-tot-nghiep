from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5 import QtCore
from squat1 import Ui_Dialog
import os
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_Dialog()
        self.uic.setupUi(self)

    #
    #
    # def __init__(self, *args, **kwargs):
    #     super(MainWindow, self).__init__(*args, **kwargs)
    #
    #     self.online_webcams = QCameraInfo.availableCameras()
    #     if not self.online_webcams:
    #         pass #quit
    #     self.exist = QCameraViewfinder()
    #     self.exist.show()
    #     self.setCentralWidget(self.exist)
    #     # self.setGeometry(QtCore.QRect(70, 250, 161, 51))
    #
    #     # self.pic1.setGeometry(QtCore.QRect(80, 80, 141, 161))
    #     # self.pic1.setText("")
    #     # self.pic1.setObjectName("pic1")
    #
    #     # set the default webcam.
    #     self.get_webcam(0)
    #     self.setWindowTitle("WebCam")
    #     self.show()
    #
    # def get_webcam(self, i):
    #     self.my_webcam = QCamera(self.online_webcams[i])
    #     self.my_webcam.setViewfinder(self.exist)
    #     self.my_webcam.setCaptureMode(QCamera.CaptureStillImage)
    #     self.my_webcam.start()
    #
    # def  setupUI(self):


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
    # app.setApplicationName("WebCam")
    #
    # window = MainWindow()
    # app.exec_()