import tensorflow as tf
import numpy as np

x_data = np.random.rand(100)
noise = np.random.normal(0, 0.01, 100)
y_data = x_data * 0.1 + 0.3 + noise
#y_data = x_data * 0.1 + 0.3

# x_data = np.random.random(100)
# noise = np.random.normal(0, 0.01, x_data.shape)
# y_data = x_data * 0.1 + 100 + noise

Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases

loss = tf.reduce_mean(tf.square(y - y_data))

optimizer = tf.train.GradientDescentOptimizer(0.1)

train = optimizer.minimize(loss)

init = tf.initialize_all_variables()

sess = tf.Session()

sess.run(init)

for step in range(20000):
    sess.run(train)
    if step % 20 == 0:
        print('step:', step, 'weights:', sess.run(Weights), 'biases:', sess.run(biases), 'loss:', sess.run(loss))
