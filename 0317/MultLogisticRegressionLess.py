import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation
from keras.optimizers import SGD, Adagrad, RMSprop
from keras.datasets import mnist
from keras.utils import np_utils
import pandas as pd

# 先设置一个默认的随机值
seed = 7
np.random.seed(seed)

iris_data = pd.read_csv('./data/iris', header=None)

iris_data_values = iris_data.values

train_x = iris_data_values[:, 0: 4].astype(float)
train_y = iris_data_values[:, 4:]
train_y = np_utils.to_categorical(train_y)

print(train_x)
print(train_y)


def buildModel():
    model = Sequential([
        Dense(4, input_dim=4),
        Activation('relu'),
        Dense(3),
        Activation('softmax')
    ])

    rmsprop = RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

    model.compile(optimizer=rmsprop,
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    model.fit(train_x, train_y, epochs=2000, batch_size=32)

    loss, accuracy = model.evaluate(train_x, train_y)

    print('test loss: ', loss)
    print('test accuracy: ', accuracy)


if __name__ == "__main__":
    buildModel()
    # buildModel()
    # use model
