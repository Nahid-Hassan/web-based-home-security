from tensorflow.keras.models import model_from_json
from tensorflow.python.keras.backend import set_session
import numpy as np
import tensorflow as tf
import time
from django.db import models

config = tf.compat.v1.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.15
session = tf.compat.v1.Session(config=config)
set_session(session)


class ObjectRecognitionModel(object):

    PERSON_NAME_LIST = ["Abir", "Bobi", "Empty", "Rafi", "Unknowns"]

    def __init__(self, model_json_file, model_weights_file):
        # load model from JSON file
        with open(model_json_file, "r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded_model = model_from_json(loaded_model_json)
            self.loaded_model.summary()

        # load weights into the new model
        self.loaded_model.load_weights(model_weights_file)

    # write predict_person function is here
    def predict_person(self, img):
       global session
       set_session(session)
       self.preds = self.loaded_model.predict(img)
       print("[DEBUG-Models.py]" + str(self.preds))
    #    print(self.preds)
       return ObjectRecognitionModel.PERSON_NAME_LIST[np.argmax(self.preds)]

# create database model with parameter name, id, entry_time
# create list

class RecordListDB(models.Model):
    person = models.CharField(verbose_name="Predicted Person",max_length=50)
    record_datetime = models.DateTimeField(verbose_name="Creation Date", auto_now_add=True)
    # image = models.ImageField(verbose_name="Unknown Person Image", upload_to="uploads/%Y/%m/%d", height_field=None, width_field=None, max_length=None, blank=True)
    image = models.FileField(verbose_name = "Person Image", upload_to="uploads/%Y/%m/%d", max_length=100, null=True)

    def __str__(self):
        return self.person
    
    def get_absolute_url(self):
        return reverse("records", kwargs={"pk": self.pk})
    