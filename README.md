# Advanced-Surveillance-System
This Raspberry pi project focuses on a smart and advanced IOT based surveillance system.
This is my first full fledged Raspberry Pi Project which basically involves the use of Raspberry pi camera and a robot chasis(with 2 D motors and a motor driver)
so, in this project I have used several different technologies namely IOT , machine learning , Image Processing using OpenCV , motor drive using Rpi 

Description of the project:
This is a robot based camera system fitted on a robot chasis , the main code running in loop in the Rpi is taking continuous live feed of the surroundings covering 360 degrees. 
As soon as a person is detected in the camera frame , the frame is tested in the Face Recognition model and is determined whether the person is Authorised or not ( depending on pictures of authorised person in the database ).
If the Person is Unauthorised, the robot will stop such as the person's face is in the camera frame and a mail will be sent to the owner with the link to a continuous live feed of the camera showing the activities of the unauthorized person including an attachment with the Unauthorised person's picture highlighting his face in a red box.
