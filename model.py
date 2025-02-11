from tensorflow.keras.models import model_from_json
import numpy as np
import tensorflow as tf

class FacialExpressionModel(object):
    EMOTIONS_LIST = ["Angry","Disgust","Fear","Happy","Neutral","Sad","Surprised"]

    def __init__(self,model_json_file,model_weights_file):
        with open(model_json_file,"r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded = model_from_json(loaded_model_json)

        self.loaded.load_weights(model_weights_file)
        #self.loaded.make_predict_function()

    def predict_emotion(self,img):
        self.preds = self.loaded.predict(img)
        return FacialExpressionModel.EMOTIONS_LIST[np.argmax(self.preds)]
