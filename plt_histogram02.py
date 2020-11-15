from matplotlib import pyplot as plt
import numpy as np


u = 100  # 均值
sigma = 20  # 方差
# 2000个数据
x = u + sigma*np.random.randn(2000)
# x = np.random.randn(2000)
# 画图 bins:条形的个数， normed:是否标准化
plt.hist(x=x, bins=10, normed=True)
plt.show()


