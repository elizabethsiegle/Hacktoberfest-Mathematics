# plot an histogram using matplotlib package
import numpy as np
import matplotlib.pyplot as plt
data = np.random.randn(500)
plt.hist(data)
plt.show()
