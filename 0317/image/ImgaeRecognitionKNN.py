import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils
from keras.layers import Dense
from keras.optimizers import SGD
from keras.models import Sequential

label_szie = 10
image_weight = 28
image_height = 28

# 载入数据
(train_x, train_y), (test_x, test_y) = mnist.load_data()
train_x = train_x.reshape(train_x.shape[0], train_x.shape[1] * train_x.shape[2]) / 255.0
print(train_x)
print(train_y)
train_y = np_utils.to_categorical(train_y, num_classes=label_szie)
test_x = test_x.reshape(test_x.shape[0], test_x.shape[1] * test_x.shape[2]) / 255.0
test_y = np_utils.to_categorical(test_y, num_classes=label_szie)
# 输入图片的长度和高度 得到标签
model = Sequential([
    Dense(units=10, input_dim=image_weight * image_height, bias_initializer='one', activation='softmax')
])
sgd = SGD(lr=0.1)
# 定义优化器 loss function
model.compile(optimizer=sgd, loss='mse', metrics=['accuracy'])

model.fit(train_x, train_y, batch_size=32, epochs=10)

loss, accuracy = model.evaluate(test_x, test_y)

print('loss:', loss, 'accuracy:', accuracy)
