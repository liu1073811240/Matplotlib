import matplotlib.pyplot as plt
import numpy as np


ax = []
ay = []
plt.ion()

for i in range(100):
    random = np.random.rand()
    ax.append(i)
    # ay.append(i**2)
    # ay.append(np.log(i**2))
    # ay.append(-np.log(i**2))
    ay.append(-np.log(i**2)*random)

    # plt.clf()
    plt.plot(ax, ay)  # 画折线图
    plt.scatter(ax,ay, c="r", marker="v")
    plt.pause(0.1)

plt.ioff()
plt.show()









