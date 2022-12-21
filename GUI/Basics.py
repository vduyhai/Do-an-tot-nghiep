import cv2 as cv
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv.VideoCapture(1)
pTime = 0
while True:
    success, img = cap.read()
    img = cv.resize(img, None, fx=1.4, fy=1.4)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime



    cv.imshow("Image", img)
    cv.waitKey(1)
