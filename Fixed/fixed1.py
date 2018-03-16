'''

测试线性回归

y=W*x=B

其中W为权重，b为偏置。

权重和偏执都需要监督学习之后才能得到
我们只是提供训练样本
,0
 !.设置各种超参数，例如学习率，迭代次数等；
 !.定义变量和模型；
 !.初始化变量;
 !.正式开始训练.


换种思路
'''

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

train_x = np.random.random(100)
noise = np.random.normal(0, 1, 100)
noise = 0
train_y = train_x * 10 + 3 + noise

# 用placeholder的地方都需要后面进行替换
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(np.random.rand())
b = tf.Variable(np.random.rand())

# 预测值
activation = X * W + b
# 损失函数
cost = tf.reduce_mean(tf.square(activation - train_y))
# 梯度下降
optimizer = tf.train.GradientDescentOptimizer(0.001).minimize(cost)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for step in range(58500):
        sess.run(optimizer, feed_dict={X: train_x, Y: train_y})
        if step % 500 == 0:
            print("step:", step, 'b:', sess.run(b), 'w:', sess.run(W))

    print("b:%f" % sess.run(b))
    print("W:%f" % sess.run(W))
