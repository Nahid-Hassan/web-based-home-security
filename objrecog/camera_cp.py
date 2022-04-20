import os
import cv2
import numpy as np
import urllib.request
from django.conf import settings
from keras.models import load_model
from objrecog.models import ObjectRecognitionModel
from tensorflow.keras.preprocessing import image
from time import time


facec = cv2.CascadeClassifier(
'./objrecog/static/objrecog/weights/haarcascade_frontalface_default.xml')
model = ObjectRecognitionModel(
    "./objrecog/static/objrecog/weights/model_5_2022_99.json", "./objrecog/static/objrecog/weights/model_5_2022_99.h5")
font = cv2.FONT_HERSHEY_SIMPLEX


previous = time()
delta = 0

class VideoCamera(object):
	def __init__(self):
            self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		status, fr = self.video.read()
		gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2RGB)

		global delta
		global previous

		current = time()
		delta += current - previous
		previous = current

		if delta >= 2:
			delta =0
			faces = facec.detectMultiScale(gray_fr, 1.3, 5)
			# print(faces, len(faces))

			# here we using for loop for create rectangle for multiple face.
			for (x, y, w, h) in faces:
				# draw rectangle
				fc = gray_fr[y:y+h, x: x+w]
				roi = cv2.resize(fc, (224, 224))

				# predict human face	
				img = image.img_to_array(roi)
				img = np.expand_dims(img, axis=0)
				
				print("DeBUG : ", len(faces))
				if len(faces) < 1:
					print("Not found")


				if len(faces) >= 1:
					print("Found")
				
			
				# if len(faces) >= 1:
				# 	pred = model.predict_person(img)
				# 	# print(pred)
				# 	# print(x, y)
				# 	cv2.putText(fr, pred, (x, y), font, 1, (255, 255, 0), 2)
				# 	cv2.rectangle(fr, (x, y), (x + w, y + h), (255, 0, 0), 2)
				# else:
				# 	print("Hey....")
				# 	cv2.putText(fr, "No Person", (383, 233), font, 1, (255, 255, 0), 2)
				# 	cv2.rectangle(fr, (383,233), (383 + 20, 233 + 20), (255, 0, 0), 2)
				# 	print("I am here....")
				pred = model.predict_person(img)
				# print(pred)
				# print(x, y)
				cv2.putText(fr, pred, (x, y), font, 1, (255, 255, 0), 2)
				cv2.rectangle(fr, (x, y), (x + w, y + h), (255, 0, 0), 2)
			
		else:
			# gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2RGB)
			faces = facec.detectMultiScale(gray_fr, 1.3, 5)
			# print(faces, len(faces))

			# here we using for loop for create rectangle for multiple face.
			for (x, y, w, h) in faces:
				# draw rectangle
				fc = gray_fr[y:y+h, x: x+w]
				roi = cv2.resize(fc, (300, 300))

				# predict human face	
				img = image.img_to_array(roi)
				img = np.expand_dims(img, axis=0)
				
			
				# if len(faces) >= 1:
				# 	pred = model.predict_person(img)
				# 	# print(pred)
				# 	# print(x, y)
				# 	cv2.putText(fr, pred, (x, y), font, 1, (255, 255, 0), 2)
				# 	cv2.rectangle(fr, (x, y), (x + w, y + h), (255, 0, 0), 2)
				# else:
				# 	print("Hey....")
				# 	cv2.putText(fr, "No Person", (383, 233), font, 1, (255, 255, 0), 2)
				# 	cv2.rectangle(fr, (383,233), (383 + 20, 233 + 20), (255, 0, 0), 2)
				# 	print("I am here....")
				# pred = model.predict_person(img)
				# print(pred)
				# print(x, y)
				# cv2.putText(fr, pred, (x, y), font, 1, (255, 255, 0), 2)
				cv2.rectangle(fr, (x, y), (x + w, y + h), (255, 0, 0), 2)
				
			
		ret, jpeg = cv2.imencode('.jpg', fr)
		return jpeg.tobytes()
1