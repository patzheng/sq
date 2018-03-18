import numpy as np

'''
获取线性回归训练数据
'''


def buildLineRegressionData(data_size=100, Weights=0.1, biases=0.2):
    train_x = np.random.random(data_size)
    noise = np.random.normal(0, 0.01, data_size)
    train_y = train_x * Weights + biases + noise
    return train_x, train_y


def buildNonLineRegressionData(data_size=100):
    train_x = np.linspace(-0.5, 0.5, data_size)
    noise = np.random.normal(0, 0.01, data_size)
    train_y = np.square(train_x) + noise
    return train_x, train_y

    if __name__ == "__main__":
        buildLineRegressionData()
