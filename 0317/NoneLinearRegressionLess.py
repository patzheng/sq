from keras.models import Sequential, load_model
from keras.layers import Dense, Activation
from keras.optimizers import SGD
import matplotlib.pyplot as plt
import DataBuilder


def buildModel():
    model = Sequential()
    # 1-10-1 第一层
    # line model.add(Dense(input_dim=1, units=1, use_bias=True))
    # [1,10] * [10,1]=[1,1]
    model.add(Dense(input_dim=1, units=10,use_bias=True))
    model.add(Activation('tanh'))

    model.add(Dense(units=1))
    model.add(Activation('tanh'))

    # 增加学习率 降低迭代次数
    sgd = SGD(lr=0.1)
    model.compile(optimizer=sgd, loss='mse')

    train_x, train_y = DataBuilder.buildNonLineRegressionData(data_size=100)

    for step in range(13000):
        cost = model.train_on_batch(train_x, train_y)
        if step % 500 == 0:
            print("step:", step, "cost:", cost)
    model.save('model/NoneLinearRegressionLess.h5')


def testModel():
    model = load_model('model/NoneLinearRegressionLess.h5')
    test_x, test_y = DataBuilder.buildNonLineRegressionData(data_size=100)
    predict_y = model.predict(test_x)
    plt.scatter(test_x, test_y)
    plt.plot(test_x, predict_y)
    plt.show()


if __name__ == "__main__":
    testModel()
