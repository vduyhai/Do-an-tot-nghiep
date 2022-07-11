import sys

import numpy as np
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from home import Ui_MainWindow
from pick import Ui_MainWindow1
from camera import Ui_MainWindow2
import cv2

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.start.clicked.connect(self.show_pick)

    def show_pick(self):
        self.hide()
        self.pick = QMainWindow()
        self.uic1 = Ui_MainWindow1()
        self.uic1.setupUi(self.pick)
        self.uic1.cancel.clicked.connect(self.show_home)
        self.uic1.coffee.clicked.connect(self.show_camera)
        self.pick.show()

    def show_camera(self):
        self.show_pick.hide()
        self.camera = QMainWindow()
        self.uic2 = Ui_MainWindow2()
        self.uic2.setupUi(self.camera)
        self.uic2.canel.clicked.connect(self.show_home)

        self.thread = {}
        self.thread[1] = capture_video(index=1)
        self.thread[1].start()
        self.thread[1].signal.connect(self.show_wedcam)

    def show_wedcam(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.uic2.camera.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(800, 600, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def show_home(self):
        self.show()

class capture_video(QThread):
    signal = pyqtSignal(np.ndarray)

    def __init__(self, index):
        self.index = index
        print("start threading", self.index)
        super(capture_video, self).__init__()

    def run(self):
        cap = cv2.VideoCapture('squat1.mp4')  # 'D:/8.Record video/My Video.mp4'
        while True:
            ret, cv_img = cap.read()
            print(cv_img.shape)
            cv_img = cv_img[:, 180:460]
            if ret:
                self.signal.emit(cv_img)

    def stop(self):
        print("stop threading", self.index)
        self.terminate()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())