import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

x_data = np.random.random(100)
noise = np.random.normal(0, 0.01, x_data.shape)
y_data = x_data * 0.1 + 100 + noise

plt.scatter(x_data, y_data)
model = Sequential()
# 输出和输入
model.add(Dense(units=1, input_dim=1))
# sgd 随机梯度下降法 loss：均方误差
model.compile(optimizer='sgd', loss='mse', metrics=['accuracy'])

for step in range(10000):
    # 一次放入一个批次 现在是所有的数据放入一个批次 如果多的话咋办
    # cost 每次训练
    cost = model.train_on_batch(x_data, y_data)
    if step % 500 == 0:
        W1, b1 = model.layers[0].get_weights()
        # 打印权值和偏执值
W, b = model.layers[0].get_weights()
print('w:', W, "b:", b)

y_test = model.predict(x_data)

# 散点图
plt.scatter(x_data, y_data)

plt.plot(x_data, y_test, 'r-', lw=3)
plt.show()
