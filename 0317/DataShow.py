import matplotlib.pyplot as plt

import DataBuilder

train_x, train_y = DataBuilder.buildNonLineRegressionData()

plt.scatter(train_x, train_y)

plt.show()
