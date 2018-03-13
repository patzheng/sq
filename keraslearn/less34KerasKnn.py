import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD
from keras.datasets import mnist
from keras.utils import np_utils
import DataBuilder

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

num_pixels = x_train.shape[1] * x_train.shape[2]

# 输入的需要reshape
x_train_re = x_train.reshape(x_train.shape[0], num_pixels).astype('float32') / 255.0
x_test_re = x_test.reshape(x_test.shape[0], num_pixels).astype('float32') / 255.0
# 标签需要onehot  
y_train_re = np_utils.to_categorical(y_train)
y_test_re = np_utils.to_categorical(y_test)

model = Sequential([
    Dense(units=10, input_dim=28 * 28, bias_initializer='one', activation='softmax')
])

sgd = SGD(lr=0.2)

model.compile(
    optimizer=sgd,
    loss='mse',
    metrics=['accuracy'],
)
model.fit(x_train_re, y_train_re, batch_size=32, epochs=20)

loss, accuracy = model.evaluate(x_test_re, y_test_re);

print('loss:', loss, 'accuracy:', accuracy)
