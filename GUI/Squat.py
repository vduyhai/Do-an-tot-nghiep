import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture("squat1.mp4")

color = (255, 0, 255)
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280, 720))
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    if len(lmList) != 0:
        angle = detector.findAngle(img, 23, 25, 27)
        per = np.interp(angle, (182, 270), (0, 100))
        bar = np.interp(angle, (182, 270), (650, 100))

        if per == 100:
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            if dir == 1:
                count += 0.5
                dir = 0
        print(count)

        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                    color, 4)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                    (255, 0, 0), 25)

    cv2.imshow("Image", img)
    cv2.waitKey(1)