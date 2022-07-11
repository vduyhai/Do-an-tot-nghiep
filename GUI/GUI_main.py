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
import PoseModule as pm

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.start.clicked.connect(self.show_pick)

    def show_pick(self):
        # self.hide()
        self.pick = QMainWindow()
        self.uic1 = Ui_MainWindow1()
        self.uic1.setupUi(self)
        self.uic1.cancel.clicked.connect(self.show_home)
        self.uic1.coffee.clicked.connect(self.show_camera)
        # self.pick.show()

    def show_home(self):
        self.show()

    def show_camera(self):
        self.camera = QMainWindow()
        self.uic2 = Ui_MainWindow2()
        self.uic2.setupUi(self)
        self.uic2.canel.clicked.connect(self.show_home)

        self.uic2.progressBar.setValue(0)

        self.thread = {}
        self.thread[1] = capture_video(index=1)
        self.thread[1].start()
        self.thread[1].signal.connect(self.show_wedcam)
        self.thread[1].counting.connect(self.count)
        self.thread[1].progress_bar.connect(self.uic2.progressBar.setValue)

    def count(self, count):
        self.uic2.Continue.hide()
        self.uic2.counting.setText(str(count))
        # print(count)
        if count == 8:
            self.uic2.Continue.show()

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

class capture_video(QThread):
    signal = pyqtSignal(np.ndarray)
    counting = pyqtSignal(int)
    progress_bar = pyqtSignal(int)

    def __init__(self, index):
        self.index = index
        print("start threading", self.index)
        super(capture_video, self).__init__()

    def run(self):
        detector = pm.poseDetector()
        nos = 0
        dir = 0
        cap = cv2.VideoCapture('squat1.mp4')  # 'D:/8.Record video/My Video.mp4'
        while True:
            ret, cv_img = cap.read()
            # cv_img = cv_img[:, 180:460]
            if ret:
                cv_img = detector.findPose(cv_img, False)
                lmList = detector.findPosition(cv_img, False)
                if len(lmList) != 0:
                    angle = detector.findAngle(cv_img, 23, 25, 27)
                    per = np.interp(angle, (182, 270), (0, 100))
                    if per == 100:
                        if dir == 0:
                            nos += 0.5
                            dir = 1
                    if per == 0:
                        if dir == 1:
                            nos += 0.5
                            dir = 0
                    self.counting.emit(int(nos))
                    self.progress_bar.emit(int(per))
                self.signal.emit(cv_img)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())