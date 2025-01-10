from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np
import joblib
import json

PATH_X = ".\\vectors_np.joblib"
PATH_Y = ".\\scores_np.joblib"
PATH_MODEL = ".\\model.joblib"
PATH_EXPERIMENTS = ".\\experiments\\"

name = "model6"
random_state_model = 1
hidden_layer_sizes = (120, 60, 30)
activation = "tanh"
solver = "sgd"
verbose = True
max_iter = 100
nesterovs_momentum = False

test_size = 0.25
random_state_test = 1

print("Loading data - ", end="")
x = np.asarray(joblib.load(PATH_X))
y = np.asarray(joblib.load(PATH_Y))
print("Done")

print("Preparing train/test data - ", end="")
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=random_state_test)
print("Done")

print("Creating model - ", end="")
model = MLPRegressor(random_state=random_state_model,
                     hidden_layer_sizes=hidden_layer_sizes,
                     activation=activation,
                     solver=solver,
                     verbose=verbose,
                     max_iter=max_iter,
                     nesterovs_momentum=nesterovs_momentum)
print("Done")

print("Learning model: Processing")
model.fit(x_train, y_train)
print("Learning model: Done")

score = sqrt(mean_squared_error(model.predict(x_test), y_test))
print("Score -", score)

file_name = PATH_EXPERIMENTS + name + ".json"
with open(file_name, 'w') as file:
    data = {}
    data["model_settings"] = {"random_state_model": random_state_model,
                              "hidden_layer_sizes": hidden_layer_sizes,
                              "activation": activation,
                              "solver": solver,
                              "verbose": verbose,
                              "max_iter": max_iter,
                              "nesterovs_momentum":nesterovs_momentum}
    data["test_settings"] = {"random_state_test": random_state_test,
                             "test_size": test_size}
    data["result"] = score
    json.dump(data, file)

joblib.dump(model, PATH_MODEL, compress=9)
