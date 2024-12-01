import pickle

class Model():
    _MODEL_PATH = "./model.dat"
    
    def __init__():
        with open(self._MODEL_PATH, 'rb') as file:
            self.model = pickle.load(file)

    def GetScore(**kwargs):

        #TODO vectorization
        parameters = []

        score = self.model.predict([parameters])

        return score
