import numpy as np
import cv2
from subprocess import call
import pyautogui
import time
import os
import glob
import smtplib
import base64
import base64
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
number = 0
cam = cv2.VideoCapture("Video.mp4")

while True:
        _,image = cam.read()
        grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(grayImage)

        if len(faces) == 0:
            print("No Faces Detected")

        else:
            print("Number of faces detected:" + str(faces.shape[0]))
            number = faces.shape[0]
            for(x,y,w,h) in faces:
                cv2.rectangle(image, (x,y), (x + w, y + h) ,(0, 255, 0), 2)

        cv2.rectangle(image,((0, image.shape[0] - 25)), (270, image.shape[0]), (255,255,255), -1)
        cv2.imshow("Faces Detected",image)
        cv2.waitKey(2)
        if len(faces) > 9:
            print("Number has exceeded")
            ss = pyautogui.screenshot()
            ss.save(r"C:\Users\visha\OneDrive\Desktop\notes\Internship\IoT\Task 13\screenshot.jpg")

            user = "vishalu06@gmail.com"
            pwd = "Nagavishal63"
            From = "Tech-Support Team"
            To = "hahalalapapakaka@gmail.com"

            msg = MIMEMultipart()
            time.sleep(1)
            msg['Subject'] = "Too many faces detected"

            body = "This is regarding a the number of people gathering"
            msg.attach(MIMEText(body,'plain'))

            fp = open(r"C:\Users\visha\OneDrive\Desktop\notes\Internship\IoT\Task 13\screenshot.jpg", 'rb')
            time.sleep(1)
            img = MIMEImage(fp.read())
            time.sleep(1)
            msg.attach(img)
            time.sleep(1)

            try:
                serv = smtplib.SMTP("smtp.gmail.com",587)
                print("smtp gmail")
                serv.ehlo()
                print("ehlo")
                serv.starttls()
                print("starttls")
                serv.login(user,pwd)
                print("Reading E-mail and Password")
                serv.sendmail(From,To,msg.as_string())
                print("from")
                serv.close()
                print("Sent E-mail successfully")

            except:
                print("Failed to send E-mail")


