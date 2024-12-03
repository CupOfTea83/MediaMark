from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
import pickle
import pandas as pd

PATH = "C:\\Users\\Никита\\Desktop\\data\\prepared_data.csv"

print("Loading data - ", end="")
df = pd.read_csv(PATH, header = None)
print("Done")
y = df[0]
print("Done")
x = df.drop([0], axis=1).to_numpy()
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
    with open("./model.dat", "wb") as file:
        pickle.dump(model, file)
