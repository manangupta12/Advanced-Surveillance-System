# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 16:42:40 2019

@author: lappy
"""

import cv2

haar_face=cv2.CascadeClassifier("G:\\image dataset\\haarcascade_frontalface_alt.xml")
haar_upper=cv2.CascadeClassifier("G:\\image dataset\\haarcascade_upperbody.xml")
haar_full=cv2.CascadeClassifier("G:\\image dataset\\haarcascade_fullbody.xml")
haar_lower=cv2.CascadeClassifier("G:\\image dataset\\haarcascade_lowerbody.xml")
cap=cv2.VideoCapture("G:\\image dataset\\walking.avi")
while True:
    ret,img=cap.read()
    cv2.imshow("Live",img)
    rect1=haar_full.detectMultiScale(img,1.2,5)
    for (x1,y1,w1,h1) in rect1:
        cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(255,0,0),3)

    rect2=haar_face.detectMultiScale(img,1.3,20)
    for (x2,y2,w2,h2) in rect2:
        cv2.rectangle(img,(x2,y2),(x2+w2,y2+h2),(0,0,255),3)
    cv2.imshow("Upper Body and Face",img)
    if cv2.waitKey(1)==27:    
        break     
cap.release()
cv2.destroyAllWindows()