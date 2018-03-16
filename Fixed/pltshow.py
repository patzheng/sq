import numpy as np

import matplotlib.pyplot as plt

axis_x = np.random.random(100)

noise = np.random.normal(0, 0.1, 100)

axis_y = axis_x * 3 + 0.5 + noise

plt.scatter(axis_x, axis_y)

plt.show()
