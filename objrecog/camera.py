import cv2
import numpy as np
import urllib.request
from django.conf import settings
from keras.models import load_model
from lfr.models import FacialExpressionModel

facec = cv2.CascadeClassifier(
	'./objrecog/static/objrecog/weights/haarcascade_frontalface_default.xml')
model = FacialExpressionModel(
    "./objrecog/static/objrecog/weights/model.json", "./objrecog/static/objrecog/weights/model_weights.h5")
font = cv2.FONT_HERSHEY_SIMPLEX


class VideoCamera(object):
	def __init__(self):
            self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		status, fr = self.video.read()
		gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
		faces = facec.detectMultiScale(gray_fr, 1.3, 5)

		# here we using for loop for create rectangle for multiple face.
		for (x, y, w, h) in faces:
			# draw rectangle
			fc = gray_fr[y:y+h, x: x+w]
			roi = cv2.resize(fc, (48, 48))
			# predict emotions
			pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])

            # predict human face
			# pred = model.predict_person(roi[np.newaxis, :, :, np.newaxis])

            # write predict persons code is here

			cv2.putText(fr, pred, (x, y), font, 1, (255, 255, 0), 2)
			cv2.rectangle(fr, (x, y), (x + w, y + h), (255, 0, 0), 2)
		ret, jpeg = cv2.imencode('.jpg', fr)
		return jpeg.tobytes()
