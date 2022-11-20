import sys
import os
from PyQt5 import QtGui
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QImage, QPixmap
# pip install pyqt6
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from screen1 import Ui_MainWindow
import cv2
from detect_or_track import detect

os.environ['OPENCV_VIDEOIO_DEBUG'] = '1'
os.environ['OPENCV_VIDEOIO_PRIORITY_MSMF'] = '0'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.thread = {}

        self.cam_links = []
        self.cam_links.append(0)
        self.cam_links.append('videoplayback.mp4')
        self.cam_links.append('videoplayback (1).mp4')
        self.cam_links.append('videoplayback (2).mp4')
        self.cam_links.append('videoplayback (3).mp4')
        self.cam_links.append('videoplayback (4).mp4')
        self.cam_links.append('videoplayback (5).mp4')
        self.cam_links.append('videoplayback (6).mp4')
        self.cam_links.append('videoplayback (7).mp4')

        self.uic.screen1.clicked.connect(self.ShowS1)
        self.uic.screen4.clicked.connect(self.ShowS4)
        self.uic.screen8.clicked.connect(self.ShowS8)

        self.S1bool = False
        self.S4bool = False
        self.S8bool = False

        self.ShowS1()

    def ShowS1(self):
        print("Show S1")
        self.S1bool = True

        if self.S4bool == True:
            self.S4bool = False
            self.StopPlaying()
        if self.S8bool == True:
            self.S8bool = False
            self.StopPlaying()

        self.uic.stackedWidget.setCurrentWidget(self.uic.S1)

        self.labels = [self.uic.S1C1]

        self.ShowCamera(1026, 762)

    def ShowS4(self):
        print("Show S4")
        self.S4bool = True

        if self.S1bool == True:
            self.S1bool = False
            self.StopPlaying()
        if self.S8bool == True:
            self.S8bool = False
            self.StopPlaying()

        # self.uic.screen1.clicked.connect(self.ShowS1)

        self.uic.stackedWidget.setCurrentWidget(self.uic.S4)

        self.labels = [self.uic.S4C1, self.uic.S4C2, self.uic.S4C3, self.uic.S4C4]

        self.ShowCamera(513, 381)

        # self.uic.screen1.clicked.connect(self.StopPlaying)

    def ShowS8(self):
        print("Show S8")
        self.S8bool = True

        if self.S1bool == True:
            self.S1bool = False
            self.StopPlaying()
        if self.S4bool == True:
            self.S4bool = False
            self.StopPlaying()

        self.uic.stackedWidget.setCurrentWidget(self.uic.S8)

        self.labels = [self.uic.S8C1, self.uic.S8C2, self.uic.S8C3, self.uic.S8C4,
                       self.uic.S8C5, self.uic.S8C6, self.uic.S8C7, self.uic.S8C8, self.uic.S8C9]

        self.ShowCamera(343, 254)

    def StopPlaying(self):
        for i, label in enumerate(self.labels):
            label.clear()
            self.thread[i].stop()
            print("Stop threading ", i)

    def ShowCamera(self, width, height):
        for i, label in enumerate(self.labels):
            self.thread[i] = detect(cam_link=self.cam_links[i], label=label,
                                               width=width, height=height)
            self.thread[i].start()
            print("Start threading ", i)
            self.thread[i].signal.connect(self.show_webcam)

    def show_webcam(self, frame, label):
        label.setPixmap(QPixmap.fromImage(frame))

class Work(QThread):
    signal = pyqtSignal(QImage, QLabel)

    def __init__(self, cam_link, label, width, height):
        self.cam_link = cam_link
        self.label = label
        self.w = width
        self.h = height
        super(Work, self).__init__()

    def run(self):
        self.hilo_corriendo = True
        cap = cv2.VideoCapture(self.cam_link)
        while self.hilo_corriendo:
            ret, frame = cap.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = Image.shape
                bytes_per_line = ch * w
                convert_to_Qt_format = QtGui.QImage(Image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
                p = convert_to_Qt_format.scaled(self.w, self.h, Qt.KeepAspectRatio)
                self.signal.emit(p, self.label)
    def stop(self):
        self.hilo_corriendo = False
        self.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
