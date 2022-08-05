import sys
import cv2
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractButton
from camera import Ui_MainWindow2
import PoseModule as pm

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow2()
        self.uic.setupUi(self)
        self.uic.progressBar.setValue(0)
        self.uic.Continue.clicked.connect(self.start_capture_video)
        self.uic.cancel.clicked.connect(self.stop_capture_video)

        self.thread = {}
    def start_capture_video(self):
        self.thread[1] = capture_video(index=1)
        self.thread[1].start()
        self.thread[1].signal.connect(self.show_wedcam)
        self.thread[1].counting.connect(self.count)
        self.thread[1].progress_bar.connect(self.uic.progressBar.setValue)

    def closeEvent(self, event):
        self.stop_capture_video()

    def stop_capture_video(self):
        self.thread[1].stop()

    def count(self, count):
        self.uic.Continue.hide()
        self.uic.counting.setText(str(count))
        if count == 8:
            self.uic.Continue.show()

    def show_wedcam(self, cv_img):
        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.uic.camera.setPixmap(qt_img)

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
                    bar = np.interp(angle, (182, 270), (650, 100))

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
                    # print(nos)

                    # cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
                    # cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
                    # cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                    #             color, 4)
                    # cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                    #             (255, 0, 0), 25)
                #
                # cv2.imshow("Image", img_)
                # cv2.waitKey(1)
                self.signal.emit(cv_img)
    def stop(self):
        print("stop threading", self.index)
        self.terminate()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())