import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
import sen_image_email as email
import live
def fun():
    c=0
    data_path = "/home/pi/Desktop/robotics/image datatset/"
    onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path,f))]

    Training_Data, Labels = [], []

    for i, files in enumerate(onlyfiles):
        image_path = data_path + onlyfiles[i]
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        Training_Data.append(np.asarray(images, dtype=np.uint8))
        Labels.append(i)

    Labels = np.asarray(Labels, dtype=np.int32)

    model = cv2.face.LBPHFaceRecognizer_create()

    model.train(np.asarray(Training_Data), np.asarray(Labels))

    print("Model Training Complete!!!!!")

    face_classifier = cv2.CascadeClassifier("/home/pi/Desktop/robotics/haarcascade_frontalface_alt.xml")
    img=cv2.imread("/home/pi/Desktop/robotics/img.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray)
    if faces is():
        return 0

    for(x,y,w,h) in faces:
        #cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200,200))

    face=roi.copy()

    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        result = model.predict(face)

        if result[1] < 500:
            confidence = int(100*(1-(result[1])/300))


        if confidence > 83:
            print"AUTHORISED PERSON"


        else:
            c=1
            print"NOT AN AUTHORISED PERSON"

            email.mail()
            print"Mail has been sent !!!!"

            live.fun()
    except:
        print "Face Not Found"    

