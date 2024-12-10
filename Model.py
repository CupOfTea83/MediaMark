import joblib
from sklearn.neural_network import MLPRegressor
from vectorization_module.vectorization import vectorize_parameters

class Model():
    _MODEL_PATH = "./model.joblib"
    
    def __init__():
        self.model = joblib.load(_MODEL_PATH)

    def GetScore(**kwargs):
        parameters = vectorize_parameters(kwargs["name"],
                         kwargs["description"],
                         kwargs["genres"],
                         kwargs["media_type"],
                         kwargs["episodes"],
                         kwargs["year"],
                         kwargs["studios"],
                         kwargs["rating"])

        score = self.model.predict([parameters])

        return score
