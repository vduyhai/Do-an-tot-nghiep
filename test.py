import numpy as np
import cv2 as cv
import time

img = cv.imread('background.png', cv.WINDOW_FULLSCREEN)
i = 0
while True:
    i += 1
    cv.putText(img, str(i), (200, 200), cv.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv.imshow('bg', img)
    cv.waitKey(1)
    cv.destroyWindow('bg')
    time.sleep(1)

# Define the codec and create VideoWriter object
# fourcc = cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     frame = cv.flip(frame, 0)
#     # write the flipped frame
#     out.write(frame)
#     cv.imshow('frame', frame)
#     if cv.waitKey(1) == ord('q'):
#         break
# # Release everything if job is finished
# cap.release()
# out.release()
# cv.destroyAllWindows()