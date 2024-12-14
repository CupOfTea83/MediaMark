from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np
import joblib

PATH_X = ".\\vectors_np.joblib"
PATH_Y = ".\\scores_np.joblib"
PATH_MODEL = ".\\model.joblib"

print("Loading data - ", end="")
x = np.asarray(joblib.load(PATH_X))
y = np.asarray(joblib.load(PATH_Y))
print("Done")

print("Preparing train/test data - ", end="")
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 1)
print("Done")

print("Creating model - ", end="")
model = MLPRegressor(random_state = 1,
                     hidden_layer_sizes = (240, 120, 60),
                     activation = "tanh",
                     solver = "adam",
                     verbose = True,
                     max_iter = 100)
print("Done")

print("Learning model: Processing")
model.fit(x_train, y_train)
print("Learning model: Done")

score = sqrt(mean_squared_error(model.predict(x_test), y_test))
print("Score -", score)

print("Save? [y/n]")
command = input()
if command == "y":
    joblib.dump(model, PATH_MODEL, compress=9)
