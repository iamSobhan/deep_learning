#importing libraries
import numpy as np
import pandas as pd
import cv2

#loading the pre-trained Haarcascades classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#checking the video file is opening successfully or not
faces = cv2.VideoCapture("faces01.mp4")

if faces.isOpened():
    rval , frame = faces.read()
else:
    rval = False
    print("Video is not Found!")

#detecting faces from the video
rectangles = []

while rval:
    rval, frame = faces.read()
    frameHeight, frameWidth, fdepth = frame.shape
    frame = cv2.resize(frame, (600, 400))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # convert the frame to grayscale
    face = face_cascade.detectMultiScale(gray, 1.2, 2)

    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # draw rectangles around the detected faces

    cv2.imshow("Result", frame)  # display the frame with detected faces

    if cv2.waitKey(33) == ord("b"):  # break the loop if "b" is pressed
        break

faces.release()  # release the video capture and close all windows
cv2.destroyAllWindows()