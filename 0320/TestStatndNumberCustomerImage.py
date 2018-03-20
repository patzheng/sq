'''

'''
from keras.utils import np_utils
from keras.layers import Dense
from keras.optimizers import SGD
from keras.models import Sequential, load_model
import ImageUtil
from PIL import Image
import numpy as np

data = np.empty((1, 50, 28), dtype="float32")
img = Image.open("/Users/pat/Documents/ml/sq/0320/train/1706_2.jpg").convert('L')
arr = np.asarray(img, dtype="float32")
data[0, :, :] = arr

train_x = data.reshape(data.shape[0], -1) / 255.0

model = load_model("model/StatndNumberCustomerImage.h5")

predict_y = model.predict(train_x)

print('cL', predict_y)

maxx = np.max(predict_y)

print(maxx)

print('max:', maxx)
