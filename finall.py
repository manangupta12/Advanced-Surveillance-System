import drive
import cv2
import face_detect as face
import training as train

while True:
    count=face.fun()
    if count==0:
        drive.forward()
    if count==1:

        face.fun()
        
        train.fun()

gpio.release()
