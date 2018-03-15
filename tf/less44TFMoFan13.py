# 激励函数

# 不能用线性方程能概括的问题

# 掰弯利器

import tensorflow as tf


# None:线性函数 y=w*x+b
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros[1, out_size] + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        # 作为激励函数的参数
        outputs = activation_function(Wx_plus_b)
    return outputs
