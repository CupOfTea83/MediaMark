import matplotlib.pyplot as plt

#settings
models = [1, 2, 3, 4, 5, 6]
base_path = "./learn_log_{0}.txt"
#/settings

for i in range(len(models)):
    name = str(models[i])
    with open(base_path.format(name),'r') as file:
        data = file.readlines()

    x = []
    y = []

    for j in data:
        iter_part, loss_part = j.split(',')
        x.append(int(iter_part.split(' ')[1]))
        y.append(float(loss_part.split(' = ')[1]))
        
    plt.plot(x, y, color="red")
    plt.savefig("./learning_stat_{0}.png".format(name))
    plt.close()

