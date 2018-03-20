# 如何得到train_x和Train_y
import os
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from PIL import Image
import numpy as np


def load_data():
    data = np.empty((100, 1, 50, 28), dtype="float32")
    label = np.empty((100,), dtype="uint8")
    imgs = os.listdir("../data/train/")
    i = 0
    for imgFile in imgs:
        img = Image.open("../data/train/" + imgFile).convert('L')
        arr = np.asarray(img, dtype="float32")
        data[i, :, :, :] = arr
        label[i] = int(imgs[i].split('.')[0].split('_')[1])
        i = i + 1
    return data, label


if __name__ == "__main__":
    data, label = load_data()
    for i in label:
        print("label:", i)
