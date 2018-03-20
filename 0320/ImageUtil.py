# 如何得到train_x和Train_y
import os
from PIL import Image
import numpy as np
from keras.datasets import mnist

'''
'''


def test():
    (train_x, train_y), (test_x, test_y) = mnist.load_data()
    print(train_x.shape)
    print(train_y.shape)


def load_data():
    print('load data from image')
    imgs = os.listdir("/Users/pat/research/stick/train/")
    num = len(imgs)
    print("num", num)
    data = np.empty((num, 50, 28), dtype="float32")
    label = np.empty((num,), dtype="uint8")

    i = 0
    for imgFile in imgs:
        img = Image.open("/Users/pat/research/stick/train/" + imgFile).convert('L')
        arr = np.asarray(img, dtype="float32")
        data[i, :, :] = arr
        label[i] = int(imgs[i].split('.')[0].split('_')[1])
        i = i + 1
    return data, label




if __name__ == "__main__":
    data, label = load_data()
    (train_x, train_y), (test_x, test_y) = mnist.load_data()

    print(label[0])
    print(train_y[0])

    print(data[0])
    print(train_x[0])
