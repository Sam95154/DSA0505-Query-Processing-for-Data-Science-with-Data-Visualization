import matplotlib.pyplot as plt
import numpy as np
x = np.random.rand(100)
y = np.random.rand(100)
plt.scatter(x, y, label='Random Data', color='red')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Scatter Plot of Random Data')
plt.legend()
plt.show()
