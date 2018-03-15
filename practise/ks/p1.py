# 2018-03-14 14:00

# keras 联系

# 1 建立模型
# 2 添加层
# 3 编译

# 4 训练

import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense

TRAIN_X = np.random.random(100)
NOISE = np.random.normal(0, 0.01, 100)
TRAIN_Y = TRAIN_X * 0.3 + NOISE

model = Sequential();
model.add(Dense(input_dim=1, units=1))
model.compile(loss='mse', optimizer='sgd')

for step in range(3000):
    cost = model.train_on_batch(TRAIN_X, TRAIN_Y)
    if (step % 50 == 0):
        print('cost:', cost)

W, b = model.layers[0].get_weights()

print('Weights=', W, '\nbiases=', b)

TEST_Y = model.predict(TRAIN_X)

plt.scatter(TRAIN_X, TRAIN_Y)
plt.plot(TRAIN_X, TEST_Y)

plt.show()

# 3000 :0.00017362389,Weights= [[0.28055158]],biases= [0.0111051]
# 1000:cost: 0.0044718906,Weights= [[0.5304448]],biases= [-0.1307068]
