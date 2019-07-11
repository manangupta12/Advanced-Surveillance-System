
import cv2
cap=cv2.VideoCapture(0)
haar_face=cv2.CascadeClassifier("/home/pi/Desktop/robotics/haarcascade_frontalface_alt.xml")
def fun():
    count=0
    while True:
        ret,img=cap.read()
        rect=haar_face.detectMultiScale(img,1.3,5)
        for (x,y,w,h) in rect:
            count+=1
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
            print "Face Detected"
            cv2.imwrite("/home/pi/Desktop/robotics/img.jpg",img)
        break
    return count
