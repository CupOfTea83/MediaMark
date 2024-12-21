import joblib
from sklearn.neural_network import MLPRegressor
import numpy as np
from vectorization_module.vectorization import vectorize_parameters

class Model():
    _MODEL_PATH = "./model.joblib"
    
    def __init__(self):
        self.model = joblib.load(self._MODEL_PATH)

    def getscore(self, **kwargs):
        parameters = np.asarray(vectorize_parameters(kwargs["name"],
                         kwargs["description"],
                         kwargs["genres"],
                         kwargs["media_type"],
                         kwargs["episodes"],
                         kwargs["year"],
                         kwargs["studios"],
                         kwargs["rating"]))

        score = self.model.predict(parameters)

        return score
