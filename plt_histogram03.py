import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(10000)
y = np.random.rand(10000)

plt.hist2d(x=x, y=y, bins=100)
plt.show()




