from keras.models import Sequential, load_model
from keras.layers import Dense
import matplotlib.pyplot as plt

import DataBuilder


def buildModel():
    model = Sequential()
    model.add(Dense(input_dim=1, units=1, use_bias=True))
    model.compile(loss='mse', optimizer='sgd')
    train_x, train_y = DataBuilder.buildLineRegressionData(data_size=100, Weights=0.1, biases=0.2)
    for step in range(3000):
        cost = model.train_on_batch(train_x, train_y)
        if step % 100 == 0:
            W, b = model.layers[0].get_weights()
            print("step:", step, "cost:", cost, "W:", W, "b:", b)
    model.save('model/linearRegressionLess.h5')


def testModel():
    model = load_model("model/linearRegressionLess.h5")
    test_x, test_y = DataBuilder.buildLineRegressionData(data_size=100, Weights=0.1, biases=0.2)
    predict_y = model.predict(test_x)
    plt.scatter(test_x, test_y)
    plt.plot(test_x, predict_y)
    plt.show()


if __name__ == "__main__":
    testModel()
# buildModel()
# use model
