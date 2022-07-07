from cvzone.SerialModule import SerialObject
from time import sleep

arduino = SerialObject()

while True:
    a = arduino.getData()
    print(a[0])