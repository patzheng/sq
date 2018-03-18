# 逻辑回归
# collect the training data

import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation
from keras.optimizers import SGD, Adagrad

#拿到

def buildModel():
    train_x = np.array([[1, 5], [2, 7], [9, 14], [6, 10], [8, 21], [16, 19],
                        [5, 1], [7, 2], [14, 9], [10, 6], [21, 8], [19, 16]])
    train_y = np.array([[1], [1], [1], [1], [1], [1],
                        [0], [0], [0], [0], [0], [0]])
    model = Sequential()
    model.add(Dense(units=1, input_dim=2, activation=None, use_bias=False))
    model.add(Activation('sigmoid'))

    agd = Adagrad(lr=0.1, epsilon=1e-8)

    model.compile(optimizer=agd, loss='binary_crossentropy', metrics=['accuracy'])

    model.fit(train_x, train_y, batch_size=4, epochs=100, shuffle=True)
    model.fit(train_x, train_y, batch_size=12, epochs=100, shuffle=True)

    model.save('model/LogisticRegressionLess.h5')


def testModel():
    model = load_model("model/LogisticRegressionLess.h5")
    test_ans = model.predict(np.array([[2, 20], [20, 2], [3, 30], [30, 3]]), batch_size=2)
    print(type(test_ans))
    print(test_ans)


if __name__ == "__main__":
    testModel()
