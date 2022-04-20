# import necessary packages
import numpy as np
import cv2
import time
import os
import sys

# some necessary works before store images
# run your program like below
# nahid@cseru: Desktop $ python script.py {person_n} {person_name} 

# this portion of code is not handle any error. manually handle the error
# if new person is added below line must be uncomment
# os.mkdir(os.path.join("datasets", sys.argv[2]),0o777)
# image_path = os.path.join("datasets", sys.argv[2], sys.argv[1])


# ============= Start: handle folder and image file names =====================

flag = int(input("If new person is add enter 1 else enter 0: "))
name = input("Enter the person name: ")
person = input("Enter the person_number (ex: person_1, or person_2 etc...): ")

if flag:
    os.mkdir(os.path.join("datasets", name),0o777)

image_path = os.path.join("datasets", name, person)

image_counter = len(os.listdir(os.path.join("datasets", name)))
print(image_counter)

# ============= End: handle folder and image file names =====================


# It needed if you want to identify faces in an images or real time video.
# you can detect faces, eyes, upper body, lower body etc using it
# in this case we want identify frontface
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# access the webcam (every webcam has a number, the default is 0)
cam_port = 0
cap = cv2.VideoCapture(cam_port, cv2.CAP_DSHOW)

# infinity loop
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # checking 
    if not ret:
        print("Failed to grab frame.")
        break


    # to detect faces in video
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # # draw an rectangle above the faces/ just need for checking
    # for (x,y,w,h) in faces:
    #     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    #     roi_gray = gray[y:y+h, x:x+w]
    #     roi_color = frame[y:y+h, x:x+w]
    
    # text_color = (0,255,0)
    
    # Display the resulting frame
    cv2.imshow('frame',frame)
    
    # waitKey(0) pause your screen
    # waitKey(1) don't pause your screen
    key = cv2.waitKey(1)

    if key == ord('q'):
        print("Quitting: Escape button pressed.")
        break
    elif len(faces) == 0:  # if face detected or identified than
        # automatically save this images.
        
        image_name = f"{image_path}_{image_counter}.jpg"
        print("Saving image " + image_name)
        cv2.imwrite(image_name,  frame)
        image_counter += 1
    
    time.sleep(.1)

# everything is done release the capture
cap.release()
cv2.destroyAllWindows()

