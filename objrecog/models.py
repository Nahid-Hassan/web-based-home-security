from tensorflow.keras.models import model_from_json
from tensorflow.python.keras.backend import set_session
import numpy as np
import tensorflow as tf

config = tf.compat.v1.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.15
session = tf.compat.v1.Session(config=config)
set_session(session)


class FacialExpressionModel(object):

    EMOTIONS_LIST = ["Angry", "Disgust",
                     "Fear", "Happy",
                     "Natural", "Sad",
                     "Surprise"]

    # later we use it for different our actual model
    #PERSON_NAME_LIST = ["Abir", "Rafi", "Bobi"]

    def __init__(self, model_json_file, model_weights_file):
        # load model from JSON file
        with open(model_json_file, "r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded_model = model_from_json(loaded_model_json)
            self.loaded_model.summary()

        # load weights into the new model
        self.loaded_model.load_weights(model_weights_file)

    # predict human_emotion
    def predict_emotion(self, img):
        global session
        set_session(session)
        self.preds = self.loaded_model.predict(img)
        return FacialExpressionModel.EMOTIONS_LIST[np.argmax(self.preds)]

    # write predict_person function is here
    # def predict_person(self, img):
    #    global session
    #    set_session(session)
    #    self.preds = self.loaded_model.predict(img)
    #    return FacialExpressionModel.PERSON_NAME_LIST[np.argmax(self.preds)]
