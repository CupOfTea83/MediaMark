from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
import numpy as np
import pandas as pd
import joblib

PATH_X = "C:\\Users\\Никита\\Desktop\\data\\vectors_np.joblib"
PATH_Y = "C:\\Users\\Никита\\Desktop\\data\\scores_np.joblib"
PATH_MODEL = ".\\model.joblib"

print("Loading data - ", end="")
x = joblib.load(PATH_X)
y = joblib.load(PATH_Y)
print("Done")

print("Preparing train/test data - ", end="")
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 1)
print("Done")

print("Creating model - ", end="")
model = MLPRegressor(random_state = 1, max_iter = 10000)
print("Done")

print("Learning model - ", end="")
model.fit(x_train, y_train)
print("Done")

score = model.score(x_test, y_test)
print("Score -", score)

print("Save? [y/n]")
command = input()
if command == "y":
    joblib.dump(model, PATH_MODEL)
