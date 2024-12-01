from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
import pickle

PATH = "./data.csv"

def LoadData():
    with open(PATH) as file:
        string_data = file.readlines()

    x=[]
    y=[]

    for i in string_data:
        line = i.split(',')
        y.append(float(line[0]))
        x.append(list(map(float, line[1:])))

    return x, y

print("Loading data - ", end="")
x, y = LoadData()
print("Done")

print("Preparing train/test data - ", end="")
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 1)
print("Done")

print("Creating model - ", end="")
model = MLPRegressor(random_state = 1, max_iter = 500)
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
