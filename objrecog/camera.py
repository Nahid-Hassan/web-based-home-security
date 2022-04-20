from datetime import date
import os
import cv2
import numpy as np
import urllib.request
from django.conf import settings
from keras.models import load_model
from objrecog.models import ObjectRecognitionModel
from tensorflow.keras.preprocessing import image
from time import time
from skimage import transform
from .models import RecordListDB
from django.core.files.base import ContentFile

facec = cv2.CascadeClassifier(
'./objrecog/static/objrecog/weights/haarcascade_frontalface_default.xml')
model = ObjectRecognitionModel(
    "./objrecog/static/objrecog/weights/vgg19-val.json", "./objrecog/static/objrecog/weights/vgg19-val.h5")
font = cv2.FONT_HERSHEY_SIMPLEX

# model_path = "././objrecog/static/objrecog/weights/model_5_2022_85_kaggle.h5"


previous = time()
delta = 0
flag = False
pred = str()

image_path = "D:\RealtimeTestDataset\Here"
image_counter = len(os.listdir(image_path))


class VideoCamera(object):
	def __init__(self):
            self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		status, fr = self.video.read()
		
		global image_path
		global image_counter

		
		# gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2RGB)

		global delta # change to 0 every two seconds
		global previous # use for store previous time
		global flag
		global pred

		current = time()
		delta += current - previous 
		previous = current


		if delta >= 2:
			delta = 0
			flag = True

			# image_name = f"{image_path}_{image_counter}.jpg"
			# cv2.imwrite(image_name, fr)
			image_counter +=1

			
			# np_image = np.array(np_image).astype('float32')/255
    		# np_image = transform.resize(np_image, (224, 224, 3))
    		# np_image = np.expand_dims(np_image, axis=0)	

			# image_test = np.array(fr).astype('float32') / 255
			# image_test = transform.resize(image_test, (224, 224, 3))
			# img = np.expand_dims(image_test, axis=0)

			roi = cv2.resize(fr, (224,224))
			roi = roi.astype(np.float32)
			roi /= 255.0
			img = image.img_to_array(roi)
			img = np.expand_dims(img, axis=0)

			pred = model.predict_person(img)
			print(pred)
			if pred.lower() == "unknowns" and not RecordListDB.objects.filter(person=pred).exists() or not RecordListDB.objects.filter(record_datetime__date=date.today()).exists():
				ret, temp = cv2.imencode('.jpg', fr)
				content = ContentFile(temp.tobytes())

				record = RecordListDB(person=pred)
				record.image.save('output.jpg', content)
				record.save()
			elif pred.lower() in ['abir', 'bobi', 'rafi'] and not RecordListDB.objects.filter(person=pred).exists() or not RecordListDB.objects.filter(record_datetime__date=date.today()).exists() :
				record = RecordListDB(person=pred)
				record.save()

			cv2.putText(fr, pred, (383, 233), font, 1, (255, 255, 0), 2)
		else:
			if flag and delta <= 1:
				cv2.putText(fr, pred, (383, 233), font, 1, (255, 255, 0), 2)
	
		ret, jpeg = cv2.imencode('.jpg', fr)
		return jpeg.tobytes()
	