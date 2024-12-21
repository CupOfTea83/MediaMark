import matplotlib.pyplot as plt

with open("./learn_log.txt",'r') as file:
    data = f.readlines()

x = []
y = []

for i in data:
    iter_part, loss_part = i.split(',')
    x.append(int(iter_part.split(' ')[1]))
    y.append(float(loss_part.split(' = ')[1]))

plt.plot(x, y)
plt.savefig("./learning_stat.png")

