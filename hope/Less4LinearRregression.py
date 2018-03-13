# 第一课 线性回归 for Keras
import matplotlib.pyplot as plt
import numpy as np
from keras import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

train_x = np.random.random(100)
np.random.shuffle(train_x)  # randomize the data 扰乱顺序
train_y = 0.5 * train_x + 2 + np.random.normal(0, 0.05, (100,))
# plot data

model = Sequential()

dense = Dense(input_dim=1, units=1, use_bias=True)

model.add(dense)

sgd = SGD(lr=0.02)

model.compile(sgd, loss='mse')

for step in range(3000):
    cost = model.train_on_batch(train_x, train_y)
    if step % 100 == 0:
        print('train cost: ', cost)

cost = model.evaluate(train_x, train_y, batch_size=40)
print('test cost:', cost)
W, b = model.layers[0].get_weights()
print('Weights=', W, '\nbiases=', b)

Y_pred = model.predict(train_x)
plt.scatter(train_x, train_y)
plt.plot(train_x, Y_pred)
plt.show()
