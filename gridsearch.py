from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from math import sqrt
import numpy as np
import joblib
import json

PATH_X = ".\\vectors_np.joblib"
PATH_Y = ".\\scores_np.joblib"
PATH_MODEL = ".\\model.joblib"
PATH_EXPERIMENTS = ".\\experiments\\"

test_size = 0.25
random_state_test = 1

x = np.asarray(joblib.load(PATH_X))[:2000]
y = np.asarray(joblib.load(PATH_Y))[:2000]

model = MLPRegressor(random_state=1,
                     hidden_layer_sizes=(120, 60, 30),
                     activation="tanh",
                     solver="sgd",
                     max_iter=100)
param_list = {"learning_rate": ["constant", "invscaling", "adaptive"], "learning_rate_init":[0.001,0.0001], "nesterovs_momentum":[True,False]}
gridCV = GridSearchCV(cv=3,estimator=model, param_grid=param_list,verbose=3)
gridCV.fit(x,y)
print("Best Hyperparameters:", gridCV.best_params_)
print("Best Cross-Validation Score:", gridCV.best_score_)
