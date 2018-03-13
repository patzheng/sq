import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD
from keras.datasets import mnist

import DataBuilder

model = Sequential()
model.add(Dense(units=10, input_dim=1))
model.add(Activation('tanh'))
model.add(Dense(units=1))
model.add(Activation('tanh'))

# 将梯度下降算法的下降度提高
sgd = SGD(lr=0.3)
# sgd 随机梯度下降法 loss：均方误差
model.compile(optimizer=sgd, loss='mse')
# model.compile(optimizer='sgd', loss='mse')

x_train, y_train = DataBuilder.getTrainForNoneLine()

for step in range(3000):
    cost = model.train_on_batch(x_train, y_train)
    if step % 100 == 0:
        print('cost:', cost)
W, b = model.layers[0].get_weights()

print("W", W, 'b:', b)
y_pred = model.predict(x_train)

plt.scatter(x_train, y_train)
plt.plot(x_train, y_pred)
plt.show()
