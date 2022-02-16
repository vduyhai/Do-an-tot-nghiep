# import the time module
import time
import cv2 as cv

img = cv.imread('background.png')


# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        cv.putText(img, str(t), (100, 200), 1, 1, (255, 0, 0), 1)
        t -= 1



    print('Fire in the hole!!')


# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))
cv.imshow('img', img)
cv.waitKey(0)