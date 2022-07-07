import cv2 as cv
import numpy as np
import time
import PoseModule as pm
import serial
import threading

cap = cv.VideoCapture('squat1.mp4')

ser = serial.Serial()

color = (255, 0, 255)
detector = pm.poseDetector()
set = 0
dir = 0 # 0: up & 1: down
pTime = 0
t = 10
count = 0

# class myThread(threading.Thread):
#     def __init__(self, cap, count):
#         threading.Thread.__init__(self)
#         self.cap = cap
#         self.count = count
#
#     def countdown(self):
#         while self.count:
#             mins, secs = divmod(self.count, 60)
#             timer = '{:02d}:{:02d}'.format(mins, secs)
#             print(timer, end="\r")
#             time.sleep(1)
#             self.count -= 1
#
#     def Trainer(self):
#         global dir, set
#         while True:
#             success, img = self.cap.read()
#             img = cv.resize(img, (1280, 720))
#             # img = cv.imread("AiTrainer/test.jpg")
#             #
#             # nos = countdown(t)
#             # if nos < 20:
#             #     print('CONTINUE?')
#             #     ans = input('CONTINUE?')
#             #     if ans == 'y':
#             #         con = countdown(int((20 - nos) * 1))
#             #     elif ans == 'n':
#             #         print('bye')
#             #         break
#             img = detector.findPose(img, False)
#             lmList = detector.findPosition(img, False)
#             if len(lmList) != 0:
#                 #     left Arm
#                 angle = detector.findAngle(img, 23, 25, 27)
#                 per = np.interp(angle, (185, 270), (0, 100))
#
#                 bar = np.interp(angle, (185, 270), (650, 100))
#                 if per == 100:
#                     if dir == 0:
#                         set += 0.5
#                         dir = 1
#                 if per == 0:
#                     if dir == 1:
#                         set += 0.5
#                         dir = 0
#
#                 # Draw Bar
#                 cv.rectangle(img, (1100, 100), (1175, 650), color, 3)
#                 cv.rectangle(img, (1100, int(bar)), (1175, 650), color, cv.FILLED)
#                 cv.putText(img, f'{int(per)} %', (1100, 75), cv.FONT_HERSHEY_PLAIN, 4,
#                            color, 4)
#
#                 #     # Draw Curl Count
#                 #     cv.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv.FILLED)
#                 cv.putText(img, str(int(set)), (45, 670), cv.FONT_HERSHEY_PLAIN, 15,
#                            (255, 0, 0), 25)
#                 print(set)
#                 cv.imshow('img', img)
#                 cv.waitKey(1)
#
# try:
#     thread1 = myThread.countdown(20)
#     thread2 = myThread.Trainer(cap)
#     thread1.start()
#     thread2.start()
# except:
#     print('e')





while True:
    _, img = cap.read()

    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
    #     # Right Arm
        angle = detector.findAngle(img, 23, 25, 27)
    #     # # Left Arm
    #     angle1 = detector.findAngle(img, 11, 23, 25)
        per = np.interp(angle, (185, 270), (0, 100))
        # per1 = np.interp(angle1, (90, 180), (0, 100))

        bar = np.interp(angle, (185, 270), (650, 100))
        # print(angle, per)
    #     print(angle1, per1)
    #
    #     # Check for the dumbbell curls
    #     color = (255, 0, 255)
        if per == 100:
    #         color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
    #         color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0
        # print(count)

        # Draw Bar
        cv.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv.rectangle(img, (1100, int(bar)), (1175, 650), color, cv.FILLED)
        cv.putText(img, f'{int(per)} %', (1100, 75), cv.FONT_HERSHEY_PLAIN, 4,
                    color, 4)

    #     # Draw Curl Count
    #     cv.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv.FILLED)
        cv.putText(img, str(int(count)), (45, 670), cv.FONT_HERSHEY_PLAIN, 15,
                    (255, 0, 0), 25)
    print(count)

    cv.imshow("Image", img)
    cv.waitKey(1)