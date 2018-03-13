import numpy as np
import matplotlib.pyplot as plt
import keraslearn
from keras.utils import np_utils


def getTrainForLineNormal(size=100, W_PARAM=0.1, W_B=0.03):
    arr_x = np.random.random(100)
    noise = np.random.normal(0, 10, arr_x.shape)
    print(noise)
    arr_y = arr_x * W_PARAM + W_B + noise
    return arr_x, arr_y


def getTrainForNoneLine(size=100):
    arr_x = np.linspace(-0.5, 0.5, size)
    noise = np.random.normal(0, 0.02, arr_x.shape)
    arr_y = np.square(arr_x) + noise
    return arr_x, arr_y


def oneHot(arr):
    y_train = np_utils.to_categorical(arr)
    print(y_train)


if __name__ == "__main__":
    method_name = input("Enter your input:")
    if method_name == 'getTrainForNoneLine':
        getTrainForNoneLine()
    elif method_name == '1':
        arr = [0, 1, 2, 3]
        new_arr = oneHot(arr)
        print(new_arr)
