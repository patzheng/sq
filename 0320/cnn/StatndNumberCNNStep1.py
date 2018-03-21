'''

'''
from keras.datasets import mnist
from keras.utils import np_utils
from keras.layers import Dense, Dropout, Convolution2D, MaxPooling2D, Flatten
from keras.models import Sequential
from keras.optimizers import SGD, Adam
from IPython.display import Image

(train_x, train_y), (test_x, test_y) = mnist.load_data()

# (60000, 28, 28)
print(train_x.shape)

# (60000,)
print(train_y.shape)

train_x = train_x.reshape(-1, 28, 28, 1) / 255.0
test_x = test_x.reshape(-1, 28, 28, 1) / 255.0

train_y = np_utils.to_categorical(train_y, num_classes=10)
test_y = np_utils.to_categorical(test_y, num_classes=10)

# 输入是784（28*28）个神经元 输出是10个神经元

model = Sequential()
# 定义一个卷积层
# input_shape 输入平面
# filter：滤波器个数
# strides 步长
# padding same
model.add(Convolution2D(
    input_shape=(28, 28, 1),
    filters=32,
    kernel_size=5,
    strides=1,
    padding='same',
    activation='relu'
))
# 32* 28*28
# 第一个池化层
model.add(MaxPooling2D(
    pool_size=2,
    strides=2,
    padding='same'
))

# 32*14*14
# 第二个卷积层
model.add(Convolution2D(64, 5, strides=1, padding='same', activation='relu'))
# 第二个池化层 64*14*14 /2 /2=1024
model.add(MaxPooling2D(2, 2, 'same'))

# 将第二个池化层的输出扁平化为一维
model.add(Flatten())

# 第一个全连接层

model.add(Dense(1024, activation='relu'))

model.add(Dropout(0.5))

model.add(Dense(10, activation='softmax'))

adam = Adam(lr=1e-4)

# 定义优化器
sgd = SGD(lr=0.1)

model.compile(
    optimizer=adam,
    loss='categorical_crossentropy',
    # 可以输出准确率
    metrics=['accuracy']
)

# 开始训练

# 每次训练32张图片 迭代周期是10:60000张图片 ，每次回拿到60000的32张 60000%12*10个周期
model.fit(train_x, train_y, batch_size=32, epochs=1)

loss, accuracy = model.evaluate(test_x, test_y)

print('loss:', loss, 'accuracy', accuracy)

test_sub_x = test_x[0:1]

test_ans = model.predict(test_sub_x)

print(type(test_ans))

print(len(test_ans))

print('result:', test_ans[0])
