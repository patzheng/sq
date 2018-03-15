import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

train_images = mnist.train.images
train_labels = mnist.train.labels

test_images = mnist.test.images
test_labels = mnist.test.labels

# 5W个图片  现在已经是28*28个像素 图片的像素也已经除以255
print(train_images.shape)
# 5W个图片数字内容 10个数字输出
print(train_labels.shape)

# 1W个图片  现在已经是28*28个像素
print(test_images.shape)
# 1W个图片数字内容 10个数字输出
print(test_labels.shape)

print(train_images[0])





# 获取验证数据和训练数据
