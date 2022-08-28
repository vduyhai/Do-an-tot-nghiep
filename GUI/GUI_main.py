import sys
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from home import Ui_MainWindow
from pick import Ui_MainWindow1
from camera import Ui_MainWindow2
from bye import Ui_MainWindow3
import cv2
import PoseModule as pm
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.start.clicked.connect(self.show_pick)

    def show_pick(self):
        print('show pick')
        self.uic1 = Ui_MainWindow1()
        self.uic1.setupUi(self)
        self.uic1.cancel.clicked.connect(self.show_home)
        self.uic1.coffee.clicked.connect(self.show_camera)
        # self.pick.show()

    def show_home(self):
        print('show home')
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.start.clicked.connect(self.show_pick)

    def show_camera(self):
        print('show camera')
        self.uic2 = Ui_MainWindow2()
        self.uic2.setupUi(self)
        self.thread = {}
        self.uic2.progressBar.setValue(0)
        self.uic2.Continue.hide()
        self.uic2.cancel.clicked.connect(self.stop_capture_video)
        self.uic2.Continue.clicked.connect(self.stop_capture_video)

        self.Work = capture_video()
        self.Work.start()
        self.Work.signal.connect(self.show_webcam)
        self.Work.counting.connect(self.count)
        self.Work.progress_bar.connect(self.uic2.progressBar.setValue)

    def count(self, count):
        self.uic2.counting.setText(str(count))
        # print(count)
        # if count == 3:
        self.uic2.Continue.show()

    def show_webcam(self, Image):
        """Updates the image_label with a new opencv image"""
        # qt_img = self.convert_cv_qt(cv_img)
        self.uic2.camera.setPixmap(QPixmap.fromImage(Image))

    def show_bye(self):
        print('show bye')
        self.uic3 = Ui_MainWindow3()
        self.uic3.setupUi(self)
        self.my_qtimer = QTimer(self)
        self.my_qtimer.timeout.connect(self.show_home)
        self.my_qtimer.start(3000)
        self.my_qtimer.timeout.connect(self.my_qtimer.disconnect)

    def stop_capture_video(self):
        self.Work.stop()
        time.sleep(0.1)
        # self.thread[1].stop()
        self.show_bye()

class capture_video(QThread):
    signal = pyqtSignal(QImage)
    counting = pyqtSignal(int)
    progress_bar = pyqtSignal(int)

    def __init__(self):
        super(capture_video, self).__init__()

    def run(self):
        self.threadactive = True
        detector = pm.poseDetector()
        nos = 0
        dir = 0
        i = 0
        cap = cv2.VideoCapture('squat1.mp4')  # 'squat1.mp4'
        while self.threadactive:
            # print(i)
            # i = i + 1
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
                    self.progress_bar.emit(int(per))
                self.counting.emit(int(nos))

                Image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
                flip = cv2.flip(Image, 1)
                convertir_QT = QImage(flip.data, flip.shape[1], flip.shape[0], QImage.Format_RGB888)
                pic = convertir_QT.scaled(320, 240, Qt.KeepAspectRatio)
                self.signal.emit(pic)

    def stop(self):
        self.threadactive = False
        self.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())