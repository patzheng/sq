'''

'''
from keras.utils import np_utils
from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import SGD
import ImageUtil

train_x, train_y = ImageUtil.load_data()

# (60000, 28, 28)
print("train_x's shape ", train_x.shape)

# (60000,)
print("train_y's shape ", train_y.shape)

train_x = train_x.reshape(train_x.shape[0], -1) / 255.0
# test_x = test_x.reshape(test_x.shape[0], -1) / 255.0

# print(test_x.shape)
# print(test_x[0].shape)

train_y = np_utils.to_categorical(train_y, num_classes=10)
# test_y = np_utils.to_categorical(test_y, num_classes=10)

# 输入是784（28*28）个神经元 输出是10个神经元

model = Sequential([
    # softmaz 将输出转成概率
    Dense(units=10, input_dim=1400, bias_initializer='one', activation='softmax')
])

# 定义优化器
sgd = SGD(lr=0.1)

model.compile(
    optimizer=sgd,
    #loss='categorical_crossentropy'
    loss='mse',
    # 可以输出准确率
    metrics=['accuracy']
)

# 开始训练

# 每次训练32张图片 迭代周期是10:60000张图片 ，每次回拿到60000的32张 60000%12*10个周期
model.fit(train_x, train_y, batch_size=32, epochs=100)

model.save('model/StatndNumberCustomerImage.h5')
