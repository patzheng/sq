import tensorflow as tf

import numpy as np

train_x = np.random.random(100)

noise = np.random.normal(0, 0.1, 100)

train_y = train_x * 0.1 + noise

# 构建 y = x*W +b

W = tf.Variable(tf.random_uniform([1]))
b = tf.Variable(tf.Zeros[1])

y = W * train_x + b

cost = tf.reduce_mean(tf.square(y - train_y))

op = tf.train.GradientDescentOptimizer(0.01)

train = op.minimize(cost)

with tf.Session() as session:
    init = tf.global_variables_initializer()
    session.run(init)
