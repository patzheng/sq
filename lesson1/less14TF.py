import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

'''
确定2种变量之间的关系
'''
'''
获取线性回归训练参数
'''


def getTrainForLineNormal(size=100, W_PARAM=0.1, W_B=0.03):
    arr_x = np.random.random(100)
    noise = np.random.normal(0, 0.01, arr_x.shape)
    arr_y = arr_x * W_PARAM + W_B + noise
    return arr_x, arr_y


'''
显示坐标
'''


def showPoint(x, y):
    plt.scatter(x, y)
    plt.show();


# y = w*x +b
def train():
    train_x, train_y = getTrainForLineNormal(1000)
    # 均匀分布
    W = tf.Variable(tf.random_uniform([1]))
    b = tf.Variable(tf.zeros([1]))
    # 将训练的X代入函数
    y = W * train_x + b

    # 用预测的Y值和真实的Y值进行平方求平均数
    cost = tf.reduce_mean(tf.square(y - train_y))
    # 梯度下降 0.08 下降的幅度 尽可能小一点
    optimizer = tf.train.GradientDescentOptimizer(0.08)
    train = optimizer.minimize(cost)

    with tf.Session() as sess:
        init = tf.global_variables_initializer();
        sess.run(init)
        print('cost:', sess.run(cost), 'W=', sess.run(W), 'b=', sess.run(b))
        for k in range(1000):
            sess.run(train)
            print('cost:', sess.run(cost), 'W=', sess.run(W), 'b=', sess.run(b))
        print("执行完成")

        plt.plot(train_x, train_y)

        plt.plot(train_x, sess.run(y))

        plt.legend()

        plt.show()


def tfLearn():
    e = tf.square(2);
    f = tf.reduce_mean([1, 4])
    g = tf.random_uniform([2, 10])
    with tf.Session() as sess:
        init = tf.global_variables_initializer()
        sess.run(init)
        print("e是2的平方？", sess.run(e))
        print("f是求平均值？", sess.run(f))
        print("g是均匀分布的随机数？", sess.run(g))


if __name__ == "__main__":
    method_name = input("Enter your input:")
    if method_name == 'tfLearn':
        tfLearn()
    elif method_name == 'train':
        train();
