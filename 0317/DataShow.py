import matplotlib.pyplot as plt

import DataBuilder

train_x, train_y = DataBuilder.buildLineRegressionData()

plt.scatter(train_x, train_y)

plt.show()


