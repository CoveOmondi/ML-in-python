import numpy as np
from matplotlib import pyplot as plt
x = np.random.uniform(0.0, 5.0, 300)

plt.hist(x, 100)
plt.show()