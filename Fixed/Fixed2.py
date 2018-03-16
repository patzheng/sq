import numpy as np

import matplotlib.pyplot as plt

import tensorflow as tf

axis_x = np.random.random(100)

noise = np.random.normal(0, 0.1, 100)

axis_y = axis_x * 3 + 0.5 + noise

plt.scatter(axis_x, axis_y)

# plt.show()

# 占位
train_x = tf.placeholder(tf.float32)
# 占位
train_y = tf.placeholder(tf.float32)

Weight = tf.Variable(0.0)

biases = tf.Variable(0.0, tf.float32)

y_model = Weight * train_x + biases

init = tf.global_variables_initializer()

# 先说cost

cost = tf.reduce_mean(tf.square(y_model - axis_y))

optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

with tf.Session() as sess:
    sess.run(init)
    for step in range(10000):
        sess.run(optimizer, feed_dict={train_x: axis_x, train_y: axis_y})
        if step % 100 == 0:
            print(sess.run(Weight))
            print(sess.run(biases))
