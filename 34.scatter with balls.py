import matplotlib.pyplot as plt
import numpy as np
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = np.random.randint(10,100, size=(100))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='viridis')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Scatter Plot with Randomly Sized Balls')
plt.legend()
plt.show()
