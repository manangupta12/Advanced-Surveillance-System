import smtplib
import cv2

imgloc="\image_dataset\1.jpg"

img=cv2.imread(imgloc)

smtp_obj=smtplib.SMTP("smtp.gmail.com",587)

smtp_obj.ehlo()
print("Ping Sucessful")

smtp_obj.starttls()

smtp_obj.login("manangupta852@gmail.com","manshi0906")
print("Login Sucessful")


msg=img

smtp_obj.sendmail("manangupta852@gmail.com","manangupta852@gmail.com",msg)
print("Email sent")
smtp_obj.quit()
