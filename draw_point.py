import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['figure.figsize'] = (10, 6) # 图像显示大小
plt.rcParams['font.sans-serif'] = ['SimHei']  # 防止中文标签乱码，还有通过导入字体文件的方法
plt.rcParams['lines.linewidth'] = 0.5  # 设置曲线线条宽度

# plt.scatter(x=[2, 5, 6], y=[4, 8, 3], marker="*", alpha=0.5)
# plt.show()

# num = np.array([[2, 5], [3, 6], [4, 5], [3, 7], [5, 9]])
# # plt.scatter(x=num, y=num, marker="*", alpha=0.5)
# plt.scatter(x=num[:, 0], y=num[:, 1], marker="*", alpha=0.5)
# plt.show()

x = np.random.rand(20)
y = np.random.rand(20)
x1 = np.random.rand(20)
y1 = np.random.rand(20)

# 绘制点
plt.scatter(x, y, c="r", marker="p", s=20, label="girl")
plt.scatter(x1, y1, c="b", marker="v", s=18, label="boy")
plt.legend()  # 显示图例
plt.title("标题")
plt.text(0.5, 0.4, "哈哈")
plt.xlabel("x")
plt.ylabel("y")
plt.show()



