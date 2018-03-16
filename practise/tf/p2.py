import pandas as pd
import tensorflow as tf

df = pd.read_csv("data", header=None)

train_data = df.values;

train_X = train_data[:, :-1]
train_y = train_data[:, -1:]

# 2维度
feature_num = len(train_X[0])
sample_num = len(train_X)
print("Size of train_X: {}x{}".format(sample_num, feature_num))
print("Size of train_y: {}x{}".format(len(train_y), len(train_y[0])))

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

# 训练目标
W = tf.Variable(tf.zeros([feature_num, 1]))
b = tf.Variable([-.9])


